# del data[0:2]
# print(data)
# del data[14:]
# print(data)


def low_values(data, min_valid):
    stop = 0

    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break

    del data[:stop]
    return data


def high_values(data, max_valid):
    start = 0

    for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_valid:
            start = index + 1
            break

    del data[start:]
    return data


if __name__ == "__main__":
    data = [
        4,
        5,
        104,
        105,
        110,
        120,
        130,
        130,
        150,
        160,
        170,
        183,
        185,
        187,
        188,
        191,
        350,
        360,
    ]

    # data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
    # data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
    # data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
    # create a list with 15 numeric items greater than 1000

    # data = list(range(1001, 1510, 50))
    # data = []

    min_valid = 100
    max_valid = 200

    low_values(data, min_valid)
    high_values(data, max_valid)
    print(data)
