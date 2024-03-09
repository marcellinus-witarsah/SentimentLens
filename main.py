import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.pipelines.data_ingestion import DataIngestionTrainingPipeline
from src.pipelines.data_validation import DataValidationTrainingPipeline
from src.pipelines.data_labeling import DataLabelingTrainingPipeline
from src.pipelines.data_transformation import DataTransformationTrainingPipeline
from src.pipelines.model_trainer import ModelTrainerTrainingPipeline
from src.pipelines.model_evaluation import ModelEvaluationTrainingPipeline

if __name__ == "__main__":
    STAGE_NAME = "Data ingestion stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)

    STAGE_NAME = "Data validation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_validation_training_pipeline = DataValidationTrainingPipeline()
        data_validation_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)

    STAGE_NAME = "Data labeling stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_labeling_training_pipeline = DataLabelingTrainingPipeline()
        data_labeling_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)

    STAGE_NAME = "Data transformation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_transformation_training_pipeline = DataTransformationTrainingPipeline()
        data_transformation_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)

    STAGE_NAME = "Model training stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        model_trainer_training_pipeline = ModelTrainerTrainingPipeline()
        model_trainer_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)

        STAGE_NAME = "Model training stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        model_evaluation_training_pipeline = ModelEvaluationTrainingPipeline()
        model_evaluation_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)
