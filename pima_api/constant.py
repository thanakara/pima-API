from enum import Enum
from pathlib import Path


class Filepath(Enum):
    ROOT = Path.cwd()
    DATAPATH = ROOT / "pima_api" / "data" / "pima.csv"
    CONFIGPATH = ROOT / "pima_api" / "conf"
    REPORTPATH = ROOT / "pima_api" / "model" / "report.json"
    MODELJOB = REPORTPATH.with_name("model.pkl")
