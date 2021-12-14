from cassandra import cluster
from cassandra.cluster import Cluster
from cql_queries import create_keyspace_query, create_table_queries, drop_table_queries


def create_keyspace():
    """
    Create keyspace if not exitsts.
    """
    
    try:
        cluster = Cluster(["127.0.0.1"])
        session = cluster.connect() 
        print("Connected!")

    except Exception as e:
        print(e)

    try:
        session.execute(create_keyspace_query)
        session.set_keyspace("sparkifyks")
    
    except Exception as e:
         print(e)

    return session, cluster

def create_tables(session):
    """
    Drops and then creates tables in sparkify keyspace.
    """

    for q in drop_table_queries:
        try:
            session.execute(q)
        
        except Exception as e:
            print(e)

    for q in create_table_queries:
        
        try:
            session.execute(q)

        except Exception as e:
            print(e)

    print("Tables created!")


if __name__ == "__main__":
    
    session, clus = create_keyspace
    create_tables(session)
    session.shutdown()
    clus.shutdown()

