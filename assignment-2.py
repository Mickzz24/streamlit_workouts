import streamlit as st
from datetime import date

st.title("Age Calculator")
st.subheader("Welcome to Age Calculator")
st.write("Here you can find your age")

dob = st.date_input("Date of Birth",
                    value=date(2004, 1, 1),
                    min_value= date(2004,1,1),
                    max_value= date.today()
                    )

today = date.today()

age = today.year - dob.year

st.success(f"your age is {age}")