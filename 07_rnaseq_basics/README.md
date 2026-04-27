# 🧬 Module 07: RNA-seq Basics — Differential Expression

## 🎯 Objectives

By the end of this module you will be able to:

1. Understand the RNA-seq workflow end to end
2. Differentiate between count-based and pseudo-mapping approaches
3. Read a count matrix and conceptually run a DE analysis
4. Interpret typical DE results (log2 fold change, padj)
5. Know when R/Bioconductor is unavoidable

---

## 📖 Brief theory

### What is RNA-seq?

RNA-seq quantifies **gene expression** — i.e., how many times each gene is transcribed in a sample. Key uses:

- Compare conditions (e.g. tumor vs. normal)
- Identify drug response signatures
- Discover new transcripts and isoforms
- Single-cell: cell-type heterogeneity

### Typical workflow

```
RNA samples
    ↓ Library prep + sequencing
FASTQ reads
    ↓ FastQC + Trimmomatic
Cleaned reads
    ↓ STAR / HISAT2 (or Salmon/kallisto for pseudo-mapping)
Alignments / pseudo-counts
    ↓ featureCounts / HTSeq (if classical alignment)
Count matrix (genes × samples)
    ↓ DESeq2 / edgeR (R)
Differential expression
    ↓ clusterProfiler / GSEApy
Functional enrichment
```

### Two paradigms

#### 1. Classical alignment (STAR + featureCounts)
- Slower, uses more memory
- Allows isoform-level analysis, junctions, novel transcripts
- Output: BAM → counts

#### 2. Pseudo-mapping (Salmon, kallisto)
- Very fast (minutes per sample)
- Doesn't generate BAM, only quantifications
- Sufficient for most DE analyses

**Recommendation**: for routine DE, use **Salmon + tximport + DESeq2**. For novel discovery, use STAR.

---

## ⚠️ Why this module is conceptual (not Python-heavy)

The de facto standard tools for RNA-seq differential expression are in **R**:

- **DESeq2** (Love et al.) — most cited
- **edgeR** (Robinson et al.)
- **limma-voom** (Smyth et al.)

Python alternatives exist (pyDESeq2, diffxpy) but the R ecosystem is more mature and reviewers/journals expect it.

**This module gives you the conceptual base** so you understand what's happening before writing R code.

---

## 🛠️ Conceptual example with pseudo-code

```r
# Read counts
library(DESeq2)
counts <- read.csv("counts.csv", row.names=1)
coldata <- data.frame(
    condition = factor(c("control", "control", "control",
                          "treated", "treated", "treated"))
)

# Build DESeq2 object
dds <- DESeqDataSetFromMatrix(
    countData = counts,
    colData   = coldata,
    design    = ~ condition
)

# Filter low-count genes
dds <- dds[rowSums(counts(dds)) > 10, ]

# Run analysis
dds <- DESeq(dds)
res <- results(dds, contrast = c("condition", "treated", "control"))

# Significant genes
sig <- res[!is.na(res$padj) & res$padj < 0.05 & abs(res$log2FoldChange) > 1, ]
print(paste("Significant genes:", nrow(sig)))

# Volcano plot
library(EnhancedVolcano)
EnhancedVolcano(res,
    lab = rownames(res),
    x = 'log2FoldChange',
    y = 'padj'
)
```

### Equivalent in Python (with pyDESeq2)

```python
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds  import DeseqStats
import pandas as pd

counts = pd.read_csv("counts.csv", index_col=0).T
metadata = pd.DataFrame({
    "condition": ["control"]*3 + ["treated"]*3
}, index=counts.index)

dds = DeseqDataSet(counts=counts, metadata=metadata, design_factors="condition")
dds.deseq2()

stats = DeseqStats(dds, contrast=["condition", "treated", "control"])
stats.summary()
results_df = stats.results_df
```

---

## 💡 Key concepts to internalize

### log2 Fold Change (log2FC)

- log2FC = 1  → expression doubled
- log2FC = -1 → expression halved
- log2FC = 0  → no change

### padj (adjusted p-value)

P-value corrected for multiple testing (Benjamini-Hochberg). Use `padj < 0.05`, **not** raw p-value, because you're testing thousands of genes simultaneously.

### Normalization

You can't compare raw counts directly: samples have different sequencing depth. DESeq2 uses **size factors**, edgeR uses **TMM**, others use **CPM** or **TPM**.

---

## 📝 Suggested exercises

1. **Easy**: download a count matrix from GEO (e.g. `GSE52778`) and explore it in Python/pandas.
2. **Medium**: install R + Bioconductor + DESeq2 and run a basic analysis on public data.
3. **Medium**: try `pyDESeq2` and compare results with R.
4. **Hard**: do a complete pipeline: FASTQ → Salmon → tximport → DESeq2 with a public dataset.
5. **Pharma-focused**: download a drug treatment vs control dataset (`LINCS L1000`) and identify gene signatures.

---

## 📚 Essential resources

- [DESeq2 vignette](https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html) — official, comprehensive
- [RNA-seqlopedia](https://rnaseq.uoregon.edu/) — excellent free guide
- [Bioconductor RNA-seq workflow](https://bioconductor.org/packages/release/workflows/vignettes/rnaseqGene/inst/doc/rnaseqGene.html)
- [Salmon documentation](https://salmon.readthedocs.io/) — fast pseudo-mapping
- [pyDESeq2](https://pydeseq2.readthedocs.io/) — Python port (in development)
- [Coursera: Genomic Data Science](https://www.coursera.org/specializations/genomic-data-science) — Johns Hopkins course

---

## 🎯 Final recommendation

For your profile (software engineer + pharmacist), I recommend:

1. **Install R + RStudio + Bioconductor** (1 hour to get going)
2. **Learn the basic syntax** (R is statistically powerful but its syntax is quirky)
3. **Run an end-to-end DESeq2 analysis** on a public dataset
4. **Once you understand the pipeline**, you can stay in Python with pyDESeq2 if you prefer

R is ~the only language~ irreplaceable in modern bioinformatics. If you only learn one R skill, learn DESeq2.
