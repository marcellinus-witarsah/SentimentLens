import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.config.configuration import ConfigurationManager
from src.data.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self):
        """
        Instantiate `DataIngestionTrainingPipeline` class
        """
        self.configuration_manager = ConfigurationManager()

    def run(self):
        """
        Ingest data
        """
        data_ingestion = DataIngestion(
            config=self.configuration_manager.get_data_ingestion_config()
        )
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    STAGE_NAME = "Data ingestion stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)
