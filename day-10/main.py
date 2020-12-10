from collections import defaultdict

with open('day-10/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.readlines()]


def part_1(puzzle_input):
    puzzle_input = puzzle_input.copy()
    puzzle_input.sort()

    differences = defaultdict(int)
    current_adapter = 0

    for adapter in puzzle_input:
        adapter_diff = adapter - current_adapter

        if adapter_diff <= 3:
            current_adapter = adapter
            differences[adapter_diff] += 1

    differences[3] += 1
    return differences[1] * differences[3]


# this search implementation starts from the endpoint
# after taking the last node, it searches nodes that can be connected

# memory is a dictionary that stores amount of ways for some paths
# it helps by using cached values instead of counting again
# this reduced calculation time from being >10 sec to almost instant on my laptop
def search_ways(nodes, memory):
    ways = 0
    last = max(nodes)

    if memory.get(last, None):
        return memory[last]

    if len(nodes) <= 2:
        return 1  # there is only one path left

    # check if there devices with jolt differences 1, 2 or 3
    # if there are then search ways for each of them
    for i in range(1, 4):
        node = get_item(nodes, -i - 1, None)

        if node is not None and last - node <= 3:
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
