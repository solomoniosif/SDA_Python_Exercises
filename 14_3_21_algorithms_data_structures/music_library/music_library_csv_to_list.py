import csv


# Get data from csv file and add each song information to a Python list
music_library = list()

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
        music_library.append([name, duration, artist, album, genre, liked, times_played])


def convert_seconds(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    if days > 0:
        return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(sec)} seconds"
    return f"{int(minutes)} minutes, {sec} seconds" if hours < 1 else f"{int(hours)} hours, {int(minutes)} minutes," \
                                                                      f" {int(sec)} seconds"


def display_song(raw_song):
    name = raw_song[0]
    duration = convert_seconds(raw_song[1])
    artist = raw_song[2]
    album = raw_song[3]
    genre = raw_song[4]
    liked = int(raw_song[5])
    times_played = raw_song[6]
    play_time = int(times_played * raw_song[1])
    total_play_time = convert_seconds(play_time)
    print(
            f"\t-> '{name}' by {artist}. | Album: {album} | Genre: {genre} | Duration: {duration} | "
            f"Times played: {times_played}")
    # Likes: {liked} | Total play time: {total_play_time}


############################################################################
# TODO 1: Find songs with most 'times played'
print("\n => TODO 1: Find songs with most 'times played'")
max_play_times = max([0 if song[6] == "" else int(song[6]) for song in music_library])
most_played_songs = [song for song in music_library if song[6] == max_play_times]
for song in most_played_songs:
    display_song(song)

############################################################################
# TODO 2: Order songs by 'times played'
print("\n => TODO 2: Order songs by 'times played'")
for song in sorted(music_library, reverse=True, key=lambda x: x[6])[:10]:
    display_song(song)

############################################################################
# TODO 3: Find songs with at least 1 like
print("\n => TODO 3: Find songs with at least 1 like")
songs_with_likes = [song for song in music_library if song[5] > 0]
for song in songs_with_likes[:10]:
    display_song(song)

############################################################################
# TODO 4: Calculate  total audition hours
print("\n => TODO 4: Calculate  total audition hours")
total_play_time = convert_seconds(sum([int(song[6] * song[1]) for song in music_library]))
print(f"Total play time: {total_play_time}.")

############################################################################
# TODO 5: Get the most listened music genre
print("\n => TODO 5: Get the most listened music genre")
play_time_by_genre = {}
for genre in set([song[4] for song in music_library]):
    genre_play_time = sum(
            [int(song[6] * song[1]) for song in music_library if song[4] == genre])
    play_time_by_genre[genre] = genre_play_time
most_played_genre_duration = max(play_time_by_genre.values())
most_played_genre = \
    [k for k, v in play_time_by_genre.items() if v == most_played_genre_duration][
        0].upper()
print(f"{most_played_genre} is the most listened music genre. Total play time:"
      f" {convert_seconds(most_played_genre_duration)}.")

############################################################################
# TODO 6: Calculate total duration of music library and find out what percentage of it was listened at least once
print("""\n => TODO 6: Calculate total duration of music library
and find out what percentage of it was listened at least once\n""")
total_library_duration_in_sec = sum([song[1] for song in music_library])
total_library_duration = convert_seconds(total_library_duration_in_sec)

listened_songs_duration_in_sec = sum([song[1] for song in music_library if song[6] > 0])
listened_songs_duration = convert_seconds(listened_songs_duration_in_sec)

unlistened_songs_duration_in_sec = sum([song[1] for song in music_library if not song[6]])
unlistened_songs_duration = convert_seconds(unlistened_songs_duration_in_sec)

percent_of_listened_songs = round(
        listened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)
percent_of_unlistened_songs = round(
        unlistened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)

print(f'Total music library duration: {total_library_duration}.')
print(
        f'Total duration of songs listened at least once: {listened_songs_duration} -> {percent_of_listened_songs}%.')
print(
        f'Total duration of songs never listened: {unlistened_songs_duration} -> {percent_of_unlistened_songs}%.')
