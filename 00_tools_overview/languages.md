# 💻 Languages used in Bioinformatics

Each language has a clear niche. You don't need to master all of them — you need to know **which one to use for what**.

| Language | Main role | Key libraries / tools | Recommended when |
|----------|-----------|------------------------|------------------|
| **Python** ⭐ | Dominant general-purpose | Biopython, pandas, scikit-learn, RDKit, PyTorch | Almost any task: scripts, ML, parsing, pipelines |
| **R** | Statistics & genomics | Bioconductor, DESeq2, edgeR, limma, Seurat | Differential expression, complex statistics, single-cell |
| **Bash** | Glue & CLI tools | samtools, bcftools, bwa, GATK CLI | Pipelines, file manipulation, running CLI tools |
| **Java / Kotlin** | Enterprise tools | GATK, Picard, IGV | Reading/extending GATK, custom JVM tools |
| **SQL** | Biological databases | MySQL, SQLite, BigQuery | Querying Ensembl, UCSC, ChEMBL, NIH datasets |
| **Groovy / Nextflow DSL** | Workflow management | Nextflow DSL2 | Reproducible, scalable production pipelines |
| **C / C++** | High performance | bwa, samtools, BLAST internals | Optimizing critical algorithms (advanced) |
| **Rust** | Modern high performance | rust-bio, noodles | Modern tools that prioritize safety + speed |

---

## 🐍 Python — the dominant language

**Why it dominates**: huge ecosystem, gentle learning curve, glue between data + ML + bio.

```python
# Read a FASTA file and compute GC content
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

for record in SeqIO.parse("sequence.fasta", "fasta"):
    print(f"{record.id}: GC = {gc_fraction(record.seq):.2%}")
```

**Key libraries**:
- `Biopython` — sequences, structures, NCBI Entrez
- `pandas` / `numpy` — tabular data
- `scikit-learn` — classical machine learning
- `RDKit` — cheminformatics
- `pysam` — SAM / BAM / VCF
- `cyvcf2` / `pyvcf3` — VCF (variants)
- `Scanpy` / `anndata` — single-cell
- `PyTorch` / `TensorFlow` — deep learning

**Official documentation**:
- Biopython: https://biopython.org/
- RDKit: https://www.rdkit.org/docs/

---

## 📊 R — the language of statistics

**Why it matters**: Bioconductor (the R bio ecosystem) has the gold-standard tools for many statistical analyses.

```r
# Differential expression with DESeq2
library(DESeq2)
dds <- DESeqDataSetFromMatrix(countData = counts,
                              colData = coldata,
                              design = ~ condition)
dds <- DESeq(dds)
res <- results(dds)
summary(res)
```

**When R is more common than Python**:
- **Differential expression** (DESeq2, edgeR, limma) — the de facto standard
- **Single-cell** (Seurat) — competes with Scanpy
- **Microarrays** — heavy R legacy
- **GWAS** and statistical genetics

**Key libraries**:
- `DESeq2`, `edgeR`, `limma` — RNA-seq
- `Seurat` — single-cell
- `clusterProfiler` — functional enrichment
- `Bioconductor` — full ecosystem (https://bioconductor.org/)

---

## 🐚 Bash — the glue of pipelines

Most CLI bioinformatics tools (samtools, bwa, GATK, bcftools) live on the command line. Knowing Bash is essential.

```bash
# Typical alignment pipeline
bwa index reference.fa
bwa mem -t 8 reference.fa reads_R1.fq reads_R2.fq | \
    samtools sort -@ 8 -o aligned.bam -
samtools index aligned.bam

# Variant calling
bcftools mpileup -f reference.fa aligned.bam | \
    bcftools call -mv -Oz -o variants.vcf.gz
```

**Essential CLI tools**:
- `samtools` — manipulate SAM/BAM/CRAM
- `bcftools` — manipulate VCF/BCF
- `bwa`, `bowtie2`, `minimap2` — read alignment
- `bedtools` — interval operations
- `seqkit` — fast FASTA/FASTQ manipulation

---

## ☕ Java / Kotlin — your bridge

This is where your Kotlin background gives you a head start.

### GATK (Genome Analysis Toolkit)

GATK is the reference tool for variant calling. It is written in Java and uses Apache Spark for parallelism.

```bash
gatk HaplotypeCaller \
    -R reference.fa \
    -I aligned.bam \
    -O variants.vcf.gz
```

You can read the source: https://github.com/broadinstitute/gatk

### Picard Tools

```bash
picard MarkDuplicates \
    I=input.bam \
    O=marked.bam \
    M=metrics.txt
```

### Writing your own JVM tools

Nothing stops you from writing utilities in Kotlin that read SAM/BAM with `htsjdk` (the same library GATK uses):

```kotlin
import htsjdk.samtools.SamReaderFactory
import java.io.File

fun main() {
    val reader = SamReaderFactory.makeDefault().open(File("aligned.bam"))
    reader.use {
        for (record in it) {
            println("${record.readName}: ${record.referenceName}:${record.alignmentStart}")
        }
    }
}
```

---

## 🗄️ SQL — your other superpower

Many biological databases expose a SQL interface or are downloadable as relational dumps.

```sql
-- ChEMBL example: find all drugs that target a given protein
SELECT
    md.chembl_id    AS drug_id,
    md.pref_name    AS drug_name,
    cs.standard_value,
    cs.standard_units,
    cs.standard_type
FROM molecule_dictionary md
JOIN activities act      ON md.molregno = act.molregno
JOIN compound_structures cs ON md.molregno = cs.molregno
JOIN target_dictionary td ON act.tid = td.tid
WHERE td.pref_name LIKE '%CYP3A4%'
LIMIT 20;
```

**Where SQL helps you in bioinformatics**:
- **Ensembl BioMart** — SQL-like queries over genomes (https://www.ensembl.org/biomart)
- **UCSC** — public MySQL DB (`mysql --user=genome --host=genome-mysql.soe.ucsc.edu`)
- **ChEMBL** — downloadable SQLite (https://chembl.gitbook.io/chembl-interface-documentation/downloads)
- **BigQuery + NIH** — public datasets in BigQuery (https://cloud.google.com/life-sciences)

---

## 🌊 Groovy / Nextflow DSL

Nextflow uses a Groovy-based DSL that should feel very natural coming from Kotlin (closures, lambdas, optional types):

```groovy
nextflow.enable.dsl=2

process FASTQC {
    input:
    path reads

    output:
    path "*_fastqc.html"

    script:
    """
    fastqc ${reads}
    """
}

workflow {
    Channel.fromPath('data/*.fastq.gz') | FASTQC
}
```

Nextflow runs on the JVM, so you can use any Java/Kotlin library inside it.

---

## 🎯 Recommendation for your profile

1. **Start with Python + Biopython** — it is the universal entry point.
2. **Use Bash from day one** — even basic familiarity multiplies your productivity.
3. **Get to R when you reach Module 07** (RNA-seq) — only then is it strictly necessary.
4. **Use your SQL** in Module 03 (variants) and Module 04 (cheminformatics) — that is where it shines.
5. **Try Nextflow** in Module 02 if you want to feel at home with the JVM.
