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

    df["Predicted Price"] = df[price_col] - (df[demand_col] * 0.5)

    def get_action(x):
        if x > 50:
            return "🔥 Attack"
        elif x > 20:
            return "⚖️ Match"
        else:
            return "💰 Profit"

    df["Decision"] = df[demand_col].apply(get_action)

    st.subheader("🧠 AI Results")
    st.dataframe(df[[sku_col, price_col, "Predicted Price", demand_col, "Decision"]])

else:
    st.info("⬆️ Upload your file to start")
