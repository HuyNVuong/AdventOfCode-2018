from typing import NamedTuple, List, Tuple

class Node(NamedTuple):
    numChild: int
    numMetadata: int
    childEntries: List['Node']
    metadataEntries: List[int]
    def getData():
        print(numChild, numMetadata, childEntries, metadataEntries)

nodeList = []
'''
Part 1. recursively create new node and add it into the root, finding sum will be same way
'''
def processNode(line, start):
    numChild = line[start]
    numMetadata = line[start + 1]
    childEntries = []
    start = start + 2
    for i in range(numChild):
        node, start = processNode(line, start)
        childEntries.append(node)
    end = start + numMetadata
    metadataEntries = line[start:end]
    return Node(numChild, numMetadata, childEntries, metadataEntries), end


def findSum(node):
    sumMetadata = sum(node.metadataEntries)
    for child in node.childEntries:
        sumChild = findSum(child)
        sumMetadata += sumChild
    return sumMetadata


with open ('day_8.in') as f:
    line = [int(num) for num in f.readline().strip().split()]

root, blob = processNode(line, 0)
print(findSum(root))
'''
Unit testing
'''
TEST = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
line_TEST = [int(num) for num in TEST.strip().split()]
node, i = processNode(line_TEST, 0)
assert findSum(node) == 138
