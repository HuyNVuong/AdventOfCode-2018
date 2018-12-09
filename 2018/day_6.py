import numpy

n = 10 # Global matrix size
allNodes_test = []
# class Node(value, index):


def spread(board, node):
	j = node[1]
	i = node[2]
	value = node[0]
	print(value)
	if i < n - 1:
		board[i + 1][j] = value
		newNode = [value, j, i + 1]
		allNodes_test.append(newNode)
	if i > 0:
		board[i - 1][j] = value
		newNode = [value, j, i - 1]
		allNodes_test.append(newNode)
	if j < n - 1:
		board[i][j + 1] = value
		newNode = [value, j + 1, i]
		allNodes_test.append(newNode)
	if j > 0:
		board[i][j - 1] = value
		newNode = [value, j - 1, i]
		allNodes_test.append(newNode)
	allNodes_test.remove(node)


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
allNodes_test = [node for node in TEST]
board = initBoard(TEST)
stop = 8
i = 0
for node in allNodes_test:
	spread(board, node)
	i += 1
	if i == 15:
		break
print(allNodes_test)
print(board)

# assert == [(e, 17)]
