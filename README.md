# 🧬 Bioinformatics Learning

A progressive bioinformatics learning repository tailored for someone with a background in **software engineering (Kotlin, SQL)** and **pharmacy**. The goal is to explore different areas of bioinformatics step by step and discover which one excites you the most.

---

## 👤 Who is this repo for?

This repository is designed for profiles that combine:

- **Software engineering** (experience with Kotlin, SQL, system design)
- **Pharmacy / health sciences** (knowledge of drugs, biochemistry, pharmacology)

If you come from this background, you have concrete advantages:

| Your experience | Application in bioinformatics |
|-----------------|-------------------------------|
| **Kotlin / JVM** | Nextflow runs on the JVM (Groovy DSL, similar to Kotlin); GATK is written in Java |
| **SQL** | Ensembl BioMart, UCSC Genome Browser, ChEMBL all use SQL; BigQuery hosts NIH public datasets |
| **Pharmacy** | Direct edge in pharmacogenomics, drug discovery, ADMET, drug-drug interactions |

---

## 🗺️ Recommended roadmap

```
00_tools_overview  →  01_sequence_analysis  →  02_ngs_pipeline
        ↓                                              ↓
07_rnaseq_basics   ←   03_variant_analysis   ←  (choose your path)
        ↓
04_cheminformatics  →  05_admet_ml  →  06_protein_structure
```

The recommended order is **00 → 07**, but after module 00 you can jump to whichever area interests you most.

---

## 📂 Modules

| # | Module | Description | Difficulty | Status |
|---|--------|-------------|------------|--------|
| 00 | [tools_overview](./00_tools_overview/README.md) | Panorama of tools, languages, databases and file formats | ⭐ Beginner | ✅ Ready |
| 01 | [sequence_analysis](./01_sequence_analysis/README.md) | Biopython: FASTA parsing, GC content, translation, BLAST | ⭐⭐ Beginner-Intermediate | ✅ Ready |
| 02 | [ngs_pipeline](./02_ngs_pipeline/README.md) | Minimal NGS pipeline with Snakemake (QC + alignment) | ⭐⭐⭐ Intermediate | ✅ Ready |
| 03 | [variant_analysis](./03_variant_analysis/README.md) | Variant analysis with a pharmacogenomics focus | ⭐⭐⭐ Intermediate | ✅ Ready |
| 04 | [cheminformatics](./04_cheminformatics/README.md) | SMILES, RDKit, molecular descriptors | ⭐⭐ Beginner-Intermediate | ✅ Ready |
| 05 | [admet_ml](./05_admet_ml/README.md) | ML for ADMET prediction with scikit-learn + RDKit | ⭐⭐⭐ Intermediate | ✅ Ready |
| 06 | [protein_structure](./06_protein_structure/README.md) | Protein structure analysis with Biopython | ⭐⭐⭐ Intermediate | ✅ Ready |
| 07 | [rnaseq_basics](./07_rnaseq_basics/README.md) | RNA-seq differential expression (conceptual guide) | ⭐⭐⭐ Intermediate | ✅ Ready |

---

## ⚙️ Environment setup

### Option 1: pip

```bash
pip install -r requirements.txt
```

### Option 2: conda (recommended for bioinformatics)

```bash
conda env create -f environment.yml
conda activate bioinfo-learning
```

### Launch Jupyter

```bash
jupyter notebook
# or
jupyter lab
```

---

## 📚 External resources

| Resource | Type | URL |
|----------|------|-----|
| Rosalind | Interactive exercises | https://rosalind.info |
| Coursera: Genomic Data Science | Course (Johns Hopkins) | https://www.coursera.org/specializations/genomic-data-science |
| edX: Data Analysis for Life Sciences | Course (Harvard) | https://www.edx.org/learn/data-analysis |
| Bioinformatics Data Skills | Book (Vince Buffalo) | https://www.oreilly.com/library/view/bioinformatics-data-skills/9781449367480/ |
| Deep Learning for the Life Sciences | Book (Ramsundar et al.) | https://www.oreilly.com/library/view/deep-learning-for/9781492039822/ |
| Biostars | Q&A community | https://www.biostars.org |
| Biopython Tutorial | Official documentation | https://biopython.org/DIST/docs/tutorial/Tutorial.html |
| RDKit Documentation | Official documentation | https://www.rdkit.org/docs/ |

---

## 📄 License

MIT — see [LICENSE](./LICENSE)
