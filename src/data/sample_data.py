# -*- coding: utf-8 -*-
import os
import sys
import click
import logging
import pandas as pd
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.utils.common import parse
from src.utils.common import get_data_frame


@click.command()
@click.argument("input_folder", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_folder, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    df = pd.DataFrame({})
    for path in Path(input_folder).glob("*.gz"):
        logger.info(f"Load {path} ...")
        temp = get_data_frame(path)  # load .gz type data
        df = pd.concat([df, temp])

    logger.info(f"Sample data")
    df = df.groupby("overall").sample(
        5000, replace=True, random_state=42
    )  # Sample data

    df.to_csv(output_filepath, index=False)
    logger.info(f"Save data to {output_filepath}")


if __name__ == "__main__":
    main()
