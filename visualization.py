import streamlit as st
from PIL import Image

# Set the title of the app
st.title("My Streamlit App")

# Show some text
st.write("Welcome to my app!")

# Load and display an image
image = Image.open("image.jpg")
st.image(image, caption="A beautiful image", use_column_width=True)
