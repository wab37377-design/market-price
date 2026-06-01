import streamlit as st
import pandas as pd

st.title("🚀 AI Pricing Console")

file = st.file_uploader("Upload Excel or CSV", type=["xlsx", "csv"])

if file is not None:

    if file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)

    st.subheader("📊 Original Data")
    st.dataframe(df)

    # تلقائي يبحث عن أول عمود رقمي
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) < 1:
        st.error("❌ ما فيه أي عمود أرقام في الملف")
