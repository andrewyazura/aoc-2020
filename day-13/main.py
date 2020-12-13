import itertools
with open('day-13/input.txt', 'r') as file:
    puzzle_input_timestamp = int(file.readline().strip())
    puzzle_input = [
        int(i) if i != 'x' else i for i in file.readline().split(',')]


def part_1(timestamp, puzzle_input):
    buses = [x for x in puzzle_input if x != 'x']
    r = min([(bus, -(timestamp % bus) + bus)
             for bus in buses], key=lambda x: x[1])
    return r[0] * r[1]


def part_2(puzzle_input):
    step = 1
    start_timestamp = 100000000000000
    buses = [(i, b) for i, b in enumerate(puzzle_input) if b != 'x']

    for i, b in buses:
        for current_timestamp in itertools.count(start_timestamp, step):
            if (current_timestamp + i) % b == 0:
                start_timestamp = current_timestamp
                step *= b
                break

    return start_timestamp


print(part_1(puzzle_input_timestamp, puzzle_input))
print(part_2(puzzle_input))
