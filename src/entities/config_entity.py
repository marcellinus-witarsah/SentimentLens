from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_path: Path
    target_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    source_path: Path
    STATUS_FILE: Path
    schema: list


@dataclass(frozen=True)
class DataLabelingConfig:
    root_dir: Path
    source_path: Path
    target_dir: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    source_path: Path
    cleaned_data_path: Path
    transformed_data_path: Path
    train_data_path: Path
    test_data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    model_params: dict
    target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    model_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str
