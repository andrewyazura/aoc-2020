from collections import defaultdict

with open('day-10/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.readlines()]


def part_1(puzzle_input):
    puzzle_input = puzzle_input.copy()
    start = 0
    differences = defaultdict(int)
    device_joltage = max(puzzle_input) + 3

    while start != device_joltage - 3:
        adapter, adapter_diff = min([(i, abs(start - i))
                                     for i in puzzle_input], key=lambda x: x[1])

        if adapter_diff <= 3:
            start = adapter
            puzzle_input.remove(adapter)
            differences[adapter_diff] += 1

    differences[3] += 1
    return differences[1] * differences[3]


def search_ways(nodes, memory):
    ways = 0
    last = max(nodes)

    if memory.get(last, None):
        return memory[last]

    if len(nodes) <= 2:
        return 1  # there is only one path left

    for i in range(1, 4):
        if len(nodes) >= i + 1 and last - nodes[-i-1] <= 3:
            ways += search_ways(nodes[:-i], memory)

    memory[last] = ways
    return ways


def get_item(l, index, default):
    return l[index] if -len(l) <= index < len(l) else default


def part_2(puzzle_input):
    puzzle_input = puzzle_input.copy()
    puzzle_input.append(0)
    puzzle_input.sort()

    memory = {}

    return search_ways(puzzle_input, memory)


print(part_1(puzzle_input))
print(part_2(puzzle_input))
