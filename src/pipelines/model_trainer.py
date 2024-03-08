import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.config.configuration import ConfigurationManager
from src.models.model_trainer import ModelTrainer


class ModelTrainerTrainingPipeline:
    def __init__(self):
        """
        Instantiate `ModelTrainerTrainingPipeline` class
        """
        self.configuration_manager = ConfigurationManager()

    def run(self):
        """
        Ingest data
        """
        model_trainer = ModelTrainer(
            config=self.configuration_manager.get_model_trainer_config()
        )
        model_trainer.train()


if __name__ == "__main__":
    STAGE_NAME = "Model training stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        model_trainer_training_pipeline = ModelTrainerTrainingPipeline()
        model_trainer_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)
