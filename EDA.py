from altair import Axis
import streamlit as st
import pandas as pd
from  matplotlib import pyplot as plt

import seaborn as sns


@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_dataset1.csv")
   
    

    return df
df =  load_data()



def show_EDA():
    #st.title ('Exploratory Data Analysis')

    st.write ("""### Patients heart disease Analysis""")

    

    st.write("""##### Heart disease By Gender""")

     # Create a figure and axes
    fig, ax = plt.subplots(figsize=(6, 4))

    sns.countplot(x="sex", data=df, hue="target", ax=ax)
    plt.xlabel("Gender")
    plt.ylabel("Count of Patients")
    ax.bar_label(container=ax.containers[0], label="Count of Patients");
    ax.bar_label(container=ax.containers[1], label="Count of Patients");

    # Display the plot using st.pyplot()
    st.pyplot(fig)

    


    st.write("""##### Heart Disease by Maximum Heart Rate Achieved""")
    fig, ax = plt.subplots(figsize=(4, 3))


    # KDE plot for 'maximum heart rate achieved' with different colors for 'yes' and 'no'
    sns.kdeplot(df.loc[df['target'] == 'yes', 'max_heart_rate_achieved'], color='red', fill=True, label='Yes')
    sns.kdeplot(df.loc[df['target'] == 'no', 'max_heart_rate_achieved'], color='blue', fill=True, label='No')

    plt.xlabel('Maximum Heart Rate Achieved')
    plt.ylabel('Density')
    plt.legend()
    
    st.pyplot(fig)



    st.write("""##### Heart Disease By chest pain type""")

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(6, 4))

    # Seaborn countplot
    sns.countplot(x="Chest_pain_type", data=df, hue="target", ax=ax)

    # Customize labels and title
    plt.xlabel(" Chest pain type")
    plt.ylabel("Count of patients")
    ax.bar_label(container=ax.containers[0], label="Count of Patients");
    ax.bar_label(container=ax.containers[1], label="Count of Patients");


    # Display the plot using st.pyplot()
    st.pyplot(fig)


    st.write("""##### Heart Disease By Number of major vessels""")
    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(x= 'num_of_major_vessels' , data=df, hue="target")
    plt.xlabel('num_of_major_vessels')
    plt.ylabel("count of patients")
    ax.bar_label(container=ax.containers[0], label="count of num_of_major_vessels")
    ax.bar_label(container=ax.containers[1], label="count of num_of_major_vessels")
    

    st.pyplot(fig)

    
    st.write("""##### Heart Disease By st_depression """)
    fig, ax = plt.subplots(figsize=(6, 4))

    sns.lineplot(x='st_depression', y='count', hue='target',
                  data=df.groupby(['st_depression', 'target']).size().reset_index(name='count'))
    plt.xlabel('st_depression')
    plt.ylabel("count of patients")
   
    st.pyplot(fig)


    st.write("""##### Heart Disease By thalassemai""")
    fig, ax = plt.subplots(figsize=(6,4))


    sns.countplot(x= 'thalassemai', data=df, hue="target")
    plt.xlabel('thalassemai')
    plt.ylabel("count of thalassemai")
    ax.bar_label(container=ax.containers[0], label="count of age thalassemai")
    ax.bar_label(container=ax.containers[1], label="count of age thalassemai")
    
    st.pyplot(fig)

    st.write("""##### Heart Disease By exercise_induced_angina """)
    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(x= 'exercise_induced_angina', data=df, hue="target")
    plt.xlabel('exercise_induced_angina')
    plt.ylabel("count of patients")
    ax.bar_label(container=ax.containers[0], label="count of exercise_induced_angina")
    ax.bar_label(container=ax.containers[1], label="count of exercise_induced_angina")
    
    st.pyplot(fig)


    st.write("""##### Heart Disease By ST slope """)
    fig, ax = plt.subplots(figsize=(6,4))
    
    sns.countplot(x= 'st_slope', data=df, hue="target")
    plt.xlabel('st_slope')
    plt.ylabel("count of patients")
    ax.bar_label(container=ax.containers[0], label="count of st_slope")
    ax.bar_label(container=ax.containers[1], label="count of st_slope")

    st.pyplot(fig)
    