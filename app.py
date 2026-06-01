import streamlit as st
import pandas as pd

st.title("🚀 AI Pricing Console")

file = st.file_uploader("Upload Excel or CSV", type=["xlsx","csv"])

if file:
    if file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)

    st.subheader("📊 Original Data")
    st.dataframe(df)

    columns = df.columns.tolist()

    sku = st.selectbox("Select Product Column", columns)
    price = st.selectbox("Select Competitor Price", columns)
    demand = st.selectbox("Select Demand/Sales", columns)

    df["Predicted Price"] = df[price] - (df[demand] * 0.5)

    def action(x):
        if x > 50:
            return "🔥 Attack"
        elif x > 20:
            return "⚖️ Match"
        else:
            return "💰 Profit"

    df["Decision"] = df[demand].apply(action)

    st.subheader("🧠 AI Results")
    st.dataframe(df[[sku, price, "Predicted Price", demand, "Decision"]])

else:
    st.info("⬆️ Upload your file to start")
``
