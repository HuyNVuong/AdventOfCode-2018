from day_19 import Instruction
import re
from copy import deepcopy
import time

def try_all(instructions, registers, id):
    ip = registers[id]
    instruction_executed = 0
    while (True):
        try:
            raw_instruction = instructions[ip]
            instruction = Instruction(raw_instruction[0], raw_instruction[1], raw_instruction[2], raw_instruction[3])
            registers = instruction.operate(registers)
            # print(ip, instruction, '->', registers)
            registers[id] += 1
            ip = registers[id]
            instruction_executed += 1
            if instruction_executed > 2000:
                return False
        except KeyError:
            print(ip, instruction, '->', registers)
            registers[id] -= 1
            break
    return True

def main():
    with open('in/day_21.in') as f:
        ip_raw = f.readline()
        ip = int(re.findall(r'\d+', ip_raw)[0])
        line = f.readline()
        instructions = {}
        instruction_ip = 0
        while line != '':
            lineSplit = line.split()
            raw_instruction = (lineSplit[0], int(lineSplit[1]), int(lineSplit[2]), int(lineSplit[3]))
            instructions[instruction_ip] = raw_instruction
            instruction_ip += 1
            line = f.readline()
        start_time = time.time()
        for r0 in range(8010000, 10000000):
            registers = [r0, 0, 0, 0, 0, 0]
            if (try_all(instructions, registers, ip) == True):
                print(r0, 'successfully executed with less than 200 instruction')
                break
        print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    main()
