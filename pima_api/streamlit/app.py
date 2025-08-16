import requests
import streamlit as st

st.header("Onset Diabetes Prediction 🩺 ")

st.subheader("Fill the form below")

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


@st.dialog("Classification Report", width="large")
def report():
    report = requests.get("http://backend:80/classification_report")
    json_data = report.json()
    st.dataframe(json_data)


if st.sidebar.button("Model Metrics"):
    report()

if st.button("First Results"):
    try:
        response = requests.post("http://backend:80/check_request", json=data)
        if response.status_code == 200:
            result = response.json()
            if result is not None:
                st.table(result)
            else:
                st.error("Ivalid response from API.")
        else:
            st.error(f"API returned error: {response.status_code}")
    except Exception as e:
        st.error(f"Failed to get results: {e}")


if st.button("Onset Prediction"):
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
