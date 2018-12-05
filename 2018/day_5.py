import copy
'''
Part 1.
String repulsive reaction. If 2 letters next to each other are the same
but not equal (Aa not AA) then pop both of them out. Recurse until the
string can't pop any more character
'''
def react(polymer):
    i = 0
    length = len(polymer)
    while i < len(polymer) - 1:
        if (polymer[i].lower() == polymer[i + 1].lower()) and (polymer[i] != polymer[i + 1]):
            polymer.pop(i)
            polymer.pop(i)
        i += 1

    if length == len(polymer):
        return len(polymer)
    return react(polymer)


'''
Part 2.
Find most efficient reaction with removing 2 character out
Brute force by try removing each pair, would take long, but
not break the machine since nothing would cause iteration to raise
exponentially
'''
'''
This would avoid recursion depth maxima error
If found, go left, otherwise, go right
'''
def reactIterative(polymer):
    i = 0
    length = len(polymer)
    while i < len(polymer) - 1:
        if (polymer[i].lower() == polymer[i + 1].lower()) and (polymer[i] != polymer[i + 1]):
            polymer.pop(i)
            polymer.pop(i)
            i -= 1
        else:
            i += 1
    return len(polymer)


def tryAll(polymer, polymerSet):
    minLength = 1000000
    oldString = copy.deepcopy(polymer)
    for c in polymerSet:
        neg = c.lower()
        pos = c.upper()
        polymer = polymer.replace(neg, "")
        polymer = polymer.replace(pos, "")
        curr_length = reactIterative(list(polymer))
        if(minLength > curr_length):
            minLength = curr_length
        polymer = copy.deepcopy(oldString)
    return minLength


with open('day_5.in') as f:
    polymer = f.readline().strip()
    polymerSet = set(polymer.lower())

print (reactIterative(list(polymer)))
print (tryAll(polymer, polymerSet))

TEST = "dabAcCaCBAcCcaDA"

assert reactIterative(list(TEST)) == 10
assert tryAll(TEST, set(TEST.lower())) == 4
