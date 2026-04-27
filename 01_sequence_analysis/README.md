# 🧬 Module 01: Sequence Analysis with Biopython

## 🎯 Objectives

By the end of this module you will be able to:

1. Parse FASTA files with Biopython
2. Compute basic sequence properties (length, GC content, melting temperature)
3. Translate DNA into protein
4. Query NCBI databases programmatically with Entrez
5. Run a basic BLAST search and parse the results

---

## 📖 Brief theory

A **DNA sequence** is a string in the alphabet `{A, C, G, T}` (RNA uses `U` instead of `T`). Behind that simplicity sit decades of bioinformatics:

- **GC content**: percentage of G and C bases. Higher GC content correlates with higher thermal stability — relevant for PCR design and identifying coding regions.
- **Genetic code**: every 3 nucleotides (codon) translate to one amino acid. There are 64 codons and 20 amino acids (plus stop codons), so the code is degenerate.
- **Reading frame**: a DNA sequence has 6 possible reading frames (3 forward + 3 reverse complement). Identifying the right ORF (Open Reading Frame) is fundamental.
- **Homology search (BLAST)**: given a query sequence, BLAST finds similar regions in massive databases, suggesting evolutionary relationships and potential function.

---

## 🛠️ Practical example

See [`intro_biopython.ipynb`](./intro_biopython.ipynb). It walks through:

- Reading FASTA with `SeqIO`
- Computing GC content with `gc_fraction`
- Translating DNA → protein with `Seq.translate()`
- Querying NCBI with `Entrez.efetch`
- Inspecting BLAST results

---

## 💡 Why this matters for your profile

- **Software engineer**: Biopython has a clean OO API (`SeqRecord`, `Seq`, `SeqFeature`) that will feel comfortable. The challenge is conceptual, not technical.
- **Pharmacist**: identifying genes / proteins related to drug targets is the foundation for everything that follows in modules 03 (pharmacogenomics) and 04-05 (drug discovery).

---

## 📝 Suggested exercises

1. **Easy**: download a CYP2D6 sequence from NCBI and compute its GC content.
2. **Medium**: identify all 6 reading frames of a sequence and locate the longest ORF in each.
3. **Medium**: run a BLAST search of a fragment of human insulin against the `nr` database and parse the top 10 hits.
4. **Hard**: build a script that, given a list of gene IDs, downloads their sequences from NCBI and produces a multiple alignment with MAFFT (call it as an external command).
5. **Pharma-focused**: download the sequences of CYP2D6, CYP2C9 and CYP3A4. Compare their lengths, GC content and run a BLAST among them. Are they evolutionarily related?

---

## 📚 Additional resources

- [Biopython Tutorial and Cookbook](http://biopython.org/DIST/docs/tutorial/Tutorial.html) — official, complete
- [NCBI E-utilities Help](https://www.ncbi.nlm.nih.gov/books/NBK25497/) — to use Entrez properly
- [BLAST Help](https://blast.ncbi.nlm.nih.gov/doc/blast-help/)
- [Rosalind](https://rosalind.info/problems/list-view/) — exercises that pair perfectly with this module
