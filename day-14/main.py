import re
import itertools

with open('day-14/input.txt', 'r') as file:
    puzzle_input = [i.strip() for i in file.readlines()]


def apply_mask(value, mask, no_change='X'):
    mask = list(mask)
    value = list(bin(int(value))[2:].rjust(36, '0'))

    for i in range(36):
        if mask[i] != no_change:
            value[i] = mask[i]

    value = ''.join(value)
    if 'X' not in value:
        return int(value, 2)

    value = value.replace('X', '{}')
    combs = itertools.product((0, 1), repeat=value.count('{}'))

    return [int(value.format(*nums), 2) for nums in combs]


def part_1(puzzle_input):
    memory = {}
    mask = ''

    for entry in puzzle_input:
        mask_change = re.findall(r'mask = (.{36})', entry)
        if mask_change:
            mask = mask_change[0]

        memory_write = re.findall(r'mem\[(\d+)\] = (\d+)', entry)
        if memory_write:
            memory_write = memory_write[0]
            memory[memory_write[0]] = apply_mask(memory_write[1], mask)

    return sum(memory.values())


def part_2(puzzle_input):
    memory = {}
    mask = ''

    for entry in puzzle_input:
        mask_change = re.findall(r'mask = (.{36})', entry)
        if mask_change:
            mask = mask_change[0]

        memory_write = re.findall(r'mem\[(\d+)\] = (\d+)', entry)
        if memory_write:
            memory_write = memory_write[0]
            value = int(memory_write[1])

            for addr in apply_mask(memory_write[0], mask, '0'):
                memory[addr] = value

    return sum(memory.values())


print(part_1(puzzle_input))
print(part_2(puzzle_input))
