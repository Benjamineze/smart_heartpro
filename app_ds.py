import streamlit as st
from EDA import show_EDA
import base64
#from predict_pag import show_predict_pag
import sklearn

from predict_pag import show_predict_pag


# Function to add background
def set_background(image_file):
    with open(image_file, "rb") as file:
        data = file.read()
        encoded_image = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded_image}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Add the custom bar
st.title('Smart Heart Pro')

# Page selection
page = st.selectbox('predict or Explore', ( 'Predict', 'EDA'))

if page == 'Predict':
    set_background("abstract-blue-red-human-heart-600nw-2313147451.webp")
    show_predict_pag()

else:
    set_background("heart-1767552_1280.jpg")
    show_EDA()
