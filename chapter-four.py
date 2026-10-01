import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload Your csv file", type= ["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    tea_type = df["Tea_Type"].unique()
    selected_tea = st.selectbox("Filter by tea type",tea_type)
    filtered_data = df[df["Tea_Type"] == selected_tea]
    st.dataframe(filtered_data)
