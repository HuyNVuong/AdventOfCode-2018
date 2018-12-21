import numpy
from collections import Counter

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Node({}, {})'.format(self.x, self.y)

	def manhattan_distance(self, p2):
		return abs(self.x - p2.x) + abs(self.y - p2.y)

	def from_line(line):
		x, y = line.split(',')
		return Node(int(x), int(y))

def knn(nodes):
	rightBound = max(node.x for node in nodes)
	leftBound = min(node.x for node in nodes)
	upperBound = min(node.y for node in nodes)
	lowerBound = max(node.y for node in nodes)

	distances = {}
	for x in range(leftBound, rightBound + 1):
		for y in range(upperBound, lowerBound + 1):
			curr_node = Node(x, y)
			if curr_node not in nodes:
				distance_to_curr_node = [(curr_node.manhattan_distance(node), i) for i, node in enumerate(nodes, 1)]
				distance_to_curr_node.sort()
				if distance_to_curr_node[0][0] == distance_to_curr_node[1][0]:
					distances[curr_node] = None
				else:
					distances[curr_node] = distance_to_curr_node[0][1]
	return distances

def findArea(distances, nodes):

	rightBound = max(node.x for node in nodes)
	leftBound = min(node.x for node in nodes)
	upperBound = min(node.y for node in nodes)
	lowerBound = max(node.y for node in nodes)

	nodes_to_process = set()

	for node, id in distances.items():
		if node.x not in (rightBound, leftBound) or node.y not in (upperBound, lowerBound):
			nodes_to_process.add(id)

	areas = Counter()

	for point, id in distances.items():
		if id in nodes_to_process:
			areas[id] += 1

	return areas


with open('in/day_6.in') as f:
	lines = [line for line in f]
	nodes = [Node.from_line(line) for line in lines]

distances = knn(nodes)
print(findArea(distances, nodes).most_common(1))

def test():
	TEST = '''1, 1
	1, 6
	8, 3
	3, 4
	5, 5
	8, 9
	'''
	lines = [line for line in TEST.strip().split('\n')]
	nodes = [Node.from_line(line) for line in lines]
	distances = knn(nodes)
	print(findArea(distances, nodes).most_common(1))

test()
