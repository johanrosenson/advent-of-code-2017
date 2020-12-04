# https://adventofcode.com/2017/day/5

filename = 'input'
# filename = 'example'

instructions = [int(i) for i in open(filename).read().splitlines()]

instruction = 0
steps = 0

while instruction >= 0 and instruction < len(instructions):
    # print(instructions)
    offset = instructions[instruction]

    # store next instruction
    nextInstruction = instruction + offset

    # increase until next time
    if offset >= 3:
        instructions[instruction] -= 1
    else:
        instructions[instruction] += 1

    # set next instruction
    instruction = nextInstruction

    steps += 1

print('Exit in {} steps'.format(steps))
