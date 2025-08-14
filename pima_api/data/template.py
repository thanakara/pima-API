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


def average_check(request: Request) -> list[str]:
    aavg = "Above Average"
    bavg = "Below Average"

    if request.Pregnancies > 3:
        pre = aavg
    else:
        pre = bavg

    if request.Glucose > 121.65:
        glu = aavg
    else:
        glu = bavg

    if request.BloodPressure > 73.38:
        bp = aavg
    else:
        bp = bavg

    if request.SkinThickness > 29.1:
        st = aavg
    else:
        st = bavg

    if request.Insulin > 140.67:
        ins = aavg
    else:
        ins = bavg

    if request.BMI > 32.45:
        bmi = aavg
    else:
        bmi = bavg

    if request.DiabetesPedigreeFunction > 0.4718:
        dpf = aavg
    else:
        dpf = bavg

    if request.Age > 33:
        age = aavg
    else:
        age = bavg

    stats = [pre, glu, bp, st, ins, bmi, dpf, age]

    return stats
