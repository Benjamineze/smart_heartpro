import streamlit as st
from EDA import show_EDA
#from predict_pag import show_predict_pag
import sklearn

from predict_pag import show_predict_pag



# Add the custom bar
st.title('Smart Heart Pro')

# Rest of your Streamlit app
page = st.selectbox('predict or Explore', ( 'Predict', 'EDA'))




if page == 'Predict':
    show_predict_pag()
else:
    show_EDA()
