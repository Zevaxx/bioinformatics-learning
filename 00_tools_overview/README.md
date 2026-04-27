# 🗺️ Module 00: Bioinformatics Tools Overview

> **⭐ START HERE** — This module is the entry point to the repository.

---

## What is bioinformatics?

**Bioinformatics** is the discipline that applies computational and statistical methods to analyze and interpret biological data. In practice this means:

- Analyzing DNA / RNA / protein sequences at scale
- Identifying genetic variants and their relation to disease
- Predicting the 3D structure of proteins
- Designing and optimizing molecules with desired pharmacological properties
- Building automated pipelines that process terabytes of genomic data

The field grew out of the data explosion produced by the Human Genome Project (completed in 2003) and has accelerated with next-generation sequencing (NGS).

---

## 🏗️ How this repository is organized

| Module | Content | What you will learn |
|--------|---------|---------------------|
| **00** (this) | Tools overview | General orientation, ecosystem map |
| **01** | Sequence analysis | Biopython, FASTA, BLAST |
| **02** | NGS pipeline | Snakemake, QC, alignment |
| **03** | Variant analysis | VCF, pharmacogenomics |
| **04** | Cheminformatics | SMILES, RDKit, descriptors |
| **05** | ADMET and ML | Property prediction with ML |
| **06** | Protein structure | PDB, Biopython.PDB |
| **07** | RNA-seq | Differential expression (conceptual guide) |

---

## 🚀 Advantages of coming from Kotlin + SQL + Pharmacy

Your background is not the typical bioinformatician's — and that is a **huge advantage**.

### Kotlin / JVM

- **Nextflow** (the most widely used workflow manager in modern bioinformatics) runs on the JVM, and its DSL2 is based on Groovy — a dynamic JVM language that will feel familiar coming from Kotlin. The closure syntax, functional collections, and dynamic typing are very similar.
- **GATK (Genome Analysis Toolkit)**, the reference tool for variant analysis, is written in Java. You can read its source code, understand its algorithms and extend it if needed.
- **Picard Tools**, for SAM/BAM manipulation, is also pure Java.
- Your experience in software architecture (patterns, testing, clean code) will let you write more maintainable bioinformatics pipelines than most.

### SQL

Many biological databases use SQL or SQL-like interfaces:

```sql
-- Example: query variants on the public Ensembl MySQL server
SELECT
    s.name AS snp_id,
    vf.seq_region_id,
    vf.seq_region_start,
    vf.seq_region_end,
    vf.allele_string
FROM variation_feature vf
JOIN variation s ON vf.variation_id = s.variation_id
WHERE vf.seq_region_start BETWEEN 1000000 AND 2000000
LIMIT 10;
```

- **Ensembl BioMart**: SQL interface over multiple genomes
- **UCSC Genome Browser**: public MySQL database (`mysql.genome.ucsc.edu`)
- **ChEMBL**: distributed as a downloadable SQLite database; ideal for drug queries
- **BigQuery (NIH)**: NIH public datasets available in Google BigQuery (standard SQL)
- **PharmGKB**: downloadable pharmacogenomics datasets

### Pharmacy

Your training is gold in these areas:

- **Pharmacogenomics**: understanding how *CYP2D6* variants affect codeine metabolism does not need to be explained to you — you already know it.
- **Drug discovery**: pharmacokinetics, pharmacodynamics, ligand-receptor concepts you learned in pharmacy school are exactly what computational cheminformatics tries to model.
- **ADMET**: absorption, distribution, metabolism, excretion, toxicity — your training gives you a critical eye that no purely-software person has when interpreting prediction results.
- **Drug interactions**: knowledge of CYP polymorphisms, transporters (SLCO, ABCB) and their clinical relevance gives you context that most bioinformaticians lack.

---

## 📂 Contents of this module

| File | Content |
|------|---------|
| [languages.md](./languages.md) | Python, R, Bash, Java/Kotlin, SQL, Nextflow — when to use each |
| [databases.md](./databases.md) | NCBI, Ensembl, UniProt, ChEMBL, PDB and more — descriptions and examples |
| [workflows.md](./workflows.md) | Nextflow, Snakemake, WDL, Galaxy, Docker |
| [file_formats.md](./file_formats.md) | FASTA, FASTQ, SAM/BAM, VCF, GFF, PDB, SMILES and more |
| [ecosystem_map.md](./ecosystem_map.md) | Table: task → recommended tool |

---

## 🎯 Module objectives

After finishing this module you should be able to:

1. Identify which tool to use for each type of bioinformatics analysis
2. Understand which databases exist and what each is for
3. Recognize the most common file formats and parse the main ones
4. Decide which areas of bioinformatics you want to explore further
5. Understand how your prior experience translates to the field

---

## 📚 Additional resources

- [Bioinformatics Data Skills](https://www.oreilly.com/library/view/bioinformatics-data-skills/9781449367480/) — Vince Buffalo
- [Bioinformatics Algorithms](https://www.bioinformaticsalgorithms.org/) — Pevzner & Compeau (interactive, free)
- [EMBL-EBI Training](https://www.ebi.ac.uk/training/) — free courses from the European EBI
- [Canadian Bioinformatics Workshops](https://bioinformatics.ca/workshops-all/) — downloadable materials
