import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.config.configuration import ConfigurationManager
from src.data.data_validation import DataValidation

STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    configuration_manager = ConfigurationManager()
    data_ingestion = DataValidation(
        config=configuration_manager.get_data_validation_config()
    )
    data_ingestion.validate_data()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(e)
