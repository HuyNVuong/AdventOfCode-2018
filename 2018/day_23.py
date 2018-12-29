import re

class Bot:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def __repr__(self):
        return 'Bot <{}, {}, {}> : {}'.format(self.x, self.y, self.z, self.r)

    def distances_to_bot(self, bot):
        return abs(bot.x - self.x) + abs(bot.y - self.y) + abs(bot.z - self.z)

    def from_line(line):
        rgx = r'pos=<(.*)>, r=(.*)'
        pos, r = re.match(rgx, line).groups()
        x, y, z = [int(n) for n in pos.split(',')]
        r = int(r)
        return Bot(x, y, z, r)

def find_max_range_bot(bots):
    max_bot = Bot(0, 0, 0, 0)
    for bot in bots:
        if max_bot.r < bot.r:
            max_bot = bot
    return max_bot

def find_bots_inrange(bots, max_bot):
    total = 0
    for bot in bots:
        if bot.distances_to_bot(max_bot) <= max_bot.r:
            total += 1
    return total


def main():
    with open('in/day_23.in') as f:
        bots = [Bot.from_line(line) for line in f]
        max_bot = find_max_range_bot(bots)
        total_bots_inrange = find_bots_inrange(bots, max_bot)
        print(total_bots_inrange)

if __name__ == "__main__":
    main()
'''
Testing
'''
RAW = '''pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1'''.split('\n')

bots = [Bot.from_line(line) for line in RAW]
max_bot = find_max_range_bot(bots)
assert find_bots_inrange(bots, max_bot) == 7
