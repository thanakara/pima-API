from enum import IntEnum

from pydantic import BaseModel


class Request(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


class Response(IntEnum):
    NEGATIVE = 0
    POSITIVE = 1
