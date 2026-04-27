# 🧬 Module 07: Differential Expression — Conceptual Guide

This document complements [`README.md`](./README.md) with concrete pseudo-code and a step-by-step explanation of differential expression with DESeq2.

> **Note**: this module is intentionally documentation-heavy. Real analyses are run in R/Bioconductor. The goal here is for you to understand **what** is happening before you write the code.

---

## 📊 Step 1: data input

### Structure of a count matrix

```
              sample1  sample2  sample3  sample4  sample5  sample6
GENE0001        1245     1102     1320      245      189      201
GENE0002          12       15        8        3        5        2
GENE0003           0        0        0     1052     1130      980
GENE0004         521      498      550      490      512      535
...
```

- Rows: genes (Ensembl IDs are typical: `ENSG00000139618`)
- Columns: samples
- Values: integer counts (number of reads mapping to the gene)

### Sample metadata

```
sample      condition    batch
sample1     control      A
sample2     control      A
sample3     control      B
sample4     treated      A
sample5     treated      B
sample6     treated      B
```

---

## 🧪 Step 2: filter low-count genes

Genes with very few reads add noise and statistical overhead. Common filter:

```r
# Keep genes with at least 10 counts total across samples
keep <- rowSums(counts(dds)) >= 10
dds  <- dds[keep, ]
```

---

## 📐 Step 3: normalization

Samples don't have identical sequencing depth. DESeq2 uses **size factors**:

```
size_factor_i = median over genes of (count_ij / geometric_mean_j)
```

This cancels out total-depth differences without distorting biological signal.

---

## 🧠 Step 4: dispersion estimation

The variance of count data is **not Poisson** — it has overdispersion. DESeq2 fits a negative binomial model:

```
count ~ NegativeBinomial(mean = mu, dispersion = alpha)
```

DESeq2 estimates dispersion in three steps:
1. Per-gene dispersion (noisy when n is small)
2. Mean-dispersion trend
3. Empirical Bayes shrinkage toward the trend (the "DESeq2 trick")

---

## 🎯 Step 5: hypothesis testing

For each gene, DESeq2 performs a Wald test:

```
H0: log2FC = 0  (no change)
H1: log2FC ≠ 0  (change exists)
```

Output for each gene:
- `baseMean`: average expression across samples
- `log2FoldChange`: estimated effect (treated vs. control)
- `lfcSE`: standard error of log2FC
- `stat`: Wald statistic
- `pvalue`: raw p-value
- **`padj`**: BH-adjusted p-value ← use this

---

## 🚦 Step 6: filter significant genes

Standard criteria:

```r
significant <- res[
    !is.na(res$padj) &
    res$padj < 0.05 &
    abs(res$log2FoldChange) > 1,  # at least 2x change
]
```

- `padj < 0.05`: 5% false discovery rate
- `|log2FC| > 1`: biologically meaningful change

---

## 📈 Step 7: visualization

### Volcano plot

X-axis: log2FC. Y-axis: -log10(padj). Significant genes are in the upper corners.

```r
library(EnhancedVolcano)
EnhancedVolcano(res,
    lab = rownames(res),
    x = 'log2FoldChange',
    y = 'padj',
    pCutoff = 0.05,
    FCcutoff = 1
)
```

### MA plot

X-axis: average expression. Y-axis: log2FC. Useful to detect biases.

```r
plotMA(res, ylim = c(-5, 5))
```

### Heatmap

Top significant genes' expression across samples.

```r
library(pheatmap)
top_genes <- head(order(res$padj), 50)
pheatmap(assay(rlog(dds))[top_genes, ],
         cluster_rows = TRUE,
         show_rownames = TRUE,
         cluster_cols = TRUE,
         scale = "row")
```

---

## 🔬 Step 8: functional enrichment

Once you have a list of significant genes, you usually ask: **which pathways or functions are enriched?**

```r
library(clusterProfiler)
library(org.Hs.eg.db)

# Convert ENSEMBL → ENTREZ
gene_ids <- bitr(rownames(significant),
                  fromType = "ENSEMBL",
                  toType   = "ENTREZID",
                  OrgDb    = org.Hs.eg.db)

# GO enrichment (Biological Process)
go_enrich <- enrichGO(
    gene = gene_ids$ENTREZID,
    OrgDb = org.Hs.eg.db,
    ont = "BP",
    pAdjustMethod = "BH",
    pvalueCutoff = 0.05
)

dotplot(go_enrich, showCategory = 20)
```

---

## 🐍 Equivalent in Python (pyDESeq2)

```python
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds  import DeseqStats
import pandas as pd

# Load data
counts   = pd.read_csv("counts.csv", index_col=0).T
metadata = pd.read_csv("metadata.csv", index_col=0)

# Filter low-count genes
counts = counts.loc[:, counts.sum() >= 10]

# Build DESeq2 object
dds = DeseqDataSet(
    counts=counts,
    metadata=metadata,
    design_factors="condition"
)
dds.deseq2()

# Wald test
stats = DeseqStats(dds, contrast=["condition", "treated", "control"])
stats.summary()

# DataFrame with results
results_df = stats.results_df
significant = results_df[
    (results_df["padj"] < 0.05) &
    (results_df["log2FoldChange"].abs() > 1)
]
print(f"Significant genes: {len(significant)}")
```

---

## ⚠️ Common pitfalls

1. **Use raw counts, not normalized values**: DESeq2 normalizes internally.
2. **Don't use a single replicate per condition**: minimum 3, ideally 5+.
3. **Watch out for batch effects**: include them in the design (`~ batch + condition`).
4. **Don't filter by mean > X before DESeq2**: it bypasses its statistical model.
5. **Remember multiple testing correction**: always use `padj`, never raw `pvalue`.

---

## 🎯 When R is unavoidable

Modules where you'll likely need R:

- **Differential expression**: DESeq2, edgeR, limma
- **Functional enrichment**: clusterProfiler
- **Single-cell**: Seurat (Scanpy in Python is a good alternative)
- **Survival analysis**: `survival` package
- **Genome browser tracks**: `Gviz`, `ggbio`

For everything else, Python with Biopython, pandas, scikit-learn and RDKit covers ~90% of cases.

---

## 📚 Recommended reading

- [DESeq2 paper (Love et al. 2014)](https://doi.org/10.1186/s13059-014-0550-8)
- [DESeq2 vignette](https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html)
- [Statistical Models in Bioinformatics](https://www.bioconductor.org/help/course-materials/) — Bioconductor courses
