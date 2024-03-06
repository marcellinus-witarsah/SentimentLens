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
