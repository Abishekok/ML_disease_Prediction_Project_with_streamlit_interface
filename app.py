import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Loading ML Models

diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open("heart_disease_model.sav", 'rb'))

parkinson_model = pickle.load(open("parkinson_model.sav", 'rb'))


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

    # Inputs data
    #Columns of input
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')

    with col1:    
        SkinThickness = st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI Value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age = st.text_input('Age of the Person')


    # Prediction
    diadetes_dignosis = ''

    # Button for prediction
    if st.button('Submit'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diabetes_prediction = diabetes_model.predict([user_input]) 
        if diabetes_prediction[0] == 1:
            diadetes_dignosis = 'The person is diabetic'
        else:
            diadetes_dignosis = 'The person is not diabetic'

    st.success(diadetes_dignosis)

if(select == 'Heart Disease Prediction'):

    #page Title
    st.title('Heart Disease Prediction Using ML')

    #Input Column
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographc Result')

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')


    # Prediction
    heart_diagnosis = ''

    # Button for prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])


        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson prediction page
if(select == 'Parkinson Prediction'):

    #page Title
    st.title('Parkinson Prediction Using ML')

    #Input
    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP= st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('MDVP:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # Prediction
    parkinsons_diagnosis = ''

    # Prediction Button
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        
        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinson_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The Person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The Person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    st.success(parkinsons_prediction)


