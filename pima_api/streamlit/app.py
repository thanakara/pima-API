import requests
import streamlit as st

st.title("🩺 Onset Diabetes Prediction")

data = {
    "Pregnancies": st.number_input("Pregnancies", min_value=0, step=1, format="%d"),
    "Glucose": st.number_input("Glucose", min_value=0, step=1, format="%d"),
    "BloodPressure": st.number_input(
        "Blood Pressure", min_value=0, step=1, format="%d"
    ),
    "SkinThickness": st.number_input(
        "Skin Thickness", min_value=0, step=1, format="%d"
    ),
    "Insulin": st.number_input("Insulin", min_value=0.0, format="%.2f"),
    "BMI": st.number_input("BMI", min_value=0.0, format="%.2f"),
    "DiabetesPedigreeFunction": st.number_input(
        "Diabetes Pedigree Function", min_value=0.0, format="%.3f"
    ),
    "Age": st.number_input("Age", min_value=0, step=1, format="%d"),
}

if st.button("Predict"):
    try:
        response = requests.post("http://backend:80/predict_diabetes", json=data)
        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction", None)
            if prediction is not None:
                st.success(f"Prediction: {prediction}")
            else:
                st.error("Invalid response from API.")
        else:
            st.error(f"API returned error: {response.status_code}")
    except Exception as e:
        st.error(f"Failed to get prediction: {e}")
