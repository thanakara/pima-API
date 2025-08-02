import joblib
from omegaconf import DictConfig
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from pima_api.constant import Filepath
from pima_api.data.preprocess import stratify_split_dataset


def fit_report_and_serialize(
    config: DictConfig, artifacts: bool = False
) -> RandomForestClassifier:
    rand_f = RandomForestClassifier(
        n_estimators=config.n_estimators,
        criterion=config.criterion,
        max_depth=config.max_depth,
        min_samples_split=config.min_sample_split,
        max_features=config.max_features,
        random_state=config.seed,
        oob_score=config.oob_score,
        n_jobs=config.n_jobs,
        class_weight=config.class_weight,
    )

    X_train, y_train, X_test, y_test = stratify_split_dataset(
        datapath=Filepath.DATAPATH.value, train_size=config.train_size, seed=config.seed
    )
    rand_f = rand_f.fit(X_train, y_train)

    if artifacts:
        Y_pred = rand_f.predict(X_test)
        with open("random_forest.pkl", "wb") as f_:
            joblib.dump(rand_f, f_, protocol=4)

        report = classification_report(y_test, Y_pred)
        with open("report.json", "w") as f_:
            f_.write(report)

    return rand_f
