import os
import sys
import pandas as pd
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.entities.config_entity import DataLabelingConfig


class DataLabeling:
    def __init__(self, config: DataLabelingConfig):
        """
        Instantiate `DataIngestion` class

        Args:
            config (DataIngestionConfig): configuration for data ingestion
        """
        self.config = config

    def label_data(self):
        """Label data"""
        logger.info("Label data")
        source_path = self.config.source_path
        df = pd.read_csv(source_path)
        df["sentiment"] = df["overall"].apply(
            lambda x: 1 if x >= 3 else 0
        )  # convert overall to sentiment
        df = df.drop(columns=["overall"])
        df.to_csv(self.config.target_dir + "/sample_data.csv", index=False)
