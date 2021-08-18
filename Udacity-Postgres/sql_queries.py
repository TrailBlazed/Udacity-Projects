# DROP TABLES

songplay_table_drop = "Drop table if exists songplays "
user_table_drop = "Drop table if exists users"
song_table_drop = "Drop table if exists songs"
artist_table_drop = "Drop table if exists artists"
time_table_drop = "Drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (songplay_id int,start_time bigint,user_id int,level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)""")


user_table_create = ("""Create table users (user_id int, first_name varchar, last_name varchar, gender varchar(1), level varchar)""")

song_table_create = ("""Create table songs(song_id varchar, title varchar, artist_id varchar, year int, duration double precision)""")
 
artist_table_create =(""" create table artists(artist_id varchar, name varchar, location varchar, latitude double precision, longitude double precision)""")

time_table_create = ("""create table time(start_time BIGINT, hour int, day int, week int, month int, year int, weekday int)""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays(songplay_id ,start_time ,user_id ,level , song_id , artist_id , session_id , location , user_agent ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""insert into users(user_id, first_name, last_name, gender, level) values(%s,%s,%s,%s,%s)""")

song_table_insert = ("""insert into songs(song_id, title, artist_id, year, duration) values (%s,%s,%s,%s,%s)""")

artist_table_insert = ("""insert into artists(artist_id, name, location, latitude, longitude ) values (%s,%s,%s,%s,%s)""")


time_table_insert = ("""insert into time(start_time, hour, day, week, month, year, weekday)values (%s,%s,%s,%s,%s,%s,%s) """)

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id
    FROM songs s
    JOIN artists a ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND s.duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
