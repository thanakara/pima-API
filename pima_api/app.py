import joblib
from fastapi import FastAPI, HTTPException

from pima_api.constant import Filepath
from pima_api.data.template import Request, Response

api = FastAPI()

modeljob_path = Filepath.MODELJOB.value
rand_f = joblib.load(modeljob_path)


@api.post("/predict")
def endpoint(request: Request) -> str:
    pregnancies = request.Pregnancies
    glucose = request.Glucose
    blood_pressure = request.BloodPressure
    skin_thickness = request.SkinThickness
    insulin = request.Insulin
    bmi = request.BMI
    dpf = request.DiabetesPedigreeFunction
    age = request.Age
    features = [
        [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
    ]
    prediction = rand_f.predict(features).ravel()
    if prediction == Response.NEGATIVE:
        return "Negative"
    elif prediction == Response.POSITIVE:
        return "Positive"
    else:
        raise HTTPException
