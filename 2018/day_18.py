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

'''
Part 2.
Possible answer resonating between minute 567 -> 594 (Repeat every 27 minutes)
 resonate at  185460 679 -> 567  0 (out)
 resonate at  187040 680 -> 568  1 (out, Why??)     -- Somewhere around here???? --
 resonate at  185885 681 -> 569  2 (out)             -- Cycle start at 0 or 1 ?? --
 resonate at  190518 682 -> 570 (out)
 resonate at  189596 683 -> 571 (out)
 resonate at  191295 684 -> 572 (too high)
 resonate at  186686 685 -> 573
 resonate at  183048 686 -> 574
 resonate at  175602 687 -> 575
 resonate at  171342 688 -> 576
 resonate at  164406 689 -> 577
 resonate at  163386 690 -> 578
 resonate at  162792 691 -> 579
 resonate at  165376 692 -> 580 -> Right here !!
 resonate at  163494 693 -> 581
 resonate at  170400 694 -> 582
 resonate at  175160 695 -> 583
 resonate at  181383 696 -> 584
 resonate at  185609 697 -> 585
 resonate at  192185 698 -> 586 (out)
 resonate at  194296 699 -> 587 (out)
 resonate at  197728 700 -> 588 (out)
 resonate at  197232 701 -> 589 (out)
 resonate at  196860 702 -> 590 23 (out)
 resonate at  195052 703 -> 591 24 (out)
 resonate at  193230 704 -> 592 24 (out)    -- Somewhere around here???? --
 resonate at  190400 705 -> 593 25
 resonate at  188720 706 -> 594 26 (out)
 (1000000000 - 594) % 27 = 1
 (1000000000 - 568) % 27 = 0
Minute 1000000000: at index 1 of the cycle -> 187040
'''

def first_10_min(board, points, size):
    next_board = deepcopy(board)
    seen = {}
    for t in range(2000):
        # print (t)
        # if t >= 249:
        counter = count_trees_lumbers(board, size)
        count = counter['#'] * counter['|']
        # print(count)
        print_board(board, size)
        if count in seen.keys():
            print(' resonate at ', count, t, '->', seen[count])
        else:
            seen[count] = t
        points, next_board = deepcopy(get_next_iteration(points, board, size))
        board = deepcopy(next_board)

    return board

def count_trees_lumbers(board, size):
    count = Counter()
    for i in range(size):
        for j in range(size):
            count[board[i][j]] += 1
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
    print((676 - 595) % 27)
    print((1000000000 - 571) % 27)
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

    # first_10_min_board = first_10_min(board, points, size)
    print_board(first_10_min_board, size)
    count = count_trees_lumbers(first_10_min_board, size)
    print(count['#'] * count['|'])

# test()
