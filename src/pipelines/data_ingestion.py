import os
import sys
from dotenv import load_dotenv, find_dotenv
import zipfile
load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.config.configuration import ConfigurationManager
from src.data.data_ingestion import DataIngestion

STAGE_NAME = "Data ingestion Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    configuration_manager = ConfigurationManager()
    data_ingestion = DataIngestion(config=configuration_manager.get_data_ingestion_config())
    data_ingestion.extract_zip_file()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(e)
