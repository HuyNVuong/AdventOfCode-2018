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

candicates = []
def find_possible_instruction(before, inst, after):
    pre_instruction = [int(s) for s in re.findall(r'\d+', before)]
    ins = [int(s) for s in inst.split()]
    post_instruction = [int(s) for s in re.findall(r'\d+', after)]
    possible = 0
    for operation in OPERATIONS:
        instruction = Instruction(operation, ins[0], ins[1], ins[2], ins[3])
        output = instruction.operate(pre_instruction)
        candicate = []
        if output == post_instruction:
            possible += 1
            candicate.append((instruction.opcode, instruction.operation))
            candicates.append(candicate)
    return possible


def find_instruction_opcode():
    raw_operation_with_opcode = {}
    for candicate in candicates:
        if len(candicate) == 1:
            key = candicate[0][0]
            if key not in raw_operation_with_opcode.keys():
                raw_operation_with_opcode.setdefault(key, set())
            else:
                raw_operation_with_opcode[key].add(candicate[0][1])
    # for key, val in raw_operation_with_opcode.items():
        # print(key, val.difference({'muli', 'addi', 'mulr', 'addr', 'eqri', 'eqrr', 'bori', 'borr', 'seti', 'eqir', 'gtrr', 'gtri'}))


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
'''
At this point, raw was easy enough to scan with normal eye and work it on paper
to determine the instruction instruction based on raw set extracted
'''
instruction_with_opcode = {
    0  : 'banr',
    1  : 'addr',
    2  : 'eqri',
    3  : 'setr',
    4  : 'gtrr',
    5  : 'bori',
    6  : 'gtir',
    7  : 'seti',
    8  : 'borr',
    9  : 'bani',
    10 : 'eqir',
    11 : 'eqrr',
    12 : 'gtri',
    13 : 'addi',
    14 : 'muli',
    15 : 'mulr',
}

def part_2():
    i = 3116
    blank = input()
    blank = input()
    r0 = 0
    curr_registers = [0, 0, 0, 0]
    while True:
        try:
            line = [int(s) for s in input().split()]
            instruction = Instruction(instruction_with_opcode[line[0]], line[0], line[1], line[2], line[3])
            result_registers = instruction.operate(curr_registers)
            curr_registers = result_registers
            print(line, '->', curr_registers)
        except EOFError:
            break
    return curr_registers[0]
print(part_2())
