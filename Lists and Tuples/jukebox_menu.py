from neested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exists):")

    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song:")

    for index, (track_number, song) in enumerate(songs_list):
        print(f"{index + 1}: {song}")

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print(f"Playing {title}")
    print("=" * 40)
