import re
from copy import deepcopy

class Instruction:
    def __init__(self, operation, a, b, c):
        self.operation = operation
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return 'Instruction({} {} {} {})'.format(self.operation, self.a, self.b, self.c)

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
Part 1. I was patient enought to wait for 5 min for the answer
It comes to notice that all instructions seems to run in a cycle,
if we could find 1 cycle we can predict what's going to be next
'''
def operate_with_ip(instructions, id):
    registers = [0, 0, 0, 0, 0, 0]
    ip = registers[id]
    while (True):
        try:
            raw_instruction = instructions[ip]
            instruction = Instruction(raw_instruction[0], raw_instruction[1], raw_instruction[2], raw_instruction[3])
            registers = instruction.operate(registers)
            print(ip, instruction, '->', registers)
            registers[id] += 1
            ip = registers[id]
        except KeyError:
            print(ip, instruction, '->', registers)
            registers[id] -= 1
            break
    return registers

def main():
    with open('in/day_19.in') as f:
        ip_raw = f.readline()
        ip = int(re.findall(r'\d+', ip_raw)[0])
        print(ip)
        line = f.readline()
        instructions = {}
        instruction_ip = 0
        while line != '':
            lineSplit = line.split()
            raw_instruction = (lineSplit[0], int(lineSplit[1]), int(lineSplit[2]), int(lineSplit[3]))
            instructions[instruction_ip] = raw_instruction
            instruction_ip += 1
            line = f.readline()
        # execute_all(instructions)
        operate_with_ip(instructions, ip)
if __name__ == "__main__":
    main()

TEST = '''seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5'''.split('\n')

'''
Part 2. Changing r0 to 1 makes r1 stucks at 105512560
therefore after 1 cycle r0 = sum of factors 105512560
Answer: 22157688
'''
def test():
    instructions = {}
    ip = 0
    for line in TEST:
        lineSplit = line.split()
        raw_instruction = (lineSplit[0], int(lineSplit[1]), int(lineSplit[2]), int(lineSplit[3]))
        instructions[ip] = raw_instruction
        ip += 1
    print(operate_with_ip(instructions, 0))
