from numpy import zeros
from collections import Counter
'''
depth: 5913
target: 8,701
'''
'''
RAW:
depth: 510
target: 10, 10
'''
DEPTH = 5913
TARGET = (8, 701)

test = zeros((2, 5))

def get_erosion_level(x, y, map):
    geologic_idx = 0
    if x == 0 or y == 0:
        if x == 0:
            geologic_idx = y * 48271
        elif y == 0:
            geologic_idx = x * 16807
    else:
        geologic_idx = map[y][x - 1] * map[y-1][x]
    erosion_level = ((geologic_idx + DEPTH) % 20183)
    return erosion_level

def generate_map(Y, X):
    map = zeros((Y + 1, X + 1))
    return map

def get_risk_level(map, Y, X):
    for y in range(Y + 1):
        for x in range(X + 1):
            map[y][x] = get_erosion_level(x, y, map)
            if y == Y and x == X:
                map[y][x] = 0

    risk_level = 0
    for y in range(Y + 1):
        for x in range(X + 1):
            map[y][x] = ((map[y][x] + DEPTH)) % 3

            risk_level += map[y][x]
    return risk_level

def visualize(map, Y, X):
    for y in range(Y + 1):
        for x in range(X + 1):
            if x == 0 and y == 0:
                print('M', end='')
            elif x == X and y == Y:
                print('T', end='')
            elif map[y][x] == 0:
                print('.', end='')
            elif map[y][x] == 1:
                print('=', end='')
            else:
                print('|', end='')
        print()


def main():
    map = generate_map(TARGET[1], TARGET[0])
    print('Risk level:', int(get_risk_level(map, TARGET[1], TARGET[0])))
    visualize(map, TARGET[1], TARGET[0])

if __name__ == "__main__":
    main()
