import json

import joblib
from fastapi import FastAPI, HTTPException

from pima_api.constant import Filepath
from pima_api.data.template import Request, Response, average_check

api = FastAPI()

modeljob_path = Filepath.MODELJOB.value
model = joblib.load(modeljob_path)


@api.get("/")
def home():
    return {"message": "Onset Diabetes Predictions: end@_PIMA-App_v1.0"}


@api.get("/classification_report")
def report():
    with open(Filepath.REPORTPATH.value, "r") as f_:
        clf_report = json.load(f_)

    return clf_report


@api.post("/check_request")
def first_results(request: Request) -> dict:
    stats = average_check(request=request)
    req_keys = Request.model_fields.keys()

    return {name: stat for name, stat in zip(req_keys, stats)}


@api.post("/predict_diabetes")
def invoke_endpoint(request: Request) -> str:
    pregn = request.Pregnancies
    glucose = request.Glucose
    bl_pre = request.BloodPressure
    skin_thickness = request.SkinThickness
    insulin = request.Insulin
    bmi = request.BMI
    dpf = request.DiabetesPedigreeFunction
    age = request.Age

    features = [[pregn, glucose, bl_pre, skin_thickness, insulin, bmi, dpf, age]]
    prediction = model.predict(features).ravel()

    if prediction == Response.NEGATIVE:
        return "Non-Diabetic"

    elif prediction == Response.POSITIVE:
        return "Diabetic"

    else:
        raise HTTPException
