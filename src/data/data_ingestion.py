import os
import zipfile
from src.utils.common import logger
from src.entities.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Instantiate `DataIngestion` class

        Args:
            config (DataIngestionConfig): configuration for data ingestion
        """
        logger.info("Instantiate `DataIngestion` class")
        self.config = config

    def extract_zip_file(self):
        """Extract `.zip` file"""
        logger.info("Extract .zip file")
        target_dir = self.config.target_dir
        os.makedirs(target_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.source_path, "r") as zip_ref:
            zip_ref.extractall(target_dir)
