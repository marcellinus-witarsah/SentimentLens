import os
import sys
import numpy as np
import joblib
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.entities.config_entity import ModelPredictorConfig


class ModelPredictor:
    def __init__(self, config: ModelPredictorConfig):
        self.config = config
        self.model = self.get_model()

    def get_model(self):
        """
        Get trained model
        """
        logger.info("Load model")
        model = None
        with open(self.config.model_path, "rb") as f:
            model = joblib.load(f)
        return model

    def predict(self, data: np.array) -> np.array:
        """
        Predict the data

        Args:
            data (np.array): Preprocessed text
        Return:
            np.array: Prediction results
        """
        logger.info("Predict")
        prediction = self.model.predict(data)
        return prediction[0]
