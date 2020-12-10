# This is a working solution, which implements depth-first search
# Unfortunately it is too inefficient and takes much time to calculate even small inputs
# I wasn't even able to get real answer for the part 2

def search_ways(start, stop, puzzle_input):
    endpoints = 0
    queue = []
    queue.extend(possible_options(start, puzzle_input))

    while queue:
        current_item = queue.pop(0)
        queue.extend(
            possible_options(
                current_item,
                puzzle_input
            )
        )

        if current_item == stop:
            endpoints += 1

    return endpoints


def possible_options(start, l):
    return [i for i in l
            if i - start <= 3 and i - start > 0]


def part_2(puzzle_input):
    puzzle_input = puzzle_input.copy()
    puzzle_input.sort()

    possible_starts = [i for i in puzzle_input if 0 < i <= 3]
    stop = max(puzzle_input)

    return sum([search_ways(start, stop, puzzle_input[1:]) for start in possible_starts])


with open('day-10/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.readlines()]

print(part_2(puzzle_input))
