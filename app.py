import streamlit as st

st.title("Growth Mindset Web App")

st.write("Welcome to the Growth Mindset Challenge!")

# Add some features to make the app interactive
st.slider("Set your learning goal", 1, 100)
st.text_area("What's your biggest challenge?", "Describe your challenge...")
if st.button("Click me!"):
    st.write("Button clicked!")
