from copy import deepcopy
'''
H {'U', 'W', 'R'}
M set()
J {'D', 'W', 'L', 'O', 'Z', 'E'}
I {'H', 'R', 'C', 'L', 'P'}
O {'K'}
V {'M'}
Q {'A', 'D', 'C', 'J', 'F', 'T', 'S', 'P', 'B'}
Y {'H', 'Q', 'A', 'D', 'C', 'I', 'T', 'P', 'U', 'N', 'B'}
C {'G', 'U'}
S {'G', 'M', 'D', 'F', 'T', 'I', 'O', 'P', 'U'}
U {'K', 'X', 'V'}
Z set()
D {'G', 'Z', 'X', 'M'}
F {'H', 'C', 'O', 'U'}
T {'D', 'C', 'F', 'P'}
N {'Q', 'A', 'I', 'T', 'O', 'S', 'P', 'Z', 'B'}
E {'Z', 'C'}
B {'V', 'G', 'M', 'A', 'R', 'F', 'J', 'K', 'S', 'P', 'X', 'W'}
G set()
A {'H', 'R', 'D', 'F', 'O', 'Z'}
R {'L', 'J', 'U'}
K {'Z'}
L {'G'}
P {'Z', 'L', 'E', 'R'}
X {'G'}
W set()
'''
vertexSet = {}
with open ('in/day_7.in') as f:
    lines = [line.strip().split() for line in f]  
    for line in lines:
        pre = line[7]
        req = line[1]
        if req not in vertexSet.keys():
            vertexSet.setdefault(req, set())
        if pre not in vertexSet.keys():
            vertexSet.setdefault(pre, set())
            vertexSet[pre].add(line[1])
        else:
            vertexSet[pre].add(line[1])


def process_order():
    processed = []
    process = deepcopy(vertexSet)
    while process:
        possible_path = [vertex for vertex, reqs in process.items() if len(reqs) == 0]
        possible_path.sort()
        next_vertex = possible_path[0]
        processed.append(next_vertex)
        for reqs in process.values():
            if next_vertex in reqs:
                reqs.remove(next_vertex)
        del process[next_vertex]
    return ''.join(processed)

class Worker:
    def __init__(self, time_to_work, time_start):
        self.time_start = time_start
        self.time_to_work = time_to_work
def process_work_time():
    workList = []
    process = deepcopy(vertexSet)
    tick = 0
    while process:
        possible_path = [vertex for vertex, reqs in process.items() if len(reqs) == 0]
        possible_path.sort()
        next_vertex = possible_path[0]
        while possible_path:
            next_work = possible_path.pop(0)
            worker = Worker(ord(next_work) - 96, tick)
            if len(workList) <= 5:
                workList.append(worker)
            tick += 1
        for worker in workList:
            if worker.time_to_work == tick - worker.time_start:
                workList.remove(worker)
        tick += 60
        for reqs in process.values():
            if next_vertex in reqs:
                reqs.remove(next_vertex)
        del process[next_vertex]
    return tick
  

if __name__ == "__main__":
    print(process_order())
    print(process_work_time())
'''
Unit testing
'''
RAW = [
'Step C must be finished before step A can begin.',
'Step C must be finished before step F can begin.',
'Step A must be finished before step B can begin.',
'Step A must be finished before step D can begin.',
'Step B must be finished before step E can begin.',
'Step D must be finished before step E can begin.',
'Step F must be finished before step E can begin.'
]

