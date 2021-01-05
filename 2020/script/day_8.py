with open("puzzle8_input.txt") as f:
    inst = [i.strip() for i in f]

instructions = [i.split(' ') for i in inst]

def getAccumulator(instruction_list: list, solution: str=None) -> int:
    memo = {}
    accumulator = 0
    i = 0
    while i < len(instruction_list) and i not in memo.keys():
        if instruction_list[i][0] == 'acc':
            memo[i] = instruction_list[i]
            if instruction_list[i][1][0] == '+':
                accumulator += int(instruction_list[i][1][1:])
            else: accumulator -= int(instruction_list[i][1][1:])
            i += 1
        elif instruction_list[i][0] == 'jmp':
            memo[i] = instruction_list[i]
            if instructions[i][1][0] == '+':
                i += int(instruction_list[i][1][1:])
            else: i -= int(instruction_list[i][1][1:])
        elif instruction_list[i][0] == 'nop':
            memo[i] = instruction_list[i]
            i += 1
            continue
    if solution == 'accumulator':
        return accumulator
    else: return i == len(instruction_list)

print("Part I:", getAccumulator(instructions, 'accumulator'))

def changeJmpNop(instruction_list: list) -> int:
    for i in range(len(instruction_list)):
        if instruction_list[i][0] == 'jmp':
            instruction_list[i][0] = 'nop'
            if getAccumulator(instruction_list) == False:
                instruction_list[i][0] = 'jmp'
            else: return True, i
        elif instruction_list[i][0] == 'nop':
            instruction_list[i][0] = 'jmp'
            if getAccumulator(instruction_list) == False:
                instruction_list[i][0] = 'nop'
            else: return True, i 

changeJmpNop(instructions)
print("Part II:", getAccumulator(instructions, 'accumulator'))
