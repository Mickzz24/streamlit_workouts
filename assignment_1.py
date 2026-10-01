import streamlit as st

st.title("Programming Language Picker")
st.subheader("Welcome to Programming Language Picker")
st.write("Here, You can select your favourite programming Language")
st.text("SO LET'S GET STARTED")

lan = st.selectbox("Select Your favourite programming language:", ["python","Java","C","SQL","COBOL","HTML","C++","R"])
st.write(f"Congrats!!You have selected {lan}. Successfully")

st.success("HOORAY!!Thank you for your valuable time")
