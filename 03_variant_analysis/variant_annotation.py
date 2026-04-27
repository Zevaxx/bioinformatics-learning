#!/usr/bin/env python3
"""
Variant analysis with a pharmacogenomics focus.

This script demonstrates the basics of VCF analysis:
1. Read a VCF file
2. Filter by quality and frequency
3. Identify variants in pharmacogenes
4. Generate a clinical report

Usage:
    python variant_annotation.py <input.vcf>

Required dependencies:
    pip install pyvcf3

Optional (faster alternative):
    pip install cyvcf2
"""

import sys
from pathlib import Path

# Approximate genomic coordinates of pharmacogenes (GRCh38)
# In a real project these would come from Ensembl or UCSC
PHARMACOGENES = {
    "CYP2D6":  {"chrom": "22", "start": 42126499, "end": 42130881,
                "drugs": ["Codeine", "Tramadol", "Tamoxifen", "SSRIs"]},
    "CYP2C19": {"chrom": "10", "start": 94762681, "end": 94855547,
                "drugs": ["Clopidogrel", "Omeprazole", "Voriconazole"]},
    "CYP2C9":  {"chrom": "10", "start": 94938658, "end": 94989390,
                "drugs": ["Warfarin", "NSAIDs", "Phenytoin"]},
    "VKORC1":  {"chrom": "16", "start": 31102175, "end": 31106320,
                "drugs": ["Warfarin"]},
    "TPMT":    {"chrom": "6",  "start": 18130918, "end": 18155374,
                "drugs": ["Azathioprine", "6-MP", "Thioguanine"]},
    "DPYD":    {"chrom": "1",  "start": 97543300, "end": 98388615,
                "drugs": ["5-FU", "Capecitabine"]},
}


def normalize_chrom(c):
    """Normalize chromosome name (handle 'chr1' vs '1')."""
    return str(c).lstrip("chr").upper()


def parse_vcf(vcf_path):
    """
    Read a VCF file and yield filtered variants.

    Returns a generator of dicts with: chrom, pos, ref, alt, qual, filter, info.

    NOTE: this is a minimal manual parser for didactic purposes.
    In production, use cyvcf2 (fast) or pyvcf3.
    """
    with open(vcf_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            fields = line.split("\t")
            if len(fields) < 8:
                continue

            chrom, pos, vid, ref, alt, qual, filt, info = fields[:8]

            # Parse INFO into a dict
            info_dict = {}
            for kv in info.split(";"):
                if "=" in kv:
                    k, v = kv.split("=", 1)
                    info_dict[k] = v
                else:
                    info_dict[kv] = True

            yield {
                "chrom":  chrom,
                "pos":    int(pos),
                "id":     vid,
                "ref":    ref,
                "alt":    alt,
                "qual":   float(qual) if qual != "." else None,
                "filter": filt,
                "info":   info_dict,
            }


def filter_variants(variants, min_qual=20.0, max_af=0.05):
    """
    Filter variants by quality and allele frequency.

    - min_qual: minimum quality (Phred score)
    - max_af:   max population frequency (rare variants are more clinically interesting)
    """
    for v in variants:
        # Skip variants that did not PASS
        if v["filter"] not in ("PASS", "."):
            continue

        # Quality filter
        if v["qual"] is not None and v["qual"] < min_qual:
            continue

        # Allele frequency filter (if available in INFO)
        af = v["info"].get("AF")
        if af is not None and af is not True:
            try:
                af_value = float(str(af).split(",")[0])
                if af_value > max_af:
                    continue
            except (ValueError, TypeError):
                pass

        yield v


def find_pharmacogene_variants(variants):
    """Identify variants located in pharmacogenes."""
    results = {gene: [] for gene in PHARMACOGENES}

    for v in variants:
        v_chrom = normalize_chrom(v["chrom"])

        for gene, info in PHARMACOGENES.items():
            if (normalize_chrom(info["chrom"]) == v_chrom
                    and info["start"] <= v["pos"] <= info["end"]):
                results[gene].append(v)

    return results


def generate_clinical_report(pharmacogene_variants):
    """Generate a basic clinical report."""
    print("=" * 70)
    print("           PHARMACOGENOMICS REPORT (DEMO)")
    print("=" * 70)
    print()
    print("⚠️  WARNING: this is a didactic example.")
    print("   For real clinical decisions consult CPIC or PharmGKB.")
    print()

    total = sum(len(v) for v in pharmacogene_variants.values())

    if total == 0:
        print("✅ No variants detected in known pharmacogenes.")
        print("   (Note: this depends on input VCF coverage)")
        return

    print(f"⚠️  {total} variants detected in pharmacogenes:\n")

    for gene, variants in pharmacogene_variants.items():
        if not variants:
            continue

        info = PHARMACOGENES[gene]
        print(f"--- {gene} ---")
        print(f"  Affected drugs: {', '.join(info['drugs'])}")
        print(f"  Variants found: {len(variants)}")

        for v in variants[:5]:  # show first 5 only
            print(f"    {v['chrom']}:{v['pos']} {v['ref']}>{v['alt']} "
                  f"(QUAL={v['qual']}, ID={v['id']})")

        if len(variants) > 5:
            print(f"    ... and {len(variants) - 5} more")
        print()

    print("📋 Recommended next steps:")
    print("  1. Annotate variants with VEP or SnpEff")
    print("  2. Cross-reference with PharmGKB and CPIC")
    print("  3. Consult clinical guidelines for the patient's drugs")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    vcf_path = Path(sys.argv[1])
    if not vcf_path.exists():
        print(f"Error: file not found: {vcf_path}")
        sys.exit(1)

    print(f"📂 Reading {vcf_path}...")

    variants = parse_vcf(vcf_path)
    filtered = list(filter_variants(variants, min_qual=20.0, max_af=0.05))

    print(f"   {len(filtered)} variants passed filters (QUAL≥20, AF≤5%)")

    pharmacogene_variants = find_pharmacogene_variants(filtered)
    generate_clinical_report(pharmacogene_variants)


if __name__ == "__main__":
    main()
