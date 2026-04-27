# 🗄️ Biological Databases

Modern bioinformatics rests on hundreds of public databases. Knowing **which one to query for what** saves enormous amounts of time.

> 💡 **Tip for SQL devs**: many of these databases are queryable via SQL, REST API, or downloadable SQL dumps. Take advantage of that.

---

## 🧬 Sequence databases

### NCBI (National Center for Biotechnology Information)
- **URL**: https://www.ncbi.nlm.nih.gov/
- **Contents**: GenBank (sequences), RefSeq (curated), PubMed (literature), Gene, Taxonomy
- **Access**: web, REST API (Entrez E-utilities), Biopython
- **Example**:
  ```python
  from Bio import Entrez, SeqIO
  Entrez.email = "you@example.com"  # required by NCBI
  with Entrez.efetch(db="nucleotide", id="NM_001301717",
                     rettype="fasta", retmode="text") as handle:
      record = SeqIO.read(handle, "fasta")
  print(record.id, len(record.seq))
  ```

### Ensembl
- **URL**: https://www.ensembl.org/
- **Contents**: vertebrate genomes (and other taxa via Ensembl Genomes), annotations, comparative genomics
- **Access**: web, REST API (https://rest.ensembl.org/), **public MySQL**, BioMart, Perl/Python APIs
- **SQL example**:
  ```bash
  mysql --user=anonymous --host=ensembldb.ensembl.org \
        --port=3306 --database=homo_sapiens_core_110_38
  ```

### UCSC Genome Browser
- **URL**: https://genome.ucsc.edu/
- **Contents**: genomes, tracks, annotations, multiple alignments
- **Access**: web, REST API, **public MySQL** (`genome-mysql.soe.ucsc.edu`), Table Browser
- **Tip**: `mysql --user=genome --host=genome-mysql.soe.ucsc.edu -A`

---

## 🧪 Protein databases

### UniProt
- **URL**: https://www.uniprot.org/
- **Contents**: protein sequences and rich functional annotation
- **Access**: web, REST API, SPARQL endpoint, downloadable XML/FASTA
- **Sub-databases**: SwissProt (manually curated) and TrEMBL (automatic)

### PDB (Protein Data Bank)
- **URL**: https://www.rcsb.org/
- **Contents**: 3D structures of proteins, nucleic acids and complexes
- **Access**: web, REST API, FTP, Biopython
- **Example**:
  ```python
  from Bio.PDB import PDBList
  pdbl = PDBList()
  pdbl.retrieve_pdb_file('1AKE', pdir='./pdb_files', file_format='pdb')
  ```

### InterPro
- **URL**: https://www.ebi.ac.uk/interpro/
- **Contents**: protein domains, families, functional sites (integrates Pfam, SMART, etc.)

---

## 🧬 Variant databases

### dbSNP
- **URL**: https://www.ncbi.nlm.nih.gov/snp/
- **Contents**: catalog of single nucleotide polymorphisms (SNPs) and small variants
- **Access**: NCBI Entrez, downloadable VCF

### ClinVar
- **URL**: https://www.ncbi.nlm.nih.gov/clinvar/
- **Contents**: variants with clinical interpretation (pathogenic / benign / VUS)
- **Access**: web, FTP, REST API
- **Useful for**: variant classification in pharmacogenomics and clinical genetics

### gnomAD
- **URL**: https://gnomad.broadinstitute.org/
- **Contents**: variant allele frequencies in large populations (>800k exomes/genomes)
- **Access**: web, GraphQL API, downloadable VCF, **available in BigQuery** ⭐
- **Example BigQuery**:
  ```sql
  SELECT chrom, pos, ref, alt, AF
  FROM `bigquery-public-data.gnomAD.v3_genomes__chr1`
  WHERE pos BETWEEN 1000000 AND 2000000
    AND AF > 0.01
  LIMIT 100;
  ```

---

## 💊 Drug databases (your edge!)

### DrugBank
- **URL**: https://go.drugbank.com/
- **Contents**: detailed drug information (mechanism, targets, interactions, pharmacokinetics)
- **Access**: web, downloadable XML/CSV (academic license)

### ChEMBL ⭐
- **URL**: https://www.ebi.ac.uk/chembl/
- **Contents**: 2M+ bioactive molecules with quantitative bioactivity data
- **Access**: web, REST API, **downloadable SQLite/PostgreSQL** ⭐
- **SQL example**:
  ```sql
  -- Drugs with reported activity against EGFR
  SELECT md.chembl_id, md.pref_name, act.standard_value, act.standard_units
  FROM molecule_dictionary md
  JOIN activities act ON md.molregno = act.molregno
  JOIN target_dictionary td ON act.tid = td.tid
  WHERE td.pref_name = 'Epidermal growth factor receptor erbB1'
    AND act.standard_type = 'IC50'
  ORDER BY act.standard_value ASC
  LIMIT 20;
  ```

### PubChem
- **URL**: https://pubchem.ncbi.nlm.nih.gov/
- **Contents**: 110M+ chemical compounds, bioassays
- **Access**: web, REST API (PUG REST), downloadable

### PharmGKB ⭐
- **URL**: https://www.pharmgkb.org/
- **Contents**: pharmacogenomic associations (variant ↔ drug ↔ phenotype) with clinical guidelines
- **Access**: web, downloadable TSV
- **Useful for**: Module 03 (variant analysis with pharmacogenomic focus)

---

## 🧫 Gene expression databases

### GEO (Gene Expression Omnibus)
- **URL**: https://www.ncbi.nlm.nih.gov/geo/
- **Contents**: expression experiments (microarray, RNA-seq, single-cell)
- **Access**: web, FTP, GEOquery (R)

### ArrayExpress
- **URL**: https://www.ebi.ac.uk/biostudies/arrayexpress
- **Contents**: similar to GEO, hosted at the EBI

### GTEx
- **URL**: https://gtexportal.org/
- **Contents**: gene expression across tissues in healthy donors
- **Access**: web, REST API, downloadable

---

## 🛤️ Pathway databases

### KEGG
- **URL**: https://www.kegg.jp/
- **Contents**: metabolic / signaling pathways, genome / drug interactions
- **Access**: web, REST API (free for academic use)

### Reactome
- **URL**: https://reactome.org/
- **Contents**: human pathways, fully curated and cross-referenced
- **Access**: web, REST API, Cypher (Neo4j)

---

## 🎯 Quick recommendations

| If you need... | Use... |
|----------------|--------|
| Reference DNA / protein sequences | NCBI / Ensembl / UniProt |
| Variants and allele frequencies | gnomAD + dbSNP |
| Clinical variant interpretation | ClinVar + PharmGKB |
| Drug-target data | ChEMBL + DrugBank |
| 3D structures | PDB |
| RNA-seq experiments | GEO + GTEx |
| Pathways | KEGG + Reactome |

---

## 🔑 Key idea

Most of these databases offer **REST APIs and SQL access**. For someone with your background, learning to query them is much faster than relearning data structures: write the right query and pull straight from the source.
