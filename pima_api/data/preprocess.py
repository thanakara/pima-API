from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def preprocess_dataset(datapath: Path | str) -> pd.DataFrame:
    df = pd.read_csv(datapath)
    eq_zero_series = df.eq(0).any().drop(labels=["Pregnancies", "Outcome"])
    mask = eq_zero_series.tolist()
    cols = eq_zero_series[mask].index
    df[cols] = df[cols].apply(lambda col_: col_.replace(0, col_.median()))

    return df


def stratify_split_dataset(
    datapath: Path | str, train_size: int | float, seed: int = 42
) -> tuple[np.ndarray]:
    df_prep = preprocess_dataset(datapath)
    train_set, test_set = train_test_split(
        df_prep, train_size=train_size, stratify=df_prep["Outcome"], random_state=seed
    )
    X_train = train_set.drop("Outcome", axis=1).to_numpy()
    y_train = train_set["Outcome"].values

    X_test = test_set.drop("Outcome", axis=1).to_numpy()
    y_test = test_set["Outcome"].values

    return X_train, y_train, X_test, y_test
