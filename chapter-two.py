import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai")

tea_type = st.radio("Pick your chai base :", ["Milk", "Water", "Oatmilk", "Almond Milk"])
st.write(f"Selected Base : {tea_type}")

flavour = st.selectbox("Choose flavour :", ["Hazelnut", "Kesar", "Tulsi", "Almond"])
st.write(f"Selected Flavour : {flavour}")

sugar = st.slider("Sugar Level (Spoon)",0,2,5)
st.write(f"Selected sugar level (Spoon): {sugar}")

cups = st.number_input("How many cups",min_value=1, max_value= 10, step= 1 )
st.write(f"Selected no of cups {cups}")

name = st.text_input("Enter Your Name")
if name:
    st.write(f"Welcome {name}!!! Your chai is on the way")

dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth is {dob}")
