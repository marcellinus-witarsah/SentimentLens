from src.utils.common import logger
from src.config.configuration import ConfigurationManager
from src.data.data_validation import DataValidation


class DataValidationTrainingPipeline:
    def __init__(self):
        """
        Instantiate `DataValidationTrainingPipeline` class
        """
        self.configuration_manager = ConfigurationManager()

    def run(self):
        """
        Ingest data
        """
        data_validation = DataValidation(
            config=self.configuration_manager.get_data_validation_config()
        )
        data_validation.validate_data()


if __name__ == "__main__":
    STAGE_NAME = "Data validation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_validation_training_pipeline = DataValidationTrainingPipeline()
        data_validation_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)
