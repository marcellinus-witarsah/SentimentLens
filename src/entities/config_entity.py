from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_path: Path
    target_dir: Path


@dataclass(frozen=True)
class DataLabelingConfig:
    root_dir: Path
    source_path: Path
    target_dir: Path