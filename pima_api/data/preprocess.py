from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess_dataset(datapath: Path | str) -> pd.DataFrame:
    pima = pd.read_csv(datapath)
    cols_toreplace = [
        col
        for col in pima.columns
        if pima[col].min() == 0 and col not in ("Pregnancies", "Outcome")
    ]
    pima[cols_toreplace] = pima[cols_toreplace].where(
        pima[cols_toreplace].ne(0), np.nan
    )
    pima[cols_toreplace] = pima[cols_toreplace].apply(lambda s_: s_.fillna(s_.median()))

    return pima


def stratify_split_dataset(
    datapath: Path | str, train_size: int | float, seed: int = 42
) -> tuple[np.ndarray]:
    df_prep = preprocess_dataset(datapath)
    train_set, test_set = train_test_split(
        df_prep, train_size=train_size, stratify=df_prep["Outcome"], random_state=seed
    )
    X_train = train_set.drop("Outcome", axis=1)
    y_train = train_set["Outcome"].values

    X_test = test_set.drop("Outcome", axis=1)
    y_test = test_set["Outcome"].values

    std_scaler = StandardScaler()
    X_train_scaled = std_scaler.fit_transform(X_train)
    X_test_scaled = std_scaler.transform(X_test)

    return X_train_scaled, y_train, X_test_scaled, y_test
