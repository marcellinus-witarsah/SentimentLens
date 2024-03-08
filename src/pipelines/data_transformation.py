import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.config.configuration import ConfigurationManager
from src.data.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:
    def __init__(self):
        """
        Instantiate `DataTransformationTrainingPipeline` class
        """
        self.configuration_manager = ConfigurationManager()

    def run(self):
        """
        Ingest data
        """
        data_transformation = DataTransformation(
            config=self.configuration_manager.get_data_transformation_config()
        )
        data_transformation.clean_data()
        data_transformation.preprocess_texts()
        data_transformation.split_data()


if __name__ == "__main__":
    STAGE_NAME = "Data transformation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_transformation_training_pipeline = DataTransformationTrainingPipeline()
        data_transformation_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)
