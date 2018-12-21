from copy import deepcopy
import re

OPERATIONS = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
           'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

class Instruction:
    def __init__(self, operation, opcode, a, b, c):
        self.operation = operation
        self.opcode = opcode
        self.a = a
        self.b = b
        self.c = c

    def __repr__():
        return 'Instruction({} {} {} {})'.format(self.opcode, self.a, self.b, self.c)

    def operate(self, r):
        output = deepcopy(r)
        if self.operation == 'addr':
            output[self.c] = r[self.a] + r[self.b]
        elif self.operation == 'addi':
            output[self.c] = r[self.a] + self.b
        elif self.operation == 'mulr':
            output[self.c] = r[self.a] * r[self.b]
        elif self.operation == 'muli':
            output[self.c] = r[self.a] * self.b
        elif self.operation == 'banr':
            output[self.c] = r[self.a] & r[self.b]
        elif self.operation == 'bani':
            output[self.c] = r[self.a] & self.b
        elif self.operation == 'borr':
            output[self.c] = r[self.a] | r[self.b]
        elif self.operation == 'bori':
            output[self.c] = r[self.a] | self.b
        elif self.operation == 'setr':
            output[self.c] = r[self.a]
        elif self.operation == 'seti':
            output[self.c] = self.a
        elif self.operation == 'gtir':
            output[self.c] = 1 if self.a > r[self.b] else 0
        elif self.operation == 'gtri':
            output[self.c] = 1 if r[self.a] > self.b else 0
        elif self.operation == 'gtrr':
            output[self.c] = 1 if r[self.a] > r[self.b] else 0
        elif self.operation == 'eqir':
            output[self.c] = 1 if self.a == r[self.b] else 0
        elif self.operation == 'eqri':
            output[self.c] = 1 if r[self.a] == self.b else 0
        elif self.operation == 'eqrr':
            output[self.c] = 1 if r[self.a] == r[self.b] else 0
        return output

'''
Testing
'''

TEST_1 = '''Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]
'''.split('\n')

TEST_2 = '''Before: [3, 1, 0, 1]
9 3 3 2
After:  [3, 1, 0, 1]
'''.split('\n')

TEST_3 = '''Before: [1, 0, 3, 1]
4 2 3 2
After:  [1, 0, 0, 1]
'''.split('\n')
operation_with_opcode = {}

def find_possible_instruction(before, inst, after):
    pre_instruction = [int(s) for s in re.findall(r'\d+', before)]
    ins = [int(s) for s in inst.split()]
    post_instruction = [int(s) for s in re.findall(r'\d+', after)]
    possible = 0
    candicates = []
    for operation in OPERATIONS:
        instruction = Instruction(operation, ins[0], ins[1], ins[2], ins[3])
        output = instruction.operate(pre_instruction)
        candicate = []
        if output == post_instruction:
            possible += 1
            candicate.append((instruction.operation, instruction.opcode))
            candicates.append(candicate)

    i = 1
    assertSet = set(deepcopy(OPERATIONS))
    find_instruction_opcode(candicates, 1, assertSet)
    print(operation_with_opcode)
    return possible

def find_instruction_opcode(candicates, length, operations):
    print(operations)
    if len(operations) == 0:
        return
    for candicate in candicates:
        if len(candicate) == length:
            for set in candicate:
                if set[0] in operations:
                    print(set[0], operations.remove(set[0]))
                    opcode = set[1]
                    operation_with_opcode[opcode] = set[0]
                    length += 1
                    continue
                else:
                    find_instruction_opcode(candicates, length, operations)


assert find_possible_instruction(TEST_1[0], TEST_1[1], TEST_1[2]) == 3
assert find_possible_instruction(TEST_2[0], TEST_2[1], TEST_2[2]) == 4
assert find_possible_instruction(TEST_3[0], TEST_3[1], TEST_3[2]) == 3

def part_1():
    i = 0
    greater_than_3_opcode = 0
    while i < 3115:
        before = input()
        ins = input()
        after = input()
        blank = input()
        if find_possible_instruction(before, ins, after) >= 3:
            greater_than_3_opcode += 1
        i += 4
    return greater_than_3_opcode

print(part_1())
