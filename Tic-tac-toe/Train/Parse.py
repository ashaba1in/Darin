import random


def parse(start, end):
    dic = {'a': 1, 'b': 2,
           'c': 3, 'd': 4,
           'e': 5, 'f': 6,
           'g': 7, 'h': 8,
           'j': 9, 'k': 10,
           'l': 11, 'm': 12,
           'n': 13, 'o': 14,
           'p': 15, 'q': 16,
           'r': 17, 's': 18,
           't': 19, 'u': 20,
           'v': 21, 'w': 22,
           'x': 23, 'y': 24,
           'z': 25}

    path = 'C:/Users/renjucoach/Darin/train-1.renju'
    file = open(path, 'r')

    white = []
    black = []
    for k, line in enumerate(file):
        if k < start:
            continue
        if k > end:
            break

        game = line.split()
        if game[0] == 'draw':
            continue

        for i in range(1, len(game)):
            game[i] = (dic[game[i][0]], int(game[i][1:]))

        if len(set(game)) == len(game):
            if game[0] == 'white':
                white.append(game[1:])
            else:
                black.append(game[1:])

    return white, black


def all_parse(start, end):
    dic = {'a': 1, 'b': 2,
           'c': 3, 'd': 4,
           'e': 5, 'f': 6,
           'g': 7, 'h': 8,
           'j': 9, 'k': 10,
           'l': 11, 'm': 12,
           'n': 13, 'o': 14,
           'p': 15, 'q': 16,
           'r': 17, 's': 18,
           't': 19, 'u': 20,
           'v': 21, 'w': 22,
           'x': 23, 'y': 24,
           'z': 25}

    path = 'C:/Users/renjucoach/Darin/train-1.renju'
    file = open(path, 'r')

    data = []
    for k, line in enumerate(file):
        if k < start:
            continue
        if k > end:
            break

        game = line.split()
        if game[0] == 'draw':
            continue

        for i in range(1, len(game)):
            game[i] = (dic[game[i][0]], int(game[i][1:]))

        if len(set(game)) == len(game):
            data.append(game)

    return data

# 1984694 lines
