# 💊 Module 04: Cheminformatics Fundamentals

## 🎯 Objectives

By the end of this module you will be able to:

1. Represent molecules with SMILES
2. Compute molecular descriptors (MW, LogP, TPSA...)
3. Apply Lipinski's Rule of Five for drug-likeness
4. Generate molecular fingerprints (Morgan / ECFP)
5. Compute similarity between molecules

---

## 📖 Brief theory

**Cheminformatics** applies computer science methods to chemistry. In drug discovery it is fundamental because:

- A typical pharma "library" has **millions** of molecules
- You can't synthesize and test everything → you need to **filter computationally first**
- Tools like RDKit let you go from a SMILES string to a usable feature vector for ML in minutes

### Key concepts

- **SMILES**: a textual representation of a molecule. Compact, easy to store in a database.
- **Descriptor**: numerical property of a molecule (MW, LogP, etc.). Hundreds exist.
- **Fingerprint**: binary vector encoding substructures. Used for similarity and ML.
- **Lipinski's Rule of Five**: classic drug-likeness filter (MW≤500, LogP≤5, HBD≤5, HBA≤10).

---

## 🛠️ Practical example

[`molecule_basics.ipynb`](./molecule_basics.ipynb) walks through, with common drugs (aspirin, caffeine, ibuprofen, paracetamol):

- Parse SMILES with RDKit
- Visualize 2D structures
- Compute descriptors and Lipinski rules
- Generate Morgan fingerprints
- Compute Tanimoto similarity

---

## 💡 For pharmacists

This is **your home turf**. You already understand:

- Why polarity (LogP) matters for absorption
- Why MW matters for blood-brain barrier permeability
- Why HBD/HBA matter for solubility
- The mechanism of why aspirin and naproxen are similar (both NSAIDs / COX inhibitors)

Cheminformatics simply gives you computational tools to scale that knowledge.

---

## 📝 Suggested exercises

1. **Easy**: pick 10 drugs you know and calculate their Lipinski violations.
2. **Medium**: write a function that, given a SMILES, says "drug-like" / "not drug-like".
3. **Medium**: cluster a list of 50 drugs by Tanimoto similarity and verify whether they group by therapeutic class.
4. **Hard**: download a fragment of ChEMBL and find all molecules similar (Tanimoto ≥ 0.7) to aspirin.
5. **Pharma-focused**: compare the descriptors of NSAIDs vs. SSRIs and identify the biggest differences.

---

## 📚 Additional resources

- [RDKit Documentation](https://www.rdkit.org/docs/)
- [RDKit Cookbook](https://www.rdkit.org/docs/Cookbook.html) — practical recipes
- [DrugBank](https://go.drugbank.com/) — drug database (free for academia)
- [ChEMBL](https://www.ebi.ac.uk/chembl/) — bioactivity database
- [Lipinski et al. 1997](https://doi.org/10.1016/S0169-409X(96)00423-1) — original paper of the rule of five
- [TeachOpenCADD](https://projects.volkamerlab.org/teachopencadd/) — excellent free tutorials
