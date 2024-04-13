# t = ("a", "b", "c")
# print(type(t))

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]

# print(len(albums))

for name, artist, year in albums:
    print(f"Album: {name}, Artist: {artist}, Year: {year}")

# for album in albums:
#     Album, Artist, Year = album
#     print(f"Album: {Album}, Artist: {Artist}, Year: {Year}")

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)

# table = ("Coffee table", 200, 100, 75, 34.50)
# # print(table[1] * table[2])
# # not very readable

# name, length, width, height, price = table  # unpacking the tuple
# print(length * width)


# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
# print()

# # metallica[0] = "Master of Puppets"
# # tuples uses less memory than lists
# # tuples protect the intergrity of our data

# metallica2 = list(metallica)
# print(metallica2)

# metallica2[0] = "Master of Puppets"
# print(metallica2)
