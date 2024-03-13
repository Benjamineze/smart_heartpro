import streamlit as st
import pickle 
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline


# Load model
def load_model():
    with open('pipe_hrtmod_.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
pipe = data['model']





def show_predict_pag():
    st.write("""### Heart disease prediction""")
    st.write("""###### Kindly enter details""")

    sex_options = ('Male', 'Female')
    chest_pain_type_options = ('typical angina', 'atypical angina', 'non-anginal pain', 'asymtomatic')
    exercise_induced_Angina_options = ('yes', 'no')
    thalassemai_options = ('Normal', 'fixed defect', 'Reversable defect')
    st_slope_options = ('upsloping', 'flat', 'downsloping')

    sex = st.selectbox('Gender', sex_options)
    Chest_pain_type = st.selectbox('Chest pain type', chest_pain_type_options)
    exercise_induced_angina = st.selectbox('Exercise induced angina', exercise_induced_Angina_options)
    thalassemai = st.selectbox('Thalassemai type', thalassemai_options)
    st_slope = st.selectbox('st_slope', st_slope_options)

    st_depression = st.slider('ST depression', 0.0, 5.0, 0.1)
    num_of_major_vessels = st.selectbox('Number of major vessels', [0, 1, 2, 3, 4, 5])
    max_heart_rate_achieved = st.slider('Maximum heart rate', 0, 200, 50)

   

    ok = st.button("Predict Heart Disease")
    if ok:
        
        expected_columns = ['sex', 'Chest_pain_type', 'max_heart_rate_achieved', 'exercise_induced_angina',
                    'st_depression', 'st_slope', 'num_of_major_vessels', 'thalassemai']
        
        user_df = pd.DataFrame([[sex, Chest_pain_type, max_heart_rate_achieved, exercise_induced_angina,
                         st_depression, st_slope, num_of_major_vessels, thalassemai]],
                       columns=expected_columns)

        # Make sure categorical columns have the correct data type
        user_df['sex'] = user_df['sex'].astype('category')
        user_df['Chest_pain_type'] = user_df['Chest_pain_type'].astype('category')
        user_df['exercise_induced_angina'] = user_df['exercise_induced_angina'].astype('category')
        user_df['thalassemai'] = user_df['thalassemai'].astype('category')
        user_df['st_slope'] = user_df['st_slope'].astype('category')

        #user_input = ([[sex, Chest_pain_type, max_heart_rate_achieved, exercise_induced_angina,
              
                      #st_depression, st_slope, num_of_major_vessels, thalassemai]])

        #user_df = pd.DataFrame([user_input])

        

# Make predictions and obtain probabilities
        heart_disease_proba = pipe.predict_proba(user_df)[:, 1]  # Assuming you want the probability of the positive class

# ... ( Make a decision based on a threshold (adjust the threshold as needed)
        threshold = 0.5
        heart_disease = 1 if heart_disease_proba > threshold else 0

    # Output results
        if heart_disease == 1:
            st.subheader(f'This patient has heart disease with a probability of {heart_disease_proba[0]*100:.2f}%')
        else:
            st.subheader(f'This patient does not have heart disease with a probability of {(1 - heart_disease_proba[0])*100:.2f}%')
        

       