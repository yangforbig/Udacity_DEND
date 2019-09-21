# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplay (songplaykey SERIAL primary key, songplay_id varchar NOT NULL CONSTRAINT songplaykey primary key, start_time timestamp, user_id int, level varchar, artist_id int, session_id int, location varchar, user_agent varchar)
""")

user_table_create = (""" CREATE TABLE users (user_id varchar CONSTRAINT userkey primary key, first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = (""" CREATE TABLE song (song_id varchar CONSTRAINT songkey primary key, title varchar, year int, artist_id varchar, duration decimal(10,5))
""")

artist_table_create = (""" CREATE TABLE artist(artist_id varchar CONSTRAINT artistkey primary key, name varchar, location varchar, lattitude varchar, longitude varchar)
""")

time_table_create = (""" CREATE TABLE time(start_time timestamp CONSTRAINT timekey primary key, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplay (songplay_id, start_time, user_id, level, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT userkey 
DO NOTHING""")

song_table_insert = (""" INSERT INTO song (song_id, title, year, artist_id, duration ) VALUES (%s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT songkey 
DO NOTHING
""")

artist_table_insert = (""" INSERT INTO artist (artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT artistkey 
DO NOTHING
""")


time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT timekey 
DO NOTHING
""")

# FIND SONGS

song_select = (""" SELECT s.song_id,a.artist_id FROM song AS s join artist as a on s.artist_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
