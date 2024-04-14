from neested_data import albums

SONGS_LIST_INDEX = 3

while True:
    print("Please choose your album (invalid choice exists):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print(albums[choice - 1])
    print(songs_list)
