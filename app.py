import streamlit as st
import pandas as pd

st.title("AI Pricing Console")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:
    df = pd.read_excel(file)

    # الأعمدة المطلوبة (حسب ملفك)
    price_cols = ["EXTRA", "SWSG", "ALMANEA", "B BOX", "ALKHUNZAIN", "BH"]
    price_cols = [col for col in price_cols if col in df.columns]

