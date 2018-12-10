import re
import sys
rgx = r"position=<(.*)> velocity=<(.*)>"
class Star:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return 'Star({}, {}, {}, {})'.format(self.x, self.y, self.vx, self.vy)

    def move(self, ticks):
        self.x += ticks * self.vx
        self.y += ticks * self.vy

    def parse(line: str):
        position, velocity = re.match(rgx, line).groups()
        x, y = [int(n) for n in position.split(',')]
        vx, vy = [int(n) for n in velocity.split(',')]
        return Star(x, y, vx, vy)

def alligning(allStars, trigger):
    locations = set()
    for star in allStars:
        star_location = (star.x, star.y)
        locations.add(star_location)
    rightBound = max(star.x for star in allStars)
    leftBound = min(star.x for star in allStars)
    upBound = min(star.y for star in allStars)
    downBound = max(star.y for star in allStars)
    if trigger is True:
        for j in range(upBound, downBound):
            for i in range(leftBound, rightBound + 1):
                if (i, j) in locations:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
    return (rightBound - leftBound) * (downBound - upBound)

def findMessage(allStars, ticks):
    trigger = False
    curr_size = alligning(allStars, trigger)
    for star in allStars:
        star.move(ticks)
    while True:
        for star in allStars:
            if trigger == False:
                next_size = alligning(allStars, trigger)
                if curr_size >= next_size:
                    star.move(1)
                    curr_size = next_size
                else:
                    trigger = True
            else:
                alligning(allStars, trigger)
                return ticks
        ticks += 1

with open('in/day_10.in') as f:
    allStars = [Star.parse(line) for line in f]

# Find message with a randomly starting second, say the magic number should be around 10000
print(findMessage(allStars, 10650))
TEST = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

allStars_test = [Star.parse(line) for line in TEST.split('\n')]

findMessage(allStars_test, 0)
