import streamlit as st
import pandas as pd

st.title("🚀 AI Pricing Console")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file is not None:
    df = pd.read_excel(file)

    st.subheader("📊 Original Data")
    st.dataframe(df)

    # نأخذ أعمدة الأسعار من اليمين تلقائي (إذا كانت أرقام)
    price_cols = df.select_dtypes(include="number").columns.tolist()

    if len(price_cols) == 0:
        st.error("❌ ما فيه أعمدة أسعار رقمية في الملف")
    else:
        # نحسب أقل سعر لكل صف
        df["Min Price"] = df[price_cols].min(axis=1)

        # نحدد أرخص منافس
        df["Best Competitor"] = df[price_cols].idxmin(axis=1)

        # قرار بسيط
        df["Decision"] = "🔥 Attack"

        st.subheader("✅ Results")
        st.dataframe(df)

else:
    st.info("⬆️ Upload your Excel file")
``
