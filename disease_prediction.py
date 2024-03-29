import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Loading ML Models

diabetes_model = pickle.load(open("/workspaces/ML_disease_Prediction_Project_with_streamlit_interface/models/diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open("/workspaces/ML_disease_Prediction_Project_with_streamlit_interface/models/heart_disease_model.sav", 'rb'))

parkinson_model = pickle.load(open("/workspaces/ML_disease_Prediction_Project_with_streamlit_interface/models/parkinson_model.sav", 'rb'))


#sidebar

with st.sidebar:

    select = option_menu('Machine Learning Disease prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinson Prediction'],

                          icons = ['activity', 'heart-pulse-fill', 'person-arms-up'],

                          default_index=0)

# Diabetes Prediction Page
if(select == 'Diabetes Prediction'):

    #page title
    st.title('Diabetes prediction Using ML')

    # Inputs
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')

    # Prediction
    diadetes_dignosis = ''

    # Button for prediction
    if st.button('Submit'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]) 
        if diabetes_prediction[0] == 1:
            diadetes_dignosis = 'The person is diabetic'
        else:
            diadetes_dignosis = 'The person is not diabetic'

    st.success(diadetes_dignosis)

if(select == 'Heart Disease Prediction'):

    #page Title
    st.title('Heart Disease Prediction Using ML')

if(select == 'Parkinson Prediction'):

    #page Title
    st.title('Parkinson Prediction Using ML')



