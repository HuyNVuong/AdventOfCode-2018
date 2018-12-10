from copy import deepcopy
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def IterativeStackDFS(graph, vertex, path=[]):
    white = []
    gray = []
    black = []
    for v in vertexSet.keys():
        white.append(v)
    S = Stack()
    S.push(vertex)
    gray.append(vertex)
    white.remove(vertex)
    count = 0
    discovery = {}
    processed = {}
    discovery[0] = count
    while not S.isEmpty():
        count += 1
        x = S.peek()
        y = None
        for w in graph[x]:
            if w in white:
                y = w
                graph[x].remove(y)
                break
        if y == None:
            if not white == []:
                S.push(white[0])
                gray.append(white[0])
                white.remove(white[0])
                continue
            S.pop()
            black.append(x)
            gray.remove(x)
            node = x
            processed[node] = count
        else:
            S.push(y)
            gray.append(y)
            white.remove(y)
            node = y
            discovery[node] = count
    black.reverse()
    return black

def IterativeBFS(graph, start):
    explored = []
    queue = [start]
    timeStamp = {}
    timeStamp[start] = 0
    visited = [start]
    while queue:
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

                timeStamp[neighbour] = timeStamp[node] + 1


    return explored

with open ('in/day_7.in') as f:
    allLines = [line.strip().split() for line in f]
    vertexSet = {}
    for line in allLines:
        key = line[1]
        vertexSet.setdefault(key, [])
        key = line[7]
        vertexSet.setdefault(key, [])
    for line in allLines:
        key = line[1]
        vertexSet[key].append(line[7])


for vertex in vertexSet.keys():
    print(vertex, vertexSet[vertex])
    # print('Possible path: ', ''.join(IterativeStackDFS(vertexSet, vertex)), len(vertexSet.keys()), '--', len(IterativeStackDFS(vertexSet, vertex)) )

'''
Unit testing
'''
TEST = [
'Step C must be finished before step A can begin.',
'Step C must be finished before step F can begin.',
'Step A must be finished before step B can begin.',
'Step A must be finished before step D can begin.',
'Step B must be finished before step E can begin.',
'Step D must be finished before step E can begin.',
'Step F must be finished before step E can begin.'
]
allLines = [line.strip().split() for line in TEST]
vertexSet = {}
for line in allLines:
    key = line[1]
    vertexSet.setdefault(key, [])
    key = line[7]
    vertexSet.setdefault(key, [])
for line in allLines:
    key = line[1]
    vertexSet[key].append(line[7])
print(vertexSet)
tmp = deepcopy(vertexSet)
print(IterativeBFS(vertexSet, 'C'))
print(IterativeStackDFS(tmp, 'C'))
