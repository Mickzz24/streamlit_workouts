import streamlit as st
import joblib
from nltk.stem import PorterStemmer

st.title("Sentiment Analysis Checker")
st.subheader("Input Text")
sentence = st.text_input("Enter the text")

st.write(f"This is your input text :  {sentence}")


