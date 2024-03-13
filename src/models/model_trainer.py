import os
import sys
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.entities.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        """
        Instantiate `ModelTrainer` class

        Args:
            config (ModelTrainerConfig): Configuration for model training
        """
        self.config = config

    def train(self):
        """
        Train and save model
        """
        logger.info("Train model")
        train = pd.read_csv(self.config.train_data_path)

        X_train = (
            train.drop(columns=[self.config.target_column], axis=1)
            .to_numpy()
            .reshape(-1)
        )
        y_train = train[self.config.target_column].to_numpy().reshape(-1)
        model = Pipeline(
            [
                ("CountVectorizer", CountVectorizer()),
                ("MultinomialNB", MultinomialNB(**self.config.model_params)),
            ]
        )
        model.fit(X_train, y_train)
        logger.info("Save model")
        joblib.dump(model, self.config.root_dir / self.config.model_name)
