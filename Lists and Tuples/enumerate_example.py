# for index, character in enumerate("abcdefgh"):
#     print(f"{index}: {character}")

for t in enumerate("abcdefgh"):
    print(t)  # t is a tuple

for t in enumerate("abcdefgh"):
    index, character = t  # unpacking a tuple
    print(f"{index}: {character}")
