import sqlite3
import csv
from tabulate import tabulate


conn = sqlite3.connect('music_library.db')
c = conn.cursor()

create_table_stmt = '''CREATE TABLE IF NOT EXISTS library
        (name TEXT NOT NULL,
         duration INT NOT NULL,
         artist TEXT,
         album TEXT,
         genre TEXT,
         liked INT,
         times_played INT);'''

c.execute(create_table_stmt)


def csv_to_db():
    with open('music_library.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        reader.__next__()  # Skip the first line in csv file
        for song in reader:
            name = song[0]
            duration = int(song[1])
            artist = song[2]
            album = song[3]
            genre = song[4]
            liked = int(song[5])
            times_played = 0 if song[6] == "" else int(song[6])
            sql = '''
            INSERT INTO library (name, duration, artist, album, genre, liked, times_played) VALUES (?,?,?,?,?,?,?)'''
            c.execute(sql, (name, duration, artist, album, genre, liked, times_played))
            conn.commit()


# csv_to_db()

def convert_seconds(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    if days > 0:
        return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(sec)} seconds"
    return f"{int(minutes)} minutes, {sec} seconds" if hours < 1 else f"{int(hours)} hours, {int(minutes)} minutes," \
                                                                      f" {int(sec)} seconds"


def print_to_table(songs, cols=10, headers=('Name', 'Artist', 'Album', 'Times Played')):
    print(tabulate(songs[:cols], headers=headers, tablefmt='pretty', stralign='left'))


############################################################################
# TODO 1: Find songs with most 'times played'
print("\n => TODO 1: Find songs with most 'times played'")
max_play_times = c.execute("SELECT MAX(times_played) FROM library").fetchone()[0]
most_played_song = c.execute("SELECT name, artist, album, times_played FROM library WHERE times_played = ?",
                             (max_play_times,)).fetchone()
print(tabulate([most_played_song], headers=('Name', 'Artist', 'Album', 'Times played'), tablefmt='pretty',
               stralign='left'))

############################################################################
# TODO 2: Order songs by 'times played'
print("\n => TODO 2: Order songs by 'times played'")
ordered_by_times_played = c.execute("SELECT name, artist, album, times_played FROM library ORDER BY times_played DESC")
print_to_table(ordered_by_times_played.fetchmany(10))

############################################################################
# TODO 3: Find songs with at least 1 like
print("\n => TODO 3: Find songs with at least 1 like")
songs_with_likes = c.execute("SELECT name, artist, album, liked, times_played FROM library WHERE liked > 0")
songs_to_show = 20
print_to_table(songs_with_likes.fetchmany(songs_to_show), cols=songs_to_show,
               headers=('Name', 'Artist', 'Album', 'Liked', 'Times Played'))

############################################################################
# TODO 4: Calculate  total audition hours
print("\n => TODO 4: Calculate  total audition hours")
total_play_time = c.execute("SELECT duration, times_played FROM library")
total_play_time = convert_seconds(sum([s[0] * s[1] for s in total_play_time.fetchall()]))
print(f"Total play time: {total_play_time}.")

############################################################################
# TODO 5: Get the most listened music genre
print("\n => TODO 5: Get the most listened music genre")
play_time_by_genre = c.execute(
        "SELECT genre, play_time FROM (SELECT genre, duration*times_played AS play_time FROM library) GROUP BY genre "
        "ORDER BY play_time DESC")
most_played_genres = play_time_by_genre.fetchall()
print_to_table(most_played_genres, headers=('Genre', 'Play Time'))
x_genre, x_playtime = most_played_genres[0]
print(f"{x_genre} is the most listened music genre. Total play time: {convert_seconds(x_playtime)}.")

############################################################################
# TODO 6: Calculate total duration of music library and find out what percentage of it was listened at least once
print("""\n => TODO 6: Calculate total duration of music library
and find out what percentage of it was listened at least once\n""")
total_library_duration_in_sec = c.execute("SELECT SUM(duration) FROM library")
total_library_duration_in_sec = total_library_duration_in_sec.fetchone()[0]
total_library_duration = convert_seconds(total_library_duration_in_sec)

listened_songs_duration_in_sec = c.execute("SELECT SUM(duration) FROM library WHERE times_played > 0")
listened_songs_duration_in_sec = listened_songs_duration_in_sec.fetchone()[0]
listened_songs_duration = convert_seconds(listened_songs_duration_in_sec)

unlistened_songs_duration_in_sec = c.execute("SELECT SUM(duration) FROM library WHERE times_played = 0")
unlistened_songs_duration_in_sec = unlistened_songs_duration_in_sec.fetchone()[0]
unlistened_songs_duration = convert_seconds(unlistened_songs_duration_in_sec)

percent_of_listened_songs = round(listened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)
percent_of_unlistened_songs = round(unlistened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)

print(f'Total music library duration: {total_library_duration}.')
print(f'Total duration of songs listened at least once: {listened_songs_duration} -> {percent_of_listened_songs}%.')
print(f'Total duration of songs never listened: {unlistened_songs_duration} -> {percent_of_unlistened_songs}%.')
