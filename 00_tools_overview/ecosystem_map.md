# 🗺️ Ecosystem Map: Task → Tool

Quick reference of which tool to use for each common bioinformatics task.

---

## 🧬 Sequence analysis

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Read / write FASTA, FASTQ | Biopython | seqkit, pysam |
| Search homology | BLAST (NCBI) | DIAMOND (faster), MMseqs2 |
| Multiple sequence alignment | MAFFT | MUSCLE, Clustal Omega, T-Coffee |
| Pairwise alignment | EMBOSS needle/water | Biopython.pairwise2, parasail |
| Trim adapters | Trimmomatic | cutadapt, fastp |
| Quality control on reads | FastQC | MultiQC, fastp |

---

## 🎯 Read alignment

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Align short reads (DNA) | **BWA-MEM** | Bowtie2, minimap2 |
| Align RNA-seq reads | **STAR** | HISAT2, Salmon (quasi-mapping) |
| Align long reads (PacBio / Nanopore) | **minimap2** | NGMLR, BLASR |
| Sort / index BAM | samtools | Picard |
| Mark duplicates | Picard MarkDuplicates | samtools markdup |

---

## 🧬 Variant analysis

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Variant calling (germline) | **GATK HaplotypeCaller** | bcftools, DeepVariant |
| Variant calling (somatic) | GATK Mutect2 | Strelka2, VarScan2 |
| Variant calling (long reads) | DeepVariant | Clair3, PEPPER |
| Variant annotation | **VEP (Ensembl)** | SnpEff, ANNOVAR |
| Variant filtering | bcftools filter | GATK VariantFiltration |
| Frequency analysis | bcftools, vcftools | plink2 |
| GWAS | PLINK2 | SAIGE, REGENIE |

---

## 💊 Cheminformatics

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Manipulate molecules | **RDKit** | OpenBabel |
| Compute molecular descriptors | RDKit | Mordred (more descriptors) |
| Generate fingerprints | RDKit (Morgan / ECFP) | OpenBabel (FP2, FP4) |
| Molecular docking | **AutoDock Vina** | Smina, GOLD, Glide (commercial) |
| Virtual screening | RDKit + Vina | OpenEye (commercial) |
| QSAR / ADMET | **RDKit + scikit-learn** | DeepChem, Mordred |
| 2D / 3D visualization | RDKit | PyMOL, Avogadro |
| Conformer generation | RDKit (ETKDG) | OpenBabel |

---

## 🧪 Protein structure

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Structure prediction | **AlphaFold2 / 3** | ESMFold (faster), RoseTTAFold |
| Read PDB / mmCIF | Biopython.PDB | BioPandas, PyMOL |
| Visualization | PyMOL | ChimeraX, NGLview (web) |
| Molecular dynamics | GROMACS | AMBER, OpenMM |
| Protein-ligand docking | AutoDock Vina | Smina, Glide |
| Sequence-structure alignment | TM-align | DALI, FATCAT |

---

## 🧫 Transcriptomics

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Quantify expression (RNA-seq) | **Salmon** (fast) | STAR + featureCounts, kallisto |
| Differential expression | **DESeq2** (R) | edgeR, limma-voom |
| Functional enrichment (GSEA) | clusterProfiler (R) | GSEApy (Python) |
| Single-cell RNA-seq | **Scanpy** (Py) / **Seurat** (R) | — |
| Trajectories (single-cell) | scVelo, PAGA | Monocle3 |
| Cell type annotation | CellTypist, Azimuth | manual markers |

---

## 🧬 Epigenomics

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| ChIP-seq peak calling | MACS2 | HOMER, SICER |
| Bisulfite sequencing | Bismark | methylKit |
| ATAC-seq | MACS2 + Genrich | HMMRATAC |
| Hi-C | Juicer | HiC-Pro, cooler |

---

## 🦠 Microbiome / metagenomics

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Taxonomy (16S) | DADA2 | QIIME2, mothur |
| Metagenomics (shotgun) | Kraken2 | MetaPhlAn, Centrifuge |
| Genome assembly | SPAdes | Flye (long reads), Unicycler |
| Functional analysis | HUMAnN | PICRUSt2 |

---

## 🌊 Pipelines and workflows

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Reproducible workflow manager | **Nextflow** ⭐ | Snakemake, WDL/Cromwell |
| Curated production pipelines | nf-core | Galaxy Toolshed |
| Containerization | Docker / Singularity | Podman |
| Package management | Bioconda | Pip, Spack |

---

## 📊 Statistical analysis

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Multivariate analysis | scikit-learn (Py) | factoextra (R) |
| Survival analysis | lifelines (Py), survival (R) | — |
| Bayesian inference | PyMC, Stan | brms (R) |
| General linear models | statsmodels (Py), lme4 (R) | — |

---

## 🗄️ Databases and APIs

| Task | Recommended tool | Alternatives |
|------|------------------|--------------|
| Query NCBI | Biopython.Entrez | edirect (CLI) |
| Query Ensembl | REST API + requests | pyEnsembl, BioMart |
| Query UniProt | REST + requests | bioservices |
| Query ChEMBL | chembl_webresource_client | direct SQL on dump |
| Query PDB | Biopython.PDB | RCSB API |

---

## 🎯 If you only had to learn five tools

For your profile (software engineer + pharmacist), I would prioritize:

1. **Biopython** — universal entry point for any sequence task
2. **RDKit** — fundamental for cheminformatics / drug discovery
3. **scikit-learn** — applied ML (you already know Python)
4. **Snakemake or Nextflow** — for reproducible pipelines
5. **bcftools + GATK** — to handle variants (your pharmacogenomics edge)

With these five tools you can tackle 80% of bioinformatics problems. The other 20% you learn on the fly.
