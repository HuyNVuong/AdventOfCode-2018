import numpy

n = 10 # Global matrix size

# class Node(value, index):


def spread(board, node):
	j = node[1]
	i = node[2]
	if i < n - 1:
		board[i + 1][j] = node[0]
	if i > 0:
		board[i - 1][j] = node[0]
	if j < n - 1:
		board[i][j + 1] = node[0]
	if j > 0:
		board[i][j - 1] = node[0]



def initBoard(positions):
	board = numpy.zeros((n, n))
	for node in positions:
		y = node[1]
		x = node[2]
		board[x][y] = node[0]
	return board


with open('day_6.in') as f:
	# allLines = [line.strip().split(',') for line in f]
	line = f.readline()
	node = 1
	allNodes = []
	while line != '':
		l = []
		l.append(node)
		split = line.strip().split(',')
		l.append(int(split[0]))
		l.append(int(split[1]))
		allNodes.append(l)
		node += 1
		line = f.readline()

# initBoard(allLines)

TEST = [
		[1, 1, 1],
		[2, 1, 6],
		[3, 8, 3],
		[4, 3, 4],
		[5, 5, 5],
		[6, 8, 9]
]
board = initBoard(TEST)

for node in TEST:
	spread(board, node)
print(board)
