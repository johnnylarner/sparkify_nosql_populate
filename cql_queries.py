# CREATE KEYSPACE

create_keyspace_query = ("""
    CREATE KEYSPACE IF NOT EXISTS sparkifyks
    WITH REPLICATION =
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
""")
# CREATE TABLES

create_table1 = ("""
        CREATE TABLE IF NOT EXISTS table1
        (
            session_id int,
            item_in_session int,
            artist text,
            song_title text,
            song_length float,
            PRIMARY KEY (session_id, item_in_session)
        );
""")

create_table2 = ("""

        CREATE TABLE IF NOT EXISTS table2
        (
            user_id int,
            session_id int,
            item_in_session int,
            artist text,
            song_title text,
            user_first_name text,
            user_last_name text,
            PRIMARY KEY (user_id, session_id, item_in_session)
        );

""")

create_table3 = ("""

        CREATE TABLE IF NOT EXISTS table3
        (
            song_title text,
            user_first_name text,
            user_last_name text,
            PRIMARY KEY (song_title, user_first_name, user_last_name)
        );

""")

# INSERT STATEMENTS

insert_table1 = ("""
INSERT INTO table1 (
    session_id,
    item_in_session,
    artist,
    song_title,
    song_length
)
VALUES (%s, %s, %s, %s, %s);

""")

insert_table2 = ("""
INSERT INTO table2 (
    user_id,
    session_id,
    item_in_session,
    artist,
    song_title,
    user_first_name,
    user_last_name
)
VALUES (%s, %s, %s, %s, %s, %s, %s);

""")

insert_table3 = ("""
INSERT INTO table3 (
    song_title,
    user_first_name,
    user_last_name
)
VALUES (%s, %s, %s);

""")

# SELECT STATEMENTS FOR DATA VALIDATION
select_table1 = ("""
SELECT artist, song_title, song_length FROM table1 WHERE session_id = 338 AND item_in_session = 4;
""")

select_table2 = ("""
SELECT artist, song_title, user_first_name, user_last_name FROM table2 WHERE user_id = 10 AND session_id = 182;
""")

select_table3 = ("""
SELECT * FROM table3 WHERE song_title = 'All Hands Against His Own';
""")

# DROP TABLES
drop_table1 = ("""
    DROP TABLE IF EXISTS table1;
""")

drop_table2 = ("""
    DROP TABLE IF EXISTS table2;
""")

drop_table3 = ("""
    DROP TABLE IF EXISTS table3;
""")

create_table_queries = [create_table1, create_table2, create_table3]
select_queries = [select_table1, select_table2, select_table3]
drop_table_queries = [drop_table1, drop_table2, drop_table3]