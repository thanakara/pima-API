import json
from pathlib import Path

import joblib
from omegaconf import DictConfig
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from xgboost import XGBClassifier

from pima_api.constant import Filepath
from pima_api.data.preprocess import stratify_split_dataset


def fit_report_and_serialize(config: DictConfig) -> RandomForestClassifier:
    # Config-based model selection
    if config.modelname == "random_forest":
        model = RandomForestClassifier(
            n_estimators=config.n_estimators,
            criterion=config.criterion,
            max_depth=config.max_depth,
            min_samples_split=config.min_samples_split,
            max_features=config.max_features,
            random_state=config.seed,
            oob_score=config.oob_score,
            n_jobs=config.n_jobs,
            class_weight=config.class_weight,
        )

    elif config.modelname == "xgboost":
        model = XGBClassifier(
            objective=config.objective,
            random_state=config.seed,
            n_estimators=config.n_estimators,
            subsample=config.subsample,
            max_depth=config.max_depth,
            eta=config.eta,
            colsample_bytree=config.colsample_bytree,
        )

    else:
        raise ValueError(
            "Modelname not in structure. Name given: %s" % config.modelname
        )

    X_train_scaled, y_train, X_test_scaled, y_test = stratify_split_dataset(
        datapath=Filepath.DATAPATH.value, train_size=config.train_size, seed=config.seed
    )

    # Train-Job
    model.fit(X_train_scaled, y_train)

    with Path.open(Filepath.MODELJOB.value, "wb") as f_:
        joblib.dump(model, f_, protocol=4)

    y_pred = model.predict(X_test_scaled)
    report = classification_report(
        y_test, y_pred, target_names=["Non-Diabetic", "Diabetic"], output_dict=True
    )
    report_json = json.dumps(report, indent=4)

    with Path.open(Filepath.REPORTPATH.value, "w") as f_:
        f_.write(report_json)

    return model
