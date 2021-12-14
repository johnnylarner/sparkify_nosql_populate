from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import pandas as pd
import os
from cql_queries import select_queries, insert_table1, insert_table2, insert_table3


def import_event_data():
    """
    Imports and returns compiled event data as DF.

    Raises:
    - FileNotFoundError if filepath wrong.
    """

    cwd = os.getcwd()
    event_filepath = cwd + "/event_datafile_new.csv"

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
    num_rows = df.shape[0]

    row_num = 1
    for row in df.itertuples():

        vals = (
            row.sessionId, row.itemInSession,
            row.artist, row.song, row.length
        )
        session.execute(insert_table1, vals)

        vals = (
            row.userId, row.sessionId, row.itemInSession,
            row.artist, row.song, row.firstName, row.lastName
        )
        session.execute(insert_table2, vals)

        vals = (
            row.song, row.firstName, row.lastName
        )
        session.execute(insert_table3, vals)

        print(f"{row_num}/{num_rows} rows processed!")
        row_num += 1

def test_queries(session):
    """
    Fetches results of test queries and displays them in CLI.
    """
    query_num = 1
    for q in select_queries:
        rows = session.execute(q)
        print(f"\nRESULTS FOR QUERY {query_num}\n")
        for r in rows.all():
            print(r)

        query_num += 1
        if query_num > 3:
            print("\nNo more query results\n")
            break
        inp = input("\nEnter anything to see the next query results\n")


if __name__ == "__main__":
    try:
        cluster = Cluster(["127.0.0.1"])
        session = cluster.connect() 
        print("Connected!")

    except Exception as e:
        print(e)

    try:
        session.set_keyspace("sparkifyks")
        session.row_factory = dict_factory # for printing
    
    except Exception as e:
         print(e)

    data = import_event_data()
    insert_event_data(data, session)
    test_queries(session)
    session.shutdown()
    cluster.shutdown()