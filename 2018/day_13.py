
class Cart:
    def __init__(self, x, y, dx, dy, state):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.state = state
    def __repr__(self):
        return 'Star({}, {}, {}, {})'.format(self.x, self.y, self.dx, self.dy, self.state)
    def move(state):
        pass
    def from_line(file):
        find_train = ['<', '>', 'v', '^']
        state : str
        for y, line in enumerate(file):
            for c in set(line):
                if c in find_train:
                    state = c
                    x = line.index(c)
                    return Cart(x, y, 0, 0, state)
