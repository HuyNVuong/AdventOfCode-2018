from collections import Counter
from typing import List
from copy import deepcopy
class Point:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point {} : ({}, {})'.format(self.type, self.x, self.y)


def count_living_neighbors(board, point, size):
    livingNeigbors = Counter()

    leftBorder = (point.x == 0)
    rightBorder = (point.x == size - 1)
    topBorder = (point.y == 0)
    bottomBorder = (point.y == size - 1)

    if topBorder:
        if leftBorder:
            livingNeigbors[board[point.y][point.x + 1]] += 1
            livingNeigbors[board[point.y + 1][point.x + 1]] += 1
            livingNeigbors[board[point.y + 1][point.x]] += 1
        elif rightBorder:
            livingNeigbors[board[point.y][point.x - 1]] += 1
            livingNeigbors[board[point.y - 1][point.x - 1]] += 1
            livingNeigbors[board[point.y - 1][point.x]] += 1
        else:
            livingNeigbors[board[point.y][point.x - 1]] += 1
            livingNeigbors[board[point.y][point.x + 1]] += 1
            livingNeigbors[board[point.y + 1][point.x - 1]] += 1
            livingNeigbors[board[point.y + 1][point.x]] += 1
            livingNeigbors[board[point.y + 1][point.x + 1]] += 1
    elif bottomBorder:
        if leftBorder:
            livingNeigbors[board[point.y - 1][point.x]] += 1
            livingNeigbors[board[point.y][point.x + 1]] += 1
            livingNeigbors[board[point.y - 1][point.x + 1]] += 1
        elif rightBorder:
            livingNeigbors[board[point.y][point.x - 1]] += 1
            livingNeigbors[board[point.y - 1][point.x]] += 1
            livingNeigbors[board[point.y - 1][point.x - 1]] += 1
        else:
            livingNeigbors[board[point.y - 1][point.x - 1]] += 1
            livingNeigbors[board[point.y - 1][point.x + 1]] += 1
            livingNeigbors[board[point.y - 1][point.x]] += 1
            livingNeigbors[board[point.y][point.x - 1]] += 1
            livingNeigbors[board[point.y][point.x + 1]] += 1
    else:
        if leftBorder:
            livingNeigbors[board[point.y - 1][point.x]] += 1
            livingNeigbors[board[point.y + 1][point.x]] += 1
            livingNeigbors[board[point.y][point.x + 1]] += 1
            livingNeigbors[board[point.y - 1][point.x + 1]] += 1
            livingNeigbors[board[point.y + 1][point.x + 1]] += 1
        elif rightBorder:
            livingNeigbors[board[point.y - 1][point.x - 1]] += 1
            livingNeigbors[board[point.y][point.x - 1]] += 1
            livingNeigbors[board[point.y + 1][point.x - 1]] += 1
            livingNeigbors[board[point.y - 1][point.x]] += 1
            livingNeigbors[board[point.y + 1][point.x]] += 1
        else:
            livingNeigbors[board[point.y][point.x + 1]] += 1
            livingNeigbors[board[point.y][point.x - 1]] += 1
            livingNeigbors[board[point.y - 1][point.x]] += 1
            livingNeigbors[board[point.y + 1][point.x]] += 1
            livingNeigbors[board[point.y - 1][point.x + 1]] += 1
            livingNeigbors[board[point.y - 1][point.x - 1]] += 1
            livingNeigbors[board[point.y + 1][point.x + 1]] += 1
            livingNeigbors[board[point.y + 1][point.x - 1]] += 1
    return livingNeigbors


def update_point_status(board, point, size):
    livingNeigbors = count_living_neighbors(board, point, size)
    new_point = Point('.', point.x, point.y)
    if point.type == '.':
        new_point.type = '|' if livingNeigbors['|'] >= 3 else '.'
    elif point.type == '|':
        new_point.type = '#' if livingNeigbors['#'] >= 3 else '|'
    elif point.type == '#':
        new_point.type = '#' if livingNeigbors['#'] >= 1 and livingNeigbors['|'] >= 1 else '.'
    else:
        new_point.type = point.type
    return new_point

def get_next_iteration(points, board, size):
    next_board = deepcopy(board)
    new_points = []
    for point in points:
        new_point = update_point_status(board, point, size)
        new_points.append(new_point)
        next_board[new_point.y][new_point.x] = new_point.type
    return new_points, next_board

def print_board(board, size):
    for i in range(size):
        for j in range(size):
            print(board[i][j], end='')
        print()

def first_10_min(board, points, size):
    next_board = deepcopy(board)
    for t in range(10):
        print (t)
        print_board(next_board, size)
        points, next_board = deepcopy(get_next_iteration(points, board, size))
        board = deepcopy(next_board)
    return board

def count_trees_lumbers(board, size):
    count = Counter()
    for i in range(size):
        for j in range(size):
            count[board[i][j]] += 1
    print(count)
    return count
def main():
    y = 0
    size = 50
    with open('in/day_18.in') as f:
        line = f.readline().strip()
        board = []
        points = []
        while line != '':
            # print(line)
            row = []
            x = 0
            for c in line:
                point = Point(c, x, y)
                row.append(c)
                points.append(point)
                x += 1
            board.append(row)
            y += 1
            line = f.readline().strip()
    # print(points)
    first_10_min_board = first_10_min(board, points, size)
    count = count_trees_lumbers(first_10_min_board, size)
    print(count['#'] * count['|'])

if __name__ == "__main__":
    main()

RAW = '''.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.'''.split('\n')

def test():
    size = 10
    num_row = 0
    board = []
    points = []
    for line in RAW:
        board_row = []
        num_col = 0
        for c in line:
            point = Point(c, num_col, num_row)
            num_col += 1
            board_row.append(c)
            points.append(point)
        num_row += 1
        board.append(board_row)
    first_10_min_board = first_10_min(board, points, size)
    print_board(first_10_min_board, size)
    count = count_trees_lumbers(first_10_min_board, size)
    print(count['#'] * count['|'])

# test()
