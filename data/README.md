# 📦 Datasets — How to download example data

This folder is meant to hold the data files used by the modules. **It is not in version control** (see the project `.gitignore`) because bioinformatics datasets are usually too large for Git.

This file explains how to download public datasets useful for each module.

---

## 🧬 Module 01: Sequence analysis

### Reference sequences from NCBI

```bash
# Download human CYP2D6 (FASTA)
mkdir -p data/sequences
curl -o data/sequences/cyp2d6.fa "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NM_000106&rettype=fasta&retmode=text"

# Or with Biopython (see notebook in module 01)
```

### Reference genomes (small examples)

```bash
# E. coli K-12 (~4.6 Mb, ideal for tests)
mkdir -p data/genomes
curl -o data/genomes/ecoli.fa.gz "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz"
gunzip data/genomes/ecoli.fa.gz
```

---

## 🎯 Module 02: NGS pipeline

### Public test reads (small)

```bash
# 1000 Genomes Project — small chr22 sample
mkdir -p data/reads
curl -o data/reads/sample_R1.fastq.gz "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/HG00096/sequence_read/SRR062634_1.filt.fastq.gz"
curl -o data/reads/sample_R2.fastq.gz "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/HG00096/sequence_read/SRR062634_2.filt.fastq.gz"
```

### Synthetic data (faster for testing)

```bash
# Generate synthetic reads with wgsim (samtools)
# wgsim ecoli.fa reads_R1.fq reads_R2.fq -N 100000
```

---

## 🧬 Module 03: Variant analysis

### 1000 Genomes VCF

```bash
mkdir -p data/variants
# Variants on chr22 (~700 MB compressed)
curl -o data/variants/chr22.vcf.gz "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"
```

### ClinVar (clinical variants)

```bash
# Full ClinVar VCF (~70 MB)
curl -o data/variants/clinvar.vcf.gz "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz"
```

### PharmGKB (pharmacogenomics) ⭐

```bash
# Free, requires registration
# https://www.pharmgkb.org/downloads
# Download: clinical_variants.tsv, drugLabels.tsv
```

---

## 💊 Modules 04 & 05: Cheminformatics & ADMET

### ChEMBL (downloadable SQLite!)

```bash
mkdir -p data/chembl
# Latest ChEMBL release as SQLite (~6 GB)
curl -o data/chembl/chembl_33_sqlite.tar.gz "https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_33_sqlite.tar.gz"
tar -xzf data/chembl/chembl_33_sqlite.tar.gz -C data/chembl/

# Now you can query with SQL:
# sqlite3 data/chembl/chembl_33/chembl_33_sqlite/chembl_33.db
```

### ESOL (solubility)

```bash
# Delaney 2004 dataset (~1144 molecules)
mkdir -p data/admet
curl -o data/admet/esol.csv "https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/delaney-processed.csv"
```

### MoleculeNet

Browse https://moleculenet.org/datasets-1 for benchmarks: BBBP, Tox21, HIV, ToxCast, etc.

---

## 🧪 Module 06: Protein structure

### PDB

Best fetched programmatically with Biopython (see notebook). Manually:

```bash
mkdir -p data/pdb
# Specific structure
curl -o data/pdb/1ake.pdb "https://files.rcsb.org/download/1AKE.pdb"

# CYP3A4 (relevant for pharmacogenomics)
curl -o data/pdb/1tqn.pdb "https://files.rcsb.org/download/1TQN.pdb"
```

### AlphaFold DB

```bash
# Predicted structure of any human protein
# Format: AF-{UniProtID}-F1-model_v4.pdb
mkdir -p data/alphafold
curl -o data/alphafold/cyp2d6.pdb "https://alphafold.ebi.ac.uk/files/AF-P10635-F1-model_v4.pdb"
```

---

## 🧬 Module 07: RNA-seq

### GEO (count matrices)

```bash
mkdir -p data/rnaseq
# Example: GSE52778 — airway smooth muscle RNA-seq
curl -o data/rnaseq/GSE52778_counts.txt "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE52nnn/GSE52778/suppl/GSE52778_All_Sample_FPKM_Matrix.txt.gz"
```

### Synthetic data with airway

```r
# In R
BiocManager::install("airway")
library(airway)
data(airway)
# Pre-existing dataset, ideal for practice
```

---

## 📊 Quick reference — public data sources

| Source | Type | URL |
|--------|------|-----|
| NCBI | Sequences, variants | https://www.ncbi.nlm.nih.gov/ |
| Ensembl | Genomes, annotation | https://www.ensembl.org/ |
| 1000 Genomes | Variants, reads | https://www.internationalgenome.org/ |
| GEO | Expression | https://www.ncbi.nlm.nih.gov/geo/ |
| TCGA | Cancer genomics | https://portal.gdc.cancer.gov/ |
| ChEMBL | Bioactivity | https://www.ebi.ac.uk/chembl/ |
| PubChem | Chemicals | https://pubchem.ncbi.nlm.nih.gov/ |
| PDB | Structures | https://www.rcsb.org/ |
| AlphaFold DB | Predicted structures | https://alphafold.ebi.ac.uk/ |
| PharmGKB | Pharmacogenomics | https://www.pharmgkb.org/ |
| MoleculeNet | ADMET benchmarks | https://moleculenet.org/ |

---

## ⚠️ Important notes

1. **DO NOT commit large data files to Git**. Use `.gitignore` (already configured).
2. **Cite the original sources** when using public data.
3. Check **license / terms of use** of each source.
4. Datasets like ChEMBL or PharmGKB may require **academic registration**.
5. For very large data (TBs), consider **cloud storage** (AWS S3, Google Cloud Storage).
