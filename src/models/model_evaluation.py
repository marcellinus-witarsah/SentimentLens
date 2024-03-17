import joblib
import mlflow
import pandas as pd
from urllib.parse import urlparse
from sklearn.metrics import precision_score, recall_score, f1_score

from src.utils.common import logger, save_json
from src.entities.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_metrics(self, y_test, y_pred):
        """
        Calculate evaluation metrics
        """
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        return precision, recall, f1

    def evaluate_model(self):
        """
        Evaluate model
        """
        logger.info("Evaluate model")
        test = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = (
            test.drop(columns=[self.config.target_column], axis=1)
            .to_numpy()
            .reshape(-1)
        )
        y_test = test[[self.config.target_column]].to_numpy().reshape(-1)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            logger.info("Log model into MLFlow")
            y_pred = model.predict(X_test)
            precision, recall, f1 = self.evaluate_metrics(y_test, y_pred)
            scores = {"precision": precision, "recall": recall, "f1_score": f1}

            save_json(path=self.config.metric_file_name, data=scores)
            mlflow.log_params(self.config.model_params)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("f1", f1)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    model,
                    "model",
                    registered_model_name="CountVectorizer+MultinomialNB",
                )
            else:
                mlflow.sklearn.log_model(model, "model")
