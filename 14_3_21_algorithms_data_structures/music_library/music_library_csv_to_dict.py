import csv
import json
from tabulate import tabulate


# Get data from csv file and add each song information to a Python dictionary
music_library = dict()

with open('music_library.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    name, duration, artist, album, genre, liked, times_played = reader.__next__()
    for idx, song in enumerate(reader):
        music_library[idx] = {
                name: song[0], duration: int(song[1]), artist: song[2], album: song[3], genre: song[4],
                liked: int(song[5]), times_played: 0 if song[6] == "" else int(song[6])
        }


def convert_seconds(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    if days > 0:
        return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(sec)} seconds"
    return f"{int(minutes)} minutes, {sec} seconds" if hours < 1 else f"{int(hours)} hours, {int(minutes)} minutes," \
                                                                      f" {int(sec)} seconds"


def print_to_table(songs, cols=10):
    print(tabulate(songs[:cols], headers='keys', tablefmt='pretty', stralign='left'))


def display_song(song):
    print(f"\t-> '{song['Name']}' by {song['Artist']}. | Album: {song['Album']} | Genre: {song['Gender/Type']} "
          f"| Duration: {song['Duration']} | Times played: {song['Times played']}")


############################################################################
# TODO 1: Find songs with most 'times played'
print("\n => TODO 1: Find songs with most 'times played'")
max_play_times = max(song['Times played'] for song in music_library.values())
most_played_songs = [song for song in music_library.values() if song['Times played'] == max_play_times]
print_to_table(most_played_songs)

############################################################################
# TODO 2: Order songs by 'times played'
print("\n => TODO 2: Order songs by 'times played'")
print_to_table(sorted(music_library.values(), reverse=True, key=lambda x: x['Times played'])[:10])

############################################################################
# TODO 3: Find songs with at least 1 like
print("\n => TODO 3: Find songs with at least 1 like")
print_to_table([song for song in music_library.values() if song['Liked'] > 0])

############################################################################
# TODO 4: Calculate  total audition hours
print("\n => TODO 4: Calculate  total audition hours")
total_play_time = convert_seconds(
        sum([int(song['Duration'] * song['Times played']) for song in music_library.values()]))
print(f"Total play time: {total_play_time}.")

############################################################################
# TODO 5: Get the most listened music genre
print("\n => TODO 5: Get the most listened music genre")
play_time_by_genre = {}
for genre in set([song['Gender/Type'] for song in music_library.values()]):
    genre_play_time = sum(
            [(song['Duration'] * song['Times played']) for song in music_library.values() if song['Gender/Type'] ==
             genre])
    play_time_by_genre[genre] = genre_play_time
most_played_genre_duration = max(play_time_by_genre.values())
most_played_genre = [k for k, v in play_time_by_genre.items() if v == most_played_genre_duration][0].upper()
print(f"{most_played_genre} is the most listened music genre. Total play time:"
      f" {convert_seconds(most_played_genre_duration)}.")

############################################################################
# TODO 6: Calculate total duration of music library and find out what percentage of it was listened at least once
print("""\n => TODO 6: Calculate total duration of music library
and find out what percentage of it was listened at least once\n""")
total_library_duration_in_sec = sum([song['Duration'] for song in music_library.values()])
total_library_duration = convert_seconds(total_library_duration_in_sec)

listened_songs_duration_in_sec = sum([song['Duration'] for song in music_library.values() if song['Times played'] > 0])
listened_songs_duration = convert_seconds(listened_songs_duration_in_sec)

unlistened_songs_duration_in_sec = sum(
        [song['Duration'] for song in music_library.values() if not song['Times played']])
unlistened_songs_duration = convert_seconds(unlistened_songs_duration_in_sec)

percent_of_listened_songs = round(listened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)
percent_of_unlistened_songs = round(unlistened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)

print(f'Total music library duration: {total_library_duration}.')
print(f'Total duration of songs listened at least once: {listened_songs_duration} -> {percent_of_listened_songs}%.')
print(f'Total duration of songs never listened: {unlistened_songs_duration} -> {percent_of_unlistened_songs}%.')

# Save music library to a json file
with open('music_library.json', 'w') as output_file:
    json.dump(music_library, output_file, indent=4)
