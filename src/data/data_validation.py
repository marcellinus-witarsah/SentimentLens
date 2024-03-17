import pandas as pd

from src.utils.common import logger
from src.entities.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        """
        Instantiate `DataValidation` class

        Args:
            config (DataValidationConfig): configuration for data ingestion
        """
        self.config = config

    def validate_data(self):
        """Extract `.zip` file"""
        try:
            logger.info("Validate data")
            validation_status = None

            df = pd.read_csv(self.config.source_path)
            all_cols = df.columns
            all_schema = self.config.schema

            for col in all_cols:
                if col not in all_schema.keys():
                    validation_status = False
                else:
                    if df[col].dtype == all_schema[col]:
                        validation_status = True
                    else:
                        validation_status = False

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"validation status: {validation_status}")
        except Exception as e:
            logger.error(e)
