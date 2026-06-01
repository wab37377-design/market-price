import streamlit as st
import pandas as pd

st.title("AI Pricing Console")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:
    df = pd.read_excel(file)

    price_cols = df.select_dtypes(include="number").columns

    if len(price_cols) == 0:
        st.write("No price columns found")
    else:
        df["Min Price"] = df[price_cols].min(axis=1)
        df["Best Source"] = df[price_cols].idxmin(axis=1)

        st.dataframe(df)
