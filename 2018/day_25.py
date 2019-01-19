
class Point:
    def __init__(self, x, y, w, z):
        self.x = x
        self.y = y
        self.w = w
        self.z = z

    def __repr__(self):
        return 'Point ({}, {}, {}, {})'.format(self.x, self.y, self.w, self.z)

    def distances(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.w - other.w) + abs(self.z - other.z)

def from_line(line):
    x, y, w, z = [int(s) for s in line.split(',')]
    return Point(x, y, w, z)

def find_num_constellation(points):
    constellation = set()
    groups = []
    for i in range(len(points) - 1):
        group = set()
        for j in range(i + 1, len(points)):
            if points[i].distances(points[j]) <= 3:
                group.add(points[i])
                group.add(points[j])
        if len(group) != 0:
            groups.append(group)
    # print(groups)
    constellation = constellation.union(groups[0])
    num_constellation = 1
    for i in range(1, len(groups)):
        if len(constellation.intersection(groups[i])) != 0:
            constellation = constellation.union(groups[i])
        elif groups[i] not in points:
            num_constellation += 1
    return num_constellation

def main():
    with open('in/day_25.in') as f:
        points = [from_line(line.strip()) for line in f]
        num_constellation = find_num_constellation(points)
        print(num_constellation)

if __name__ == "__main__":
    main()

'''
Testing
'''
RAW_1 = '''0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0'''.split('\n')

RAW_2 = '''-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0'''.split('\n')

RAW_3 = '''1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2'''.split('\n')

RAW_4 = '''1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2'''.split('\n')

def test():
    points = [Point.from_line(line) for line in RAW_4]
    num_constellation = find_num_constellation(points)
    print(num_constellation)

# test()
