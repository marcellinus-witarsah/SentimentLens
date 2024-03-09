import os
import sys
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.utils.common import read_yaml, create_directories
from src.entities.config_entity import DataIngestionConfig
from src.entities.config_entity import DataValidationConfig
from src.entities.config_entity import DataLabelingConfig
from src.entities.config_entity import DataTransformationConfig
from src.entities.config_entity import ModelTrainerConfig
from src.entities.config_entity import ModelEvaluationConfig


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
            root_dir=config.root_dir,
            source_path=config.source_path,
            target_dir=config.target_dir,
        )
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Get configuration for data validation

        Returns:
            DataValidationConfig: Configuration for data validation
        """
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            source_path=config.source_path,
            STATUS_FILE=config.STATUS_FILE,
            schema=schema,
        )
        return data_validation_config

    def get_data_labeling_config(self) -> DataLabelingConfig:
        """
        Get configuration for data labeling

        Returns:
            DataLabelingConfig: Configuration for data labeling
        """
        config = self.config.data_labeling

        create_directories([config.root_dir])

        data_labeling_config = DataLabelingConfig(
            root_dir=config.root_dir,
            source_path=config.source_path,
            target_dir=config.target_dir,
        )
        return data_labeling_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Get configuration for data transformation

        Returns:
            DataTransformationConfig: Configuration for data transformation
        """
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            source_path=config.source_path,
            cleaned_data_path=config.cleaned_data_path,
            transformed_data_path=config.transformed_data_path,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Get configuration for model training

        Returns:
            ModelEvaluationConfigModelTrainerConfig: Configuration for model training
        """
        config = self.config.model_trainer
        params = self.params.MultinomialNB
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            model_name=config.model_name,
            model_params=params,
            target_column=schema.name,
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Get configuration for model evaluation

        Returns:
            ModelEvaluationConfig: Configuration for model training
        """
        config = self.config.model_evaluation
        params = self.params.MultinomialNB
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            test_data_path=Path(config.test_data_path),
            model_path=Path(config.model_path),
            model_params=params,
            metric_file_name=Path(config.metric_file_name),
            target_column=schema.name,
            mlflow_uri=os.getenv("MLFLOW_TRACKING_URI"),
        )

        return model_evaluation_config
