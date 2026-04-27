# 🧪 Module 06: Protein Structure Analysis

## 🎯 Objectives

By the end of this module you will be able to:

1. Download structures from the PDB
2. Navigate the Biopython.PDB hierarchy (Structure → Model → Chain → Residue → Atom)
3. Compute distances and basic geometric properties
4. Identify ligands and active sites
5. Extract amino acid sequences from structures

---

## 📖 Brief theory

A protein's 3D structure determines its function. Knowing the structure lets you:

- **Design drugs**: structure-based drug design (SBDD) → e.g. HIV protease inhibitors
- **Understand mutations**: how does a SNV affect folding?
- **Predict interactions**: protein-protein, protein-ligand
- **Engineer enzymes**: rational design

### Key concepts

- **PDB / mmCIF**: standard formats. PDB is fixed-width text; mmCIF is the modern replacement.
- **Hierarchy**: `Structure → Model → Chain → Residue → Atom`. NMR structures often have multiple models; X-ray usually one.
- **Coordinates**: in Ångströms (1 Å = 0.1 nm). Typical CA-CA distance: ~3.8 Å for adjacent residues.
- **HETATM**: non-standard atoms (ligands, ions, modified residues).
- **B-factor**: thermal mobility; high values indicate flexible regions.

### Recent revolution: AlphaFold

AlphaFold2 (DeepMind, 2021) and AlphaFold3 (2024) predict structures with experiment-level accuracy. The **AlphaFold Database** offers >200M predicted structures: https://alphafold.ebi.ac.uk/

---

## 🛠️ Practical example

[`protein_analysis.ipynb`](./protein_analysis.ipynb) shows, with `1AKE` (adenylate kinase):

- Download from the PDB
- Parse and explore the hierarchy
- Compute CA-CA distances
- Extract amino acid sequence from structure
- Identify ligands (HETATM)
- Find active site (residues near a ligand)

---

## 💡 For your profile

- **Software engineer**: Biopython.PDB has a clean OO API. Hierarchy is a clear tree.
- **Pharmacist**: you already understand active sites, allosteric inhibition, and binding mode. The computational part is just to scale that knowledge.

---

## 📝 Suggested exercises

1. **Easy**: download `1HVR` (HIV protease) and report the basic stats.
2. **Medium**: write a function to compute the centroid of a chain.
3. **Medium**: find all disulfide bonds (Cys-Cys at < 2.2 Å between SG atoms).
4. **Medium**: compute the radius of gyration of the protein.
5. **Hard**: align two structures (e.g. 1AKE open vs 4AKE closed) using TM-align or `Bio.PDB.Superimposer`.
6. **Pharma-focused**: download CYP3A4 (`1TQN`), identify its heme active site, and compute distances to the docked ligand.
7. **AlphaFold**: download a predicted structure from the AlphaFold DB and compare to its X-ray counterpart.

---

## 📚 Additional resources

- [Biopython.PDB FAQ](https://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ)
- [PDB101](https://pdb101.rcsb.org/) — RCSB educational portal
- [AlphaFold DB](https://alphafold.ebi.ac.uk/) — millions of predicted structures
- [PyMOL](https://pymol.org/) — gold-standard visualization
- [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) — modern alternative
- [BioPandas](https://rasbt.github.io/biopandas/) — DataFrame-based PDB API
