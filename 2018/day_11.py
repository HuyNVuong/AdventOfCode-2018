import numpy
from typing import Tuple
def grid(sn):
    G = numpy.zeros((300, 300))
    for y in range(300):
        for x in range(300):
            rackID = x + 10
            power = y * rackID
            power += sn
            power = power * rackID
            power_str = str(power)
            G[y][x] = int(power_str[-3]) - 5
    return G
'''
A lot of cool algorithm could help this a lot
'''
def subSum(x, y, grid, size):
    rightBound = x + size
    lowBound = y + size
    sum = 0
    for i in range(y, lowBound):
        for j in range(x, rightBound):
            sum += grid[i][j]
    return sum

def findMax(grid, n, size):
    new_max = 0
    pos: Tuple
    for y in range(n - size + 1):
        for x in range(n - size + 1):
            curr_max = subSum(x, y, grid, size)
            if new_max < curr_max:
                new_max = curr_max
                pos = (x, y)

    return pos, new_max

def find_max_with_size(grid, n):
    pack: Tuple
    maxPack = []
    maxArea = 0
    for size in range(2, 301):
        currPack = findMax(grid, n, size)
        if maxArea < currPack[1]:
            maxPack = currPack
            maxArea = currPack[1]
            print(size, maxPack[0])
    return maxPack

G = grid(9445)
print(findMax(G, 300, 3)[0])
print(find_max_with_size(G, 300))

'''
Testing
'''
assert grid(57)[79][122] == -5
assert grid(39)[196][217] == 0
assert grid(71)[153][101] == 4

TEST = [[-2,  -4,   4,   4,   4,], [-4,   4,   4,   4, -5,], [4,   3,  3,   4,  -4,], [ 1,   1,   2,   4,  -3], [-1,   0,   2,  -5,  -2,],]
assert findMax(TEST, 5, 3)[0] == (1, 1)
