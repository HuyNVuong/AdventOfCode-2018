from copy import deepcopy

def reproduce(state, reproduce_comp):
    state.append('.')
    next_state = deepcopy(state)
    for i in range(2, len(state) - 2):
        plantComp = ''.join(state[(i - 2):(i + 3)])
        if plantComp in list(reproduce_comp.keys()):
            next_state[i] = reproduce_comp[plantComp]
    return next_state

def countAlive(state, left_shift):
    points = 0
    for i in range(len(state)):
        if state[i] == '#':
            points += i - left_shift
    return points

with open('in/day_12.in') as f:
    reproduce_comp = {}
    line = f.readline()
    curr_state = [c for c in line if (c == '#' or c == '.')]
    curr_state.insert(0, '...')
    curr_state = list(''.join(curr_state))
    f.readline()
    for line in f:
        line = line.strip().split(' => ')
        key = line[0]
        reproduce_comp[key] = line[1]

left_shift = 3
seen = set()
# print('[{}]: {}'.format(0, ''.join(state)))
for i in range(1, 125):
    next_state = reproduce(curr_state, reproduce_comp)
    if ''.join(next_state) in seen:
        diff = countAlive(next_state, left_shift) - countAlive(curr_state, left_shift)
        print( countAlive(next_state, left_shift - 1))
        print('Repeating sequence at {} with diff {} '.format(i, diff))
        # break
    else:
        seen.add(''.join(next_state))
        curr_state = deepcopy(next_state)
    print('[{}]: {}'.format(i, ''.join(curr_state)))
    # if i > 110:
    #     print(i, countAlive(curr_state, left_shift))

print(i, countAlive(curr_state, left_shift))
'''
For each gen after gen 94, plant got shifted by 1, therefore num plants
increased by curr_sum - prev_sum, which is 20
Don't even cache the point, just print the whole thing out and eyeballing the repeating sequence
trimming the state would result in an sequence error
num_trees survive for an infnitely long time: const 23
Gen where they start to balance: 111 ~ 112?
Answer: 1150000000457
'''
print(3033 + 23 * (50000000000 - 112))

assert countAlive('.#....##....#####...#######....#.#..##', 3) == 325
