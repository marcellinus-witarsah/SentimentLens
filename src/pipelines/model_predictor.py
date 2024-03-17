import numpy as np
from src.config.configuration import ConfigurationManager
from src.models.model_predictor import ModelPredictor
from src.data.data_transformation import DataTransformation


class ModelPredictoripeline:
    def __init__(self):
        """
        Instantiate `ModelPredictoripeline` class
        """
        self.configuration_manager = ConfigurationManager()
        self.data_transformation_config = (
            self.configuration_manager.get_data_transformation_config()
        )
        self.model_predictor_config = (
            self.configuration_manager.get_model_predictor_config()
        )
        self.data_transformation = DataTransformation(self.data_transformation_config)
        self.model_predictor = ModelPredictor(self.model_predictor_config)

    def run(self, data: np.array) -> np.array:
        """
        Ingest data
        """
        preprocessed_data = self.data_transformation.preprocess_text(data)
        preprocessed_data = np.array([preprocessed_data])
        prediction = self.model_predictor.predict(preprocessed_data)
        return prediction
