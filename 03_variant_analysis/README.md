# 🧬 Module 03: Variant Analysis (Pharmacogenomics Focus)

## 🎯 Objectives

By the end of this module you will be able to:

1. Read and parse VCF files in Python
2. Filter variants by quality, allele frequency and other criteria
3. Annotate variants with population frequencies (gnomAD)
4. Identify clinically relevant variants (ClinVar / PharmGKB)
5. Apply pharmacogenomics: from a *CYP2D6* variant to a clinical recommendation

---

## 📖 Brief theory

A **genetic variant** is a difference between an individual's DNA and a reference genome. Types:

- **SNV** (Single Nucleotide Variant): a single base change. Example: `A>G`.
- **Indel**: insertion or deletion of one or more bases.
- **CNV** (Copy Number Variant): duplications / deletions of large regions.
- **SV** (Structural Variant): inversions, translocations, large deletions.

### VCF (Variant Call Format)

The standard format. Each line describes a variant with:

- Position (chromosome, coordinate)
- REF and ALT alleles
- Quality (QUAL)
- Filter (PASS or rejected)
- INFO (annotations: depth, frequency, etc.)
- FORMAT + sample data (genotype, etc.)

### 💊 Pharmacogenomics

Pharmacogenomics studies how genetic variants affect an individual's drug response. **Key examples**:

| Gene | Affected drugs | Variants of interest |
|------|----------------|----------------------|
| **CYP2D6** | Codeine, antidepressants, tamoxifen | `*4`, `*10`, `*17` (loss of function) |
| **CYP2C19** | Clopidogrel, omeprazole | `*2`, `*3` (loss of function) |
| **CYP2C9** | Warfarin, NSAIDs | `*2`, `*3` (slow metabolism) |
| **VKORC1** | Warfarin | rs9923231 (sensitivity) |
| **TPMT** | Thiopurines (azathioprine) | `*2`, `*3A` (severe toxicity) |
| **HLA-B*57:01** | Abacavir | hypersensitivity (severe) |
| **DPYD** | 5-fluorouracil | `*2A` (lethal toxicity) |

A patient who is a **CYP2D6 poor metabolizer** receiving codeine may have **no analgesic effect** (codeine is a prodrug — needs CYP2D6 to convert to morphine). One who is an **ultra-rapid metabolizer** may suffer **respiratory depression**.

This is exactly where your pharmacy training adds enormous value.

---

## 🛠️ Practical example

[`variant_annotation.py`](./variant_annotation.py) demonstrates:

- Reading a VCF with `cyvcf2`
- Filtering variants by quality and allele frequency
- Identifying variants in pharmacogenes
- Generating a clinical report with annotations

---

## 💡 For SQL devs

This is where your SQL background really shines:

- **PharmGKB** distributes downloadable TSV/CSV that loads cleanly into SQLite/Postgres
- **ClinVar** has SQL-style downloads
- **gnomAD** is available in **BigQuery** — you can run SQL queries directly on the global reference

Example BigQuery:
```sql
SELECT chrom, pos, ref, alt, AF
FROM `bigquery-public-data.gnomAD.v3_genomes__chr22`
WHERE pos BETWEEN 42126499 AND 42130881  -- approximate CYP2D6
  AND AF > 0.01
ORDER BY AF DESC
```

---

## 📝 Suggested exercises

1. **Easy**: download a VCF from the 1000 Genomes Project and count how many variants pass `PASS`.
2. **Medium**: filter variants in a 1 Mb window around the *CYP2D6* gene.
3. **Medium**: build a minimal SQLite database with PharmGKB and query "drug → pharmacogene".
4. **Hard**: download a complete ClinVar VCF and identify all "Pathogenic" variants in the *BRCA1* gene.
5. **Pharma-focused**: simulate a clinical case — patient with *CYP2D6 \*4/\*4* genotype receiving tramadol. Generate a report with the recommendation.

---

## 📚 Additional resources

- [PharmGKB](https://www.pharmgkb.org/) — pharmacogenomics database (essential)
- [CPIC Guidelines](https://cpicpgx.org/guidelines/) — official clinical guidelines
- [VEP (Variant Effect Predictor)](https://www.ensembl.org/info/docs/tools/vep/) — best annotator
- [GATK Variant Filtering](https://gatk.broadinstitute.org/hc/en-us/articles/360035890471) — best practices
- [cyvcf2 Documentation](https://brentp.github.io/cyvcf2/)
