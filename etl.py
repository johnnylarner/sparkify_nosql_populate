from cassandra.cluster import Cluster
import pandas as pd
import os


def import_event_data():
    """
    Imports and returns compiled event data as DF.

    Raises:
    - FileNotFoundError if filepath wrong.
    """

    cwd = os.getcwd()
    event_filepath = cwd + "event_datafile_new.csv"

    if os.path.isfile(event_filepath):
        df = pd.read_csv(event_filepath)
        print("Event data found!")
        return df

    else:
        raise FileNotFoundError(
            f"No file found at path {event_filepath}" # Check CWD and file path
            )

def insert_event_data(df, session):
    """
    Inserts CSV data into tables in sparkifyks.

    Args:
    - df: DataFrame containing compiled event data.
    - session: Session object connected to sparfikyks.
    """

    for row in df.itertuples():
        pass