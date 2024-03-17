import string
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split

from src.utils.common import logger
from src.entities.config_entity import DataTransformationConfig

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        """
        Instantiate `DataTransformation` class

        Args:
            config (DataTransformationConfig): configuration for data transformation
        """
        self.stopwords_en = stopwords.words("english")
        self.punctuations = string.punctuation
        self.lemmatizer = WordNetLemmatizer()
        self.config = config

    def clean_data(self):
        """
        Clean data
        """
        logger.info(f"Clean data")
        df = pd.read_csv(self.config.source_path)
        df = df.drop_duplicates()  # drop duplicates
        df = df.dropna(
            subset=["reviewText"], axis=0
        )  # drop missing `reviewText` columns
        df = df[["reviewText", "sentiment"]]  # select columns
        df = df.reset_index(drop=True)  # reset index
        df.to_csv(self.config.cleaned_data_path, index=False)

    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text

        Args:
            text (str): Raw text
        Returns:
            str: Preprocessed text
        """
        tokens = word_tokenize(
            text.lower()
        )  # normalize, remove punctuations, and tokenize text
        filtered_tokens = [
            token
            for token in tokens
            if token not in self.stopwords_en and token not in self.punctuations
        ]  # filter stop words
        lemmatized_tokens = [
            self.lemmatizer.lemmatize(token) for token in filtered_tokens
        ]  # lemmatize words
        return " ".join(lemmatized_tokens)  # Join the tokens back into a string

    def preprocess_texts(self):
        """
        Preprocess all texts
        """
        logger.info(f"Preprocess text data")
        df = pd.read_csv(self.config.cleaned_data_path)
        df["preprocessed_review_text"] = df["reviewText"].apply(
            self.preprocess_text
        )  # text preprocessing
        df = df[
            (df["preprocessed_review_text"].apply(lambda x: len(x)) != 0)
        ]  # remove 0 length preprocess text
        df = df[
            ["preprocessed_review_text", "sentiment"]
        ]  # select columns for model training
        df.to_csv(self.config.transformed_data_path, index=False)

    def split_data(self):
        """
        Split data into train and test set
        """
        logger.info(f"Split data")
        df = pd.read_csv(self.config.transformed_data_path)
        X, y = df[["preprocessed_review_text"]], df[["sentiment"]]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, stratify=y, test_size=0.2, shuffle=True, random_state=42
        )
        train = pd.concat([X_train, y_train], axis=1)
        test = pd.concat([X_test, y_test], axis=1)
        train.to_csv(self.config.train_data_path, index=False)
        test.to_csv(self.config.test_data_path, index=False)
