import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger, save_json
from src.config.configuration import ConfigurationManager
from src.models.model_evaluation import ModelEvaluation


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        """
        Instantiate `ModelEvaluationTrainingPipeline` class
        """
        self.configuration_manager = ConfigurationManager()

    def run(self):
        """
        Ingest data
        """
        model_evaluation = ModelEvaluation(
            self.configuration_manager.get_model_evaluation_config()
        )
        model_evaluation.evaluate_model()


if __name__ == "__main__":
    STAGE_NAME = "Model evaluation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        model_evaluation_training_pipeline = ModelEvaluationTrainingPipeline()
        model_evaluation_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)
