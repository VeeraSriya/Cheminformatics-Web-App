
import streamlit as st
import pandas as pd

from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw


def calculate_descriptors(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    return {
        "Molecular Weight": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol),
        "TPSA": Descriptors.TPSA(mol),
        "HBD": Descriptors.NumHDonors(mol),
        "HBA": Descriptors.NumHAcceptors(mol)
    }


st.title("Cheminformatics Web App")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    if "SMILES" not in df.columns:
        st.error("CSV must contain a column named SMILES")
        st.stop()

    results = []

    valid_count = 0
    invalid_count = 0

    for smiles in df["SMILES"]:

        desc = calculate_descriptors(smiles)

        if desc is not None:

            valid_count += 1
            results.append(desc)

        else:

            invalid_count += 1

            results.append({
                "Molecular Weight": None,
                "LogP": None,
                "TPSA": None,
                "HBD": None,
                "HBA": None
            })

    descriptor_df = pd.DataFrame(results)

    final_df = pd.concat(
        [df, descriptor_df],
        axis=1
    )

    st.subheader("Dataset Statistics")

    st.write(f"Total Molecules: {len(df)}")
    st.write(f"Valid Molecules: {valid_count}")
    st.write(f"Invalid Molecules: {invalid_count}")

    st.subheader("Dataset Summary")

st.write(
    f"Average Molecular Weight: {final_df['Molecular Weight'].mean():.2f}"
)

st.write(
    f"Average LogP: {final_df['LogP'].mean():.2f}"
)

st.write(
    f"Average TPSA: {final_df['TPSA'].mean():.2f}"
)

st.subheader("Processed Dataset")

st.dataframe(final_df)

st.subheader("Molecular Structure Viewer")

selected_smiles = st.selectbox(
        "Select a Molecule",
        df["SMILES"]
    )

mol = Chem.MolFromSmiles(selected_smiles)

if mol is not None:

        img = Draw.MolToImage(mol)

        st.image(img)

csv = final_df.to_csv(
        index=False
    ).encode("utf-8")

st.download_button(
        label="Download Processed Dataset",
        data=csv,
        file_name="processed_molecules.csv",
        mime="text/csv"
    )
