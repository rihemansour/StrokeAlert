import streamlit as st
import pickle 
import numpy as np

def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

model = load_model()

def show_predict_page():
    values = ("Yes","No")
    work_values = ("Private","Self employed","Government job","I'm a child","Never worked")
    residence_values = ("Urban","Rural")
    gender_values = ("Male","Female")
    st.markdown("<span style='color:red; font-size: 3em; font-weight: bold;'>Welcome to StrokeAlert!</span>", unsafe_allow_html=True)
    st.write("We need some information to predict the risk")
    gender = st.selectbox("What's your gender",gender_values)
    age = st.slider("Select your age", 0, 100, 20)
    hypertension = st.selectbox("Do you suffer from Hypertension", values)
    heart_disease = st.selectbox("Do you suffer from a heart disease", values)
    ever_married = st.selectbox("Are you married", values)
    work_type = st.selectbox("What's your work type", work_values)
    redidence_type = st.selectbox("What's your residence type",residence_values)
    bmi = st.slider("Select your bmi",18,50,24)
    smoking_status = st.selectbox("Do you smoke",values)