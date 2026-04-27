# 🌊 Workflow Managers in Bioinformatics

Bioinformatics analyses often involve dozens of steps with complex dependencies. **Workflow managers** orchestrate these pipelines, providing reproducibility, parallelism, and resource management.

---

## Why use a workflow manager?

| Without a manager | With a manager |
|-------------------|---------------|
| Fragile bash scripts | Declarative pipelines |
| Reruns everything if one step fails | Resumes from the failed step |
| Hard to parallelize | Auto-parallelization (samples, chunks) |
| Hard to reproduce on another machine | Reproducible (containers, configs) |
| Complex resource management | Built-in cluster / cloud support |

---

## 🐍 Snakemake (Python-based)

- **URL**: https://snakemake.readthedocs.io/
- **Language**: Python + DSL
- **Strengths**: Pythonic, file-driven (declares input/output files), easy to learn
- **Best for**: research projects, teams that already use Python

```python
# Snakefile example
rule all:
    input: "results/aligned.bam.bai"

rule align:
    input:
        ref = "data/reference.fa",
        r1  = "data/reads_R1.fq.gz",
        r2  = "data/reads_R2.fq.gz"
    output: "results/aligned.bam"
    threads: 8
    shell:
        "bwa mem -t {threads} {input.ref} {input.r1} {input.r2} | "
        "samtools sort -@ {threads} -o {output} -"

rule index:
    input:  "results/aligned.bam"
    output: "results/aligned.bam.bai"
    shell:  "samtools index {input}"
```

---

## ⚡ Nextflow (Groovy / JVM) ⭐

- **URL**: https://www.nextflow.io/
- **Language**: Groovy DSL on the JVM
- **Strengths**: scalable (HPC, cloud, K8s), large community (nf-core), excellent for production
- **Best for**: production pipelines, multi-environment scaling

> 💡 **For Kotlin developers**: Nextflow runs on the JVM and uses Groovy — closures, dynamic types, and lambdas will feel natural to you.

```groovy
nextflow.enable.dsl=2

process FASTQC {
    input:
    tuple val(sample_id), path(reads)

    output:
    path "*_fastqc.html"

    script:
    """
    fastqc ${reads}
    """
}

process ALIGN {
    input:
    tuple val(sample_id), path(reads)
    path reference

    output:
    tuple val(sample_id), path("${sample_id}.bam")

    script:
    """
    bwa mem -t 4 ${reference} ${reads} | samtools sort -o ${sample_id}.bam -
    """
}

workflow {
    Channel.fromFilePairs('data/*_{R1,R2}.fq.gz')
        | (FASTQC & ALIGN.using(reference: file('data/reference.fa')))
}
```

### nf-core
[nf-core](https://nf-co.re/) is a community-curated catalog of production-ready Nextflow pipelines: `rnaseq`, `sarek` (variants), `chipseq`, etc. Highly recommended for real projects.

---

## 📜 WDL / Cromwell

- **URL**: https://openwdl.org/ , https://cromwell.readthedocs.io/
- **Language**: WDL (Workflow Description Language) — declarative
- **Engine**: Cromwell (JVM, by the Broad Institute)
- **Strengths**: standard at the Broad (GATK), runs natively on Google Cloud and HPC
- **Best for**: GATK-heavy pipelines, clinical environments

```wdl
version 1.0

workflow AlignReads {
    input {
        File reference
        File reads_r1
        File reads_r2
    }

    call BwaMem {
        input:
            reference = reference,
            reads_r1 = reads_r1,
            reads_r2 = reads_r2
    }

    output {
        File bam = BwaMem.bam
    }
}

task BwaMem {
    input {
        File reference
        File reads_r1
        File reads_r2
    }
    command {
        bwa mem ${reference} ${reads_r1} ${reads_r2} | samtools sort -o aligned.bam -
    }
    output {
        File bam = "aligned.bam"
    }
    runtime {
        docker: "biocontainers/bwa:latest"
    }
}
```

---

## 🌌 Galaxy (web-based)

- **URL**: https://galaxyproject.org/
- **Format**: graphical web interface
- **Strengths**: no-code, ideal for biologists without programming experience
- **Best for**: training, small labs, exploratory analysis
- **Limit**: less flexible than code-based managers

---

## 🐳 Containers and reproducibility

Workflow managers usually pair with container engines:

### Docker
- **URL**: https://www.docker.com/
- **Use**: package tools with all their dependencies
- **Bioinformatics images**:
  - [BioContainers](https://biocontainers.pro/) — community-curated containers
  - [Quay.io / biocontainers](https://quay.io/organization/biocontainers) — registry

### Singularity / Apptainer
- **URL**: https://apptainer.org/
- **Use**: containers in HPC (no root needed)
- **Standard** in academic clusters

### Bioconda
- **URL**: https://bioconda.github.io/
- **Use**: install bioinformatics tools via conda
- **Example**:
  ```bash
  conda install -c bioconda bwa samtools bcftools snakemake
  ```

---

## 🆚 Comparison: which one to choose?

| Criterion | Snakemake | Nextflow | WDL | Galaxy |
|-----------|-----------|----------|-----|--------|
| Curve | 🟢 Easy | 🟡 Medium | 🟡 Medium | 🟢 Trivial |
| Cloud / HPC | 🟡 OK | 🟢 Excellent | 🟢 Excellent | 🔴 Limited |
| Community | 🟢 Large | 🟢 Huge (nf-core) | 🟡 Medium | 🟡 Medium |
| Production | 🟡 OK | 🟢 Best | 🟢 Best | 🔴 No |
| Coding required | 🟢 Python | 🟡 Groovy | 🟡 WDL | 🔴 None |

---

## 🎯 Recommendation for this repository

In **Module 02** we use **Snakemake** because it is the easiest entry point. Once you are comfortable, try **Nextflow** — it will feel familiar coming from Kotlin/JVM and is the de facto standard in modern production environments.

---

## 📚 Additional resources

- [Snakemake Tutorial](https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html)
- [Nextflow Training](https://training.nextflow.io/) — official, free
- [nf-core](https://nf-co.re/) — production-ready Nextflow pipelines
- [Awesome Pipeline](https://github.com/pditommaso/awesome-pipeline) — curated list
