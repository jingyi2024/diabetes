import streamlit as st
import joblib
import numpy as np

# Load your trained model from the specified path using a raw string to handle backslashes correctly
model_path = r'C:\Drive D\0CURRENT0\AI\MIT\Data Science\Clean Test Diabeties\diabetes_prediction_model.joblib'
model = joblib.load(model_path)

# Creating the Streamlit interface
st.title('Diabetes Prediction App')
st.write('Please enter the following data to predict diabetes:')

# Form to input new data for prediction
pregnancies = st.number_input('Number of pregnancies', min_value=0, step=1)
glucose = st.number_input('Plasma glucose concentration', min_value=0, step=1)
blood_pressure = st.number_input('Diastolic blood pressure (mm Hg)', min_value=0, step=1)
skin_thickness = st.number_input('Triceps skin fold thickness (mm)', min_value=0, step=1)
insulin = st.number_input('2-Hour serum insulin (mu U/ml)', min_value=0, step=1)
bmi = st.number_input('Body mass index', min_value=0.0, step=0.1)
diabetes_pedigree = st.number_input('Diabetes pedigree function', min_value=0.0, step=0.01)
age = st.number_input('Age', min_value=0, step=1)

# Button to make prediction
if st.button('Predict Diabetes'):
    # Create an array from the inputs
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    prediction = model.predict(input_data)
    
    # Output the prediction
    if prediction[0] == 0:
        st.success('The prediction is: No Diabetes')
    else:
        st.error('The prediction is: Diabetes')









