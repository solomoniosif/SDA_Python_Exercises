from collections import namedtuple
import csv
from tabulate import tabulate
from rich.console import Console


Song = namedtuple('Song', 'name, duration, artist, album, genre, liked, times_played')

music_library = []

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
        nt_song = Song(name, duration, artist, album, genre, liked, times_played)
        music_library.append(nt_song)


def convert_seconds(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    if days > 0:
        return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(sec)} seconds"
    return f"{int(minutes)} minutes, {sec} seconds" if hours < 1 else f"{int(hours)} hours, {int(minutes)} minutes," \
                                                                      f" {int(sec)} seconds"


def rich_print(input_string, style='bold red'):
    console = Console()
    console.print(input_string, style=style, highlight=False)


def print_to_table(songs, cols=10):
    rich_print(tabulate(songs[:cols], headers='keys', tablefmt='pretty', stralign='left'), style='bold')


############################################################################
# TODO 1: Find songs with most 'times played'
rich_print("\n => TODO 1: Find songs with most 'times played'")
max_play_times = max(s.times_played for s in music_library)
most_played_songs = [s for s in music_library if s.times_played == max_play_times]
print_to_table(most_played_songs)

############################################################################
# TODO 2: Order songs by 'times played'
rich_print("\n => TODO 2: Order songs by 'times played'")
print_to_table(sorted(music_library, reverse=True, key=lambda x: x.times_played)[:10])

############################################################################
# TODO 3: Find songs with at least 1 like
rich_print("\n => TODO 3: Find songs with at least 1 like")
print_to_table([s for s in music_library if s.liked > 0])

############################################################################
# TODO 4: Calculate  total audition hours
rich_print("\n => TODO 4: Calculate  total audition hours")
total_play_time = convert_seconds(sum([s.duration * s.times_played for s in music_library]))
print(f"Total play time: {total_play_time}.")

############################################################################
# TODO 5: Get the most listened music genre
rich_print("\n => TODO 5: Get the most listened music genre")
play_time_by_genre = {}
for genre in set([s.genre for s in music_library]):
    genre_play_time = sum([s.duration * s.times_played for s in music_library if s.genre == genre])
    play_time_by_genre[genre] = genre_play_time
most_played_genre_duration = max(play_time_by_genre.values())
most_played_genre = [k for k, v in play_time_by_genre.items() if v == most_played_genre_duration][0].upper()
print(f"{most_played_genre} is the most listened music genre. Total play time:"
      f" {convert_seconds(most_played_genre_duration)}.")

############################################################################
# TODO 6: Calculate total duration of music library and find out what percentage of it was listened at least once
rich_print("""\n => TODO 6: Calculate total duration of music library
and find out what percentage of it was listened at least once\n""")
total_library_duration_in_sec = sum([s.duration for s in music_library])
total_library_duration = convert_seconds(total_library_duration_in_sec)

listened_songs_duration_in_sec = sum([s.duration for s in music_library if s.times_played > 0])
listened_songs_duration = convert_seconds(listened_songs_duration_in_sec)

unlistened_songs_duration_in_sec = sum([s.duration for s in music_library if not s.times_played])
unlistened_songs_duration = convert_seconds(unlistened_songs_duration_in_sec)

percent_of_listened_songs = round(listened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)
percent_of_unlistened_songs = round(unlistened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)

print(f'Total music library duration: {total_library_duration}.')
print(f'Total duration of songs listened at least once: {listened_songs_duration} -> {percent_of_listened_songs}%.')
print(f'Total duration of songs never listened: {unlistened_songs_duration} -> {percent_of_unlistened_songs}%.')
