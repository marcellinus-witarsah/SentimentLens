import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.config.configuration import ConfigurationManager
from src.data.data_labeling import DataLabeling

STAGE_NAME = "Data labeling stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    configuration_manager = ConfigurationManager()
    data_labeling = DataLabeling(
        config=configuration_manager.get_data_labeling_config()
    )
    data_labeling.label_data()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(e)
