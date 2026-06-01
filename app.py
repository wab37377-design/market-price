import streamlit as st
import pandas as pd

st.title("AI Pricing Console")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file is not None:
    df = pd.read_excel(file)

    # الأعمدة اللي عندك (كما في ملفك)
    price_cols = ["EXTRA", "SWSG", "ALMANEA", "B BOX", "ALKHUNZAIN", "BH"]
    price_cols = [c for c in price_cols if c in df.columns]

    if price_cols:
        df["Min Price"] = df[price_cols].min(axis=1)
        df["Best Source"] = df[price_cols].idxmin(axis=1)

        st.write("✅ Done")
        st.dataframe(df)
    else:
        st.write("❌ No competitor columns detected")
