# Cheminformatics Web App

## Overview

This project is a Streamlit-based cheminformatics web application built using Python and RDKit.

The application allows users to upload molecular datasets containing SMILES strings, calculate important molecular descriptors, visualize molecular structures, and download processed datasets.

---

## Features

* Upload CSV datasets containing SMILES
* Process all molecules in the dataset
* Calculate molecular descriptors:

  * Molecular Weight (MW)
  * LogP
  * TPSA
  * Hydrogen Bond Donors (HBD)
  * Hydrogen Bond Acceptors (HBA)
* Validate uploaded datasets
* Count valid and invalid molecules
* Display dataset statistics
* Display dataset summary metrics
* Visualize molecular structures
* Download processed datasets

---

## Technologies Used

* Python
* Streamlit
* RDKit
* Pandas

---

## Workflow

1. Upload CSV file
2. Validate SMILES column
3. Generate molecular descriptors
4. Calculate dataset statistics
5. Visualize selected molecules
6. Download processed dataset

---

## Example Input

CSV file with a column named:

SMILES

Example:

CCO

CCN

c1ccccc1

---

## Output

The application generates a processed dataset containing:

* Molecular Weight
* LogP
* TPSA
* HBD
* HBA

and allows export as a CSV file.

---

## Author

Sriya

Computational Chemistry | Cheminformatics | AI for Drug Discovery
# Cheminformatics-Web-App
Cheminformatics-Web-App
