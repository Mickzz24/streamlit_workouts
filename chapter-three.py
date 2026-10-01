import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/10377676/pexels-photo-10377676.jpeg", width= 200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/31141291/pexels-photo-31141291.jpeg?_gl=1*rhefu3*_ga*MTgwMTQ2MjMxMS4xNzg4MjgwOTg1*_ga_8JE65Q40S6*czE3ODgzMjQ3MjQkbzIkZzEkdDE3ODgzMjQ4NjYkajU5JGwwJGgw", width= 200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting masala chai")

elif vote2:
    st.success("Thanks for voting adrak chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "Kesar", "Adrak"])

st.write(f"Welcome {name} your {tea} is getting ready")

with st.expander("Show Chai Making Instructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Add sugar as you wish
    """
    )

st.markdown("### Welcome to Chai App")
st.markdown(">Blockquote - heyyyyyyy")

