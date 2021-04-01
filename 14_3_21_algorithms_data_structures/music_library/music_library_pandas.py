import pandas as pd
from tabulate import tabulate


def print_to_table(x, cols=10):
    print(tabulate(x[:cols], headers='keys', tablefmt='pretty', stralign='left'))


def convert_seconds(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    if days > 0:
        return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(sec)} seconds"
    return f"{int(minutes)} minutes, {sec} seconds" if hours < 1 else f"{int(hours)} hours, {int(minutes)} minutes," \
                                                                      f" {int(sec)} seconds"


df = pd.read_csv('music_library.csv', encoding='utf-8')

############################################################################
# TODO 1: Find songs with most 'times played'
print("\n => TODO 1: Find songs with most 'times played'")
no_of_songs = 30
most_n_played_songs = df.nlargest(no_of_songs, 'Times played')
print_to_table(most_n_played_songs, cols=no_of_songs)

############################################################################
# TODO 2: Order songs by 'times played'
print("\n => TODO 2: Order songs by 'times played'")
df_sorted_by_times_played = df.sort_values(by='Times played', ascending=False)
print_to_table(df_sorted_by_times_played)

############################################################################
# TODO 3: Find songs with at least 1 like
print("\n => TODO 3: Find songs with at least 1 like")
songs_with_likes = df.query('Liked > 0')
print_to_table(songs_with_likes)  # Use 'cols=len(songs_with_likes)' to show all songs

############################################################################
# TODO 4: Calculate  total audition hours
print("\n => TODO 4: Calculate  total audition hours")
df['Play time'] = df['Duration'] * df['Times played']
total_play_time_in_sec = df['Play time'].sum()
total_play_time = convert_seconds(total_play_time_in_sec)
print(f"Total play time: {int(total_play_time_in_sec)} seconds or {total_play_time}.")

############################################################################
# TODO 5: Query the most listened music genre
print("\n => TODO 5: Query the most listened music genre")
play_time_by_genre = df.groupby("Gender/Type").sum().sort_values(by='Play time', ascending=False)
print_to_table(play_time_by_genre, cols=5)
most_popular_genre = play_time_by_genre.iloc[0].name.upper()
play_time_of_most_popular_genre = play_time_by_genre.iloc[0]['Play time']
print(f"{most_popular_genre} is the most listened music genre. Total play time:"
      f" {convert_seconds(play_time_of_most_popular_genre)}.")

############################################################################
# TODO 6: Calculate total duration of music library and find out what percentage of it was listened at least once
print("""\n => TODO 6: Calculate total duration of music library 
and find out what percentage of it was listened at least once\n""")
total_library_duration_in_sec = df['Duration'].sum()
total_library_duration = convert_seconds(total_library_duration_in_sec)

listened_songs = df[df['Times played'] > 0]
listened_songs_duration_in_sec = listened_songs['Duration'].sum()
listened_songs_duration = convert_seconds(listened_songs_duration_in_sec)

unlistened_songs = df[df['Times played'].isna()]
unlistened_songs_duration_in_sec = unlistened_songs['Duration'].sum()
unlistened_songs_duration = convert_seconds(unlistened_songs_duration_in_sec)

percent_of_listened_songs = round(listened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)
percent_of_unlistened_songs = round(unlistened_songs_duration_in_sec / total_library_duration_in_sec * 100, 2)

print(f'Total music library duration: {total_library_duration}.')
print(f'Total duration of songs listened at least once: {listened_songs_duration} -> {percent_of_listened_songs}%.')
print(f'Total duration of songs never listened: {unlistened_songs_duration} -> {percent_of_unlistened_songs}%.')
