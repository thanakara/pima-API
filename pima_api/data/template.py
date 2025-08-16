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

    @property
    def averages(self) -> dict:
        return {
            "Pregnancies": 3,
            "Glucose": 121.65,
            "BloodPressure": 73.38,
            "SkinThickness": 29.1,
            "Insulin": 140.67,
            "BMI": 32.45,
            "DiabetesPedigreeFunction": 0.4718,
            "Age": 32,
        }


class Response(IntEnum):
    NEGATIVE = 0
    POSITIVE = 1


def average_check(request: Request) -> dict[str, str]:
    above = "above_average"
    below = "below_average / normal"
    request_model = request.model_dump()
    results = {}

    for key, value in request_model.items():
        if value > request.averages.get(key):
            results.update({key: above})
        else:
            results.update({key: below})

    return results
