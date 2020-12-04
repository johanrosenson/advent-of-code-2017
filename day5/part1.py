# https://adventofcode.com/2017/day/5

filename = 'input'
# filename = 'example'

instructions = [int(i) for i in open(filename).read().splitlines()]

instruction = 0
steps = 0

while instruction >= 0 and instruction < len(instructions):
    # print(instructions)

    # store next instruction
    nextInstruction = instruction + instructions[instruction]

    # increase until next time
    instructions[instruction] += 1

    # set next instruction
    instruction = nextInstruction

    steps += 1

print('Exit in {} steps'.format(steps))
