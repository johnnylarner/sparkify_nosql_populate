# CREATE KEYSPACE

create_keyspace_query = ("""
    CREATE KEYSPACE IF NOT EXISTS sparkifyks
    WITH REPLICATION =
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
""")
# CREATE TABLES

create_table1 = ("""

""")

create_table2 = ("""

""")

create_table3 = ("""

""")


# SELECT STATEMENTS FOR DATA VALIDATION
select_table1 = ("""

""")

select_table2 = ("""

""")

select_table3 = ("""

""")

# DROP TABLES
drop_table1 = ("""

""")

drop_table2 = ("""

""")

drop_table3 = ("""

""")

create_table_queries = [create_table1, create_table2, create_table3]

drop_table_queries = [drop_table1, drop_table2, drop_table2]