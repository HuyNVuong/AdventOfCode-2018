
class Cart:
    def __init__(self, x, y, dx, dy, state):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.state = state

    def __repr__(self):
        return 'Cart({}, {}, {}, {})'.format(self.x, self.y, self.dx, self.dy, self.state)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def left_right(self):
        self.dy = 0
        if self.state == '>':
            self.dx = 1
        elif self.state == '<':
            self.dx = -1

    def straight(self):
        self.dx = 0
        if self.state == '^':
            self.dy = -1
        elif self.state == 'v':
            self.dy = 1

    def get_next_move(self, track):
        if track[self.y][self.x + 1] or track[self.y][sefl.x - 1] == '-':
            left_right()
        elif track[self.y + 1][self.x] or track[self.y - 1][self.x] == '|':
            straigt()
        elif track[self.y][self.x + 1] == '\\':
            left_right()
            self.state = 'v'
        elif track[self.y][self.x - 1] == '/':
            left_right()
            self.state = 'v'
        elif track[self.y][self.x + 1] == '/':
            left_right()
            self.state = '^'

RAW = r"""/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """.split('\n')
