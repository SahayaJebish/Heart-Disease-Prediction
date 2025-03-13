import joblib
import streamlit as st

with open('heart_disease_model.joblib','rb')as file:
    loaded_model = joblib.load(file)

st.title('Heart Disease Prediction')

age = st.number_input('Age', min_value=29, max_value=77)
sex = st.radio('Sex (1: Male, 0: Female)',[1,0])
cp = st.slider('Chest pain type (1-4)',min_value=1, max_value=4, value=2)
bp = st.number_input('Blood Pressure (94-200)',min_value=94,max_value=200,value=150)
chol = st.number_input('Cholesterol (126-564)',min_value=126,max_value=564,value=300)
fbs = st.radio('FBS (Fasting Blood Sugar) over 120 (True: 1, False: 0)',[1,0])
ecg = st.selectbox('ECG results (0-2)',[0,1,2])
hr = st.number_input('Max Heart Rate Achieved (71-202)',min_value=72,max_value=202,value=150)
ex = st.radio('Exercise angina (1: Yes, 0: No)',[1,0])
dep = st.number_input('ST Depression Induced by Exercise (0.0-6.2)',min_value=0.0,max_value=6.2,value=3.0)
slope = st.radio('Slope of the Peak Exercise ST Segment (1-3)',[1,2,3])
ves = st.selectbox('Number of vessels fluro (0-3)',[0,1,2,3])
ti = st.selectbox('Thallium (3,6,7)', [3,6,7])

if st.button('Predict'):
    x = loaded_model.predict([[age, sex, cp, bp, chol, fbs, ecg, hr, ex, dep, slope, ves, ti]])


    if x[0]==1:
        st.warning('Presence')
    else:
        st.success('Absence')