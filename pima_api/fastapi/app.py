import json

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from pima_api.constant import Filepath
from pima_api.data.template import Request, Response, average_check

api = FastAPI()

modeljob_path = Filepath.MODELJOB.value
model = joblib.load(modeljob_path)


@api.get("/")
def home():
    message = {"message": "Onset Diabetes Predictions: end@_PIMA-App_v1.0"}
    return JSONResponse(message)


@api.get("/classification_report")
def report():
    with open(Filepath.REPORTPATH.value, "r") as f_:
        clf_report = json.load(f_)

    return clf_report


@api.post("/check_request")
def first_results(request: Request) -> dict:
    results = average_check(request=request)
    return JSONResponse(results)


@api.post("/predict_diabetes")
def invoke_endpoint(request: Request) -> dict:
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
        non_diabetes = {"prediction": "Non-Diabetic"}
        return JSONResponse(non_diabetes)

    elif prediction == Response.POSITIVE:
        diabetes = {"prediction": "Diabetic"}
        return JSONResponse(diabetes)

    else:
        raise HTTPException
