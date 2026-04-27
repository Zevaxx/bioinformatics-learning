# 🤖 Module 05: ADMET Prediction with Machine Learning

## 🎯 Objectives

By the end of this module you will be able to:

1. Understand what ADMET means and why it is critical in drug discovery
2. Generate features from molecules (descriptors + fingerprints)
3. Train ML models (Random Forest, XGBoost) for ADMET prediction
4. Evaluate models with appropriate metrics
5. Interpret feature importances

---

## 📖 Brief theory

### What is ADMET?

| Letter | Meaning | Why it matters |
|--------|---------|----------------|
| **A** | Absorption | If a drug isn't absorbed, it doesn't work orally |
| **D** | Distribution | Reach the target tissue (e.g. cross BBB?) |
| **M** | Metabolism | CYP polymorphisms → variable response |
| **E** | Excretion | Half-life, dosage interval |
| **T** | Toxicity | Hepatic, cardiac (hERG), genotoxicity |

**Key fact**: ~40% of drugs in development fail in clinical trials due to poor ADMET. Predicting these properties **early** (in silico) saves millions of dollars and years of work.

### Why ML for ADMET?

- **Lots of data**: ChEMBL, PubChem and DrugBank have millions of measurements
- **Useful structure**: SMILES → descriptors → feature vector
- **Complex relationships**: non-linear, many subtle interactions → fits ML well
- **Mature tools**: RDKit + scikit-learn solve 80% of cases

### Typical ML pipeline

```
SMILES
   ↓ RDKit
Mol objects
   ↓ Descriptors + Morgan FP
Feature matrix X
   ↓ Train/test split
Model (RF / GBM / NN)
   ↓ Cross-validation
Trained model
   ↓
Predictions on new molecules
```

---

## 🛠️ Practical example

[`admet_predictor.ipynb`](./admet_predictor.ipynb) builds a **logS (aqueous solubility)** predictor:

- Embedded ESOL-style dataset
- Classical descriptors + Morgan fingerprints
- Random Forest training
- R² and RMSE evaluation
- Feature importance analysis

---

## 💡 For your profile

- **Software engineer**: scikit-learn is OO and Pythonic — you'll feel at home. The hard part is the science, not the code.
- **Pharmacist**: your knowledge of pharmacokinetics gives you sanity-check on predictions. Does the model say "high BBB permeability" for a polar molecule with MW 800? Something is off.

---

## 📝 Suggested exercises

1. **Easy**: try the trained model with new molecules.
2. **Medium**: compare different models (RF, GBM, SVR, kNN) using cross-validation.
3. **Medium**: use only descriptors (no fingerprints) — does performance drop?
4. **Hard**: build a hERG inhibition classifier (toxicity) using public data.
5. **Hard**: try a Graph Neural Network (PyTorch Geometric or DeepChem) and compare.
6. **Pharma-focused**: predict ADMET properties for a series of chemical analogs you design yourself, varying one functional group at a time.

---

## ⚠️ Real-world considerations

This module shows the **basic mechanics**. In a real project:

- **Much more data** (thousands, not 30 molecules)
- **Time / scaffold splits** to avoid leakage between train and test
- **Applicability domain**: knowing which predictions are trustworthy
- **Robust uncertainty estimation** (e.g. quantile regression, conformal prediction)
- **Active learning**: choose which molecules to test experimentally to improve the model

---

## 📚 Additional resources

- [MoleculeNet](https://moleculenet.org/) — standard ADMET benchmarks
- [ADMETlab 2.0](https://admetmesh.scbdd.com/) — pre-trained free web service
- [DeepChem](https://deepchem.io/) — drug discovery DL framework
- [Practical Cheminformatics (blog)](https://practicalcheminformatics.blogspot.com/) — Pat Walters
- [Therapeutics Data Commons](https://tdcommons.ai/) — large-scale benchmarks
- [Delaney 2004 (ESOL)](https://pubs.acs.org/doi/10.1021/ci034243x) — classical solubility paper
