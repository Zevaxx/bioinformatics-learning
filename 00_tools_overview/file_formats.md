# 📄 Bioinformatics File Formats

Each domain has its own file formats. Knowing the most common ones — and which tool produces / consumes each — is essential.

---

## Summary table

| Format | Extension | Domain | Content | Binary? |
|--------|-----------|--------|---------|---------|
| FASTA | `.fa`, `.fasta`, `.fna` | Sequences | DNA/RNA/protein sequences | No |
| FASTQ | `.fq`, `.fastq` | Sequences | Reads + quality scores | No |
| SAM | `.sam` | Alignments | Reads aligned to a reference | No |
| BAM | `.bam` | Alignments | SAM compressed (binary) | Yes |
| CRAM | `.cram` | Alignments | Reference-compressed BAM | Yes |
| VCF | `.vcf` | Variants | Genomic variants | No |
| BCF | `.bcf` | Variants | VCF compressed (binary) | Yes |
| GFF / GTF | `.gff`, `.gff3`, `.gtf` | Annotation | Gene / feature locations | No |
| BED | `.bed` | Annotation | Genomic intervals | No |
| Wig / BigWig | `.wig`, `.bw` | Tracks | Continuous coverage signals | Mixed |
| PDB | `.pdb` | Structure | 3D protein structure | No |
| mmCIF | `.cif`, `.mmcif` | Structure | Modern PDB replacement | No |
| SDF / MOL | `.sdf`, `.mol` | Chemistry | 2D/3D molecules | No |
| SMILES | `.smi` | Chemistry | Linear molecule notation | No |
| MAF | `.maf` | Variants | Mutation Annotation Format (TCGA) | No |

---

## 🧬 FASTA — sequences

The simplest format. A header line starting with `>` followed by lines of sequence.

```
>NM_001301717.2 Homo sapiens cytochrome P450 family 2 subfamily D6 (CYP2D6)
ATGGGGCTAGAAGCACTGGTGCCCCTGGCCGTGATAGTGGCCATCTTCCTG
CTGCTGGTGGACCTGATGCACCGGCGCCAGCGCTGGGCTGCACGCTACCCA
```

**Tools**: Biopython (`SeqIO`), `seqkit`, `samtools faidx`.

---

## 🧬 FASTQ — reads with quality

Output of sequencers. Four lines per read:
```
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
+
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65
```

1. Header (`@`)
2. Sequence
3. Separator (`+`)
4. Per-base quality (PHRED score)

**Tools**: `fastqc`, `trimmomatic`, `cutadapt`, `seqkit`.

---

## 🎯 SAM / BAM / CRAM — alignments

**SAM** (Sequence Alignment/Map) is the standard format for aligned reads. **BAM** is its binary, compressed form. **CRAM** compresses against the reference.

```
@HD VN:1.6 SO:coordinate
@SQ SN:chr1 LN:248956422
read1 0 chr1 1000 60 100M * 0 0 ACGT... IIII...
```

Key columns: read name, flags (bitwise), reference, position, mapping quality, CIGAR, sequence, qualities.

**Tools**: `samtools`, `picard`, `htsjdk` (Java/Kotlin), `pysam` (Python).

---

## 🧬 VCF / BCF — variants

**Variant Call Format**. The standard for SNPs, indels and structural variants.

```
##fileformat=VCFv4.2
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
#CHROM  POS     ID      REF  ALT  QUAL  FILTER  INFO        FORMAT  SAMPLE1
chr22   16050075 rs587  A    G    99    PASS    DP=30;AF=0.5 GT:DP   0/1:30
```

**Tools**: `bcftools`, `vcftools`, `pyvcf3`, `cyvcf2`, GATK, Picard.

---

## 📍 GFF / GTF — annotation

**General Feature Format** / **Gene Transfer Format**. Describes features on a genome (genes, exons, CDS).

```
chr1  HAVANA  gene        11869  14409  .  +  .  gene_id "ENSG00000223972"
chr1  HAVANA  transcript  11869  14409  .  +  .  transcript_id "ENST00000456328"
chr1  HAVANA  exon        11869  12227  .  +  .  exon_number "1"
```

**Tools**: `gffread`, `bedtools`, `pyranges`.

---

## 📏 BED — genomic intervals

Simpler than GFF. Minimum 3 columns: chromosome, start, end.

```
chr1  1000  5000  feature_A  100  +
chr1  6000  8000  feature_B  200  -
```

**Important**: BED uses 0-based coordinates and half-open intervals `[start, end)`. GFF / VCF use 1-based and closed intervals. **A common source of bugs.**

**Tools**: `bedtools`, `pybedtools`.

---

## 🧪 PDB — protein structure

**Protein Data Bank format**. Records each atom with its 3D coordinates.

```
ATOM      1  N   MET A   1      20.154  29.699   5.276  1.00 49.05  N
ATOM      2  CA  MET A   1      21.618  29.504   5.461  1.00 43.14  C
ATOM      3  C   MET A   1      22.219  28.683   4.331  1.00 39.31  C
```

**Note**: PDB has been superseded by **mmCIF** for new structures (PDB has fixed-width column limits that fail for huge complexes).

**Tools**: `Biopython.PDB`, PyMOL, ChimeraX, `BioPandas`.

---

## 💊 SDF / MOL — molecules

Stores 2D / 3D structures of small molecules with explicit atoms and bonds.

```
  Mrv2014 11302023062D

  9  9  0  0  0  0            999 V2000
    2.6661   -1.4438    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    ...
M  END
```

**Tools**: RDKit, OpenBabel.

---

## 💊 SMILES — linear notation

**Simplified Molecular Input Line Entry System**. Encodes a molecule as a single string.

```
Aspirin:    CC(=O)Oc1ccccc1C(=O)O
Caffeine:   CN1C=NC2=C1C(=O)N(C(=O)N2C)C
Ibuprofen:  CC(C)Cc1ccc(cc1)C(C)C(=O)O
```

**Advantages**: compact, easy to store in a database, indexable for substructure search.

**Tools**: RDKit, OpenBabel, all major chemistry databases.

---

## 🎯 Quick recommendations

| If you have... | Read with... |
|----------------|--------------|
| FASTA / FASTQ | Biopython, `seqkit` |
| SAM / BAM | `samtools`, `pysam` |
| VCF | `bcftools`, `cyvcf2`, `pyvcf3` |
| GFF / GTF | `pyranges`, `gffread` |
| BED | `bedtools`, `pybedtools` |
| PDB | `Biopython.PDB`, `BioPandas` |
| SDF / SMILES | RDKit |

---

## 💡 Critical detail about coordinates

| Format | Coord. base | Interval |
|--------|-------------|----------|
| BED | 0-based | half-open `[start, end)` |
| GFF / GTF | 1-based | closed `[start, end]` |
| VCF | 1-based | closed |
| SAM / BAM | 1-based | closed |

Always check this when converting between formats. Most off-by-one bugs in bioinformatics live here.
