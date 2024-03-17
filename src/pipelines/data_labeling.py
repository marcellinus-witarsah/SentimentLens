from src.utils.common import logger
from src.config.configuration import ConfigurationManager
from src.data.data_labeling import DataLabeling


class DataLabelingTrainingPipeline:
    def __init__(self):
        """
        Instantiate `DataLabelingTrainingPipeline` class
        """
        self.configuration_manager = ConfigurationManager()

    def run(self):
        """
        Ingest data
        """
        data_labeling = DataLabeling(
            config=self.configuration_manager.get_data_labeling_config()
        )
        data_labeling.label_data()


if __name__ == "__main__":
    STAGE_NAME = "Data labeling stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_labeling_training_pipeline = DataLabelingTrainingPipeline()
        data_labeling_training_pipeline.run()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.error(e)
