# CREATE KEYSPACE

create_keyspace_query = ("""
    CREATE KEYSPACE IF NOT EXISTS sparkifyks
    WITH REPLICATION =
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
""")
# CREATE TABLES

create_songs_per_session = ("""
        CREATE TABLE IF NOT EXISTS songs_per_session
        (
            session_id int,
            item_in_session int,
            artist text,
            song_title text,
            song_length float,
            PRIMARY KEY (session_id, item_in_session)
        );
""")

create_songs_per_user_session = ("""

        CREATE TABLE IF NOT EXISTS songs_per_user_session
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

create_songs_per_user = ("""

        CREATE TABLE IF NOT EXISTS songs_per_user
        (
            song_title text,
            user_first_name text,
            user_last_name text,
            PRIMARY KEY (song_title, user_first_name, user_last_name)
        );

""")

# INSERT STATEMENTS

insert_songs_per_session = ("""
INSERT INTO songs_per_session (
    session_id,
    item_in_session,
    artist,
    song_title,
    song_length
)
VALUES (%s, %s, %s, %s, %s);

""")

insert_songs_per_user_session = ("""
INSERT INTO songs_per_user_session (
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

insert_songs_per_user= ("""
INSERT INTO songs_per_user (
    song_title,
    user_first_name,
    user_last_name
)
VALUES (%s, %s, %s);

""")

# SELECT STATEMENTS FOR DATA VALIDATION
select_songs_per_session = ("""
SELECT artist, song_title, song_length FROM songs_per_session WHERE session_id = 338 AND item_in_session = 4;
""")

select_songs_per_user_session = ("""
SELECT artist, song_title, user_first_name, user_last_name FROM songs_per_user_session WHERE user_id = 10 AND session_id = 182;
""")

select_songs_per_user = ("""
SELECT * FROM songs_per_user WHERE song_title = 'All Hands Against His Own';
""")

# DROP TABLES
drop_songs_per_session = ("""
    DROP TABLE IF EXISTS songs_per_session;
""")

drop_songs_per_user_session = ("""
    DROP TABLE IF EXISTS songs_per_user_session;
""")

drop_songs_per_user = ("""
    DROP TABLE IF EXISTS songs_per_user;
""")

create_table_queries = [create_songs_per_session, create_songs_per_user_session, create_songs_per_user]
select_queries = [select_songs_per_session, select_songs_per_user_session, select_songs_per_user]
drop_table_queries = [drop_songs_per_session, drop_songs_per_user_session, drop_songs_per_user]