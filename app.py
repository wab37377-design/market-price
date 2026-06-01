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

    columns = df.columns.tolist()

    sku_col = st.selectbox("Product Column", columns)
    price_col = st.selectbox("Competitor Price", columns)
    demand_col = st.selectbox("Sales / Demand", columns)

    # تنظيف البيانات
    df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
    df[demand_col] = pd.to_numeric(df[demand_col], errors='coerce')

    df = df.dropna(subset=[price_col, demand_col])

    # حساب السعر المتوقع
