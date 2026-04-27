# 🧬 Module 02: NGS Pipeline with Snakemake

## 🎯 Objectives

By the end of this module you will be able to:

1. Understand the typical structure of a next-generation sequencing (NGS) pipeline
2. Write basic Snakemake rules
3. Run a minimal pipeline: QC + alignment + variant calling
4. Reproduce the analysis on different machines

---

## 📖 Brief theory

A typical NGS pipeline has these stages:

```
Raw reads (FASTQ)
    ↓ FastQC
Quality control
    ↓ Trimmomatic / cutadapt
Trimmed reads
    ↓ BWA-MEM
Alignments (SAM)
    ↓ samtools sort + index
Sorted BAM
    ↓ Picard MarkDuplicates
Deduplicated BAM
    ↓ GATK HaplotypeCaller / bcftools
Variants (VCF)
    ↓ VEP / SnpEff
Annotated variants
```

A **workflow manager** like Snakemake automates this and provides:

- **Reproducibility**: same inputs → same outputs
- **Resumability**: if one step fails, only what changed is re-run
- **Parallelism**: multiple samples in parallel automatically
- **Scalability**: laptop → HPC → cloud with little code change

---

## 🛠️ Practical example

[`Snakefile`](./Snakefile) implements a minimal pipeline that:

1. Runs FastQC on the raw reads
2. Aligns with BWA-MEM
3. Sorts and indexes the BAM file
4. Generates a quick `bcftools` variant report

> ⚠️ **Note**: this Snakefile is **demonstrative**. To actually run it you need:
> - Real FASTQ files in `data/`
> - A reference genome in `data/reference.fa`
> - The tools installed (`bwa`, `samtools`, `bcftools`, `fastqc`)
>
> Easiest install: `conda install -c bioconda bwa samtools bcftools fastqc snakemake`

---

## 💡 For Kotlin / SQL devs

- **Snakemake** uses Python — easy to learn from any language background.
- If you prefer the **JVM**, look at **Nextflow**: same purpose, Groovy DSL, all your Kotlin/JVM concepts apply directly.
- The model is similar to **Gradle**: declarative tasks with input/output dependencies.

---

## 📝 Suggested exercises

1. **Easy**: run the Snakefile in dry-run mode (`snakemake -n`) and inspect the planned DAG.
2. **Medium**: extend the pipeline to add `Trimmomatic` or `cutadapt` after FastQC.
3. **Medium**: add a MarkDuplicates step with Picard.
4. **Hard**: parallelize for multiple samples using a `samples.tsv` config file.
5. **Production**: rewrite the pipeline in Nextflow DSL2.

---

## 📚 Additional resources

- [Snakemake Documentation](https://snakemake.readthedocs.io/)
- [Snakemake Tutorial](https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html) — official, hands-on
- [GATK Best Practices](https://gatk.broadinstitute.org/hc/en-us/sections/360007226651) — reference standard
- [nf-core/sarek](https://nf-co.re/sarek) — production-grade NGS pipeline (Nextflow)
