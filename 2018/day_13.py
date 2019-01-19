from enum import Enum

class Turn(Enum):
    left = 0
    straight = 1
    right = 2

class Cart:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        if state == '>':
            self.dx = 1
            self.dy = 0
        elif state == '<':
            self.dx = -1 
            self.dy = 0
        elif state == 'v':
            self.dx = 0
            self.dy = 1
        elif state == '^':
            self.dx = 0
            self.dy = -1
        self.state = state
        self.turn = Turn.left

    def __repr__(self):
        return 'Cart({}, {}, {}, {}) : {}'.format(self.x, self.y, self.dx, self.dy, self.state)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def turn_left(self):
        self.dx, self.dy = self.dy, -self.dx 

    def turn_right(self):
        self.dx, self.dy = -self.dy, self.dx
    
    def update_state(self):
        if self.dx == 0 and self.dy == 1:
            self.state = 'v'
        elif self.dx == 0 and self.dy == -1:
            self.state = '^'
        elif self.dx == -1 and self.dy == 0:
            self.state = '<'
        elif self.dx == 1 and self.dy == 0:
            self.state = '>'
        else:
            self.state = self.state

    def get_next_move(self, track):
        pos = (self.x, self.y)
        

                
def parse(raw):
    lines = raw.split('\n')
    track = {}
    carts = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '>' or c == '<':
                pos = (x, y)
                track[pos] = '-'
                cart = Cart(x, y, c)
                carts.append(cart)
            elif c == 'v' or c == '^':
                pos = (x, y)
                track[pos] = '|'
                cart = Cart(x, y, c)
                carts.append(cart)
            elif c == '|' or c == '\\' or c == '+' or c == '/' or c == '-':
                pos = (x, y)
                track[pos] = c

    return track, carts

RAW = r"""/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """

if __name__ == "__main__":
    track, carts = parse(RAW)
    for coor, val in track.items():
        print(coor, val)
    crash = False 
    c1 = carts[0]
    c2 = carts[1]
    print(carts)
    while not crash:
        c1.move()
        c2.move()
        c1.update_state()
        c2.update_state()
        print(carts)
        
        c1.get_next_move(track)
        c2.get_next_move(track)
        
        
        if c1.x == c2.x and c1.y == c2.y:
            crash = True 

