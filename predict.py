import streamlit as st
import pickle 
import numpy as np
from encoders import *
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
    avg_glucose_level = st.slider("Select your average glucose level in mg/dl",0,350,80)
    ok = st.button("Predict risk")
    if ok:
        gender = encode_gender(gender)
        ever_married = encode_yes_no(ever_married)
        smoking_status = encode_yes_no(smoking_status)
        hypertension = encode_yes_no(hypertension)
        heart_disease = encode_yes_no(heart_disease)
        work_type = encode_work_type(work_type)
        redidence_type = encode_residence_type(redidence_type)
        X = np.array([[gender,age,hypertension,heart_disease,ever_married,work_type,redidence_type,avg_glucose_level,bmi,smoking_status]])
        X = X.astype(float)
        risk = model.predict(X)
        if(risk==1):
            st.subheader("You are in risk! You must consult a Doctor ASAP!")
        else:
            st.subheader("You're fine! Stay Healthy")
  