import os
import sys
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.utils.common import read_yaml, create_directories
from src.entities.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: str = os.getenv("CONFIG_FILE_PATH"),
        params_filepath: str = os.getenv("PARAMS_FILE_PATH"),
        schema_filepath: str = os.getenv("SCHEMA_FILE_PATH"),
    ):
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))
        self.schema = read_yaml(Path(schema_filepath))
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get configuration for data ingestion
        
        Returns:
            DataIngestionConfig: Configuration for data ingestion
        """
        logger.info("Get data ingest configuration")
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_path  = config.source_path,
            unzip_dir = config.unzip_dir,
        )
        return data_ingestion_config