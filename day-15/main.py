puzzle_input = [1, 2, 16, 19, 18, 0]


def game(puzzle_input, stop_number):
    memory = {n: i for i, n in enumerate(puzzle_input)}
    current_number = 0
    next_number = 0

    for i in range(len(puzzle_input), stop_number):
        current_number = next_number
        if current_number in memory:
            next_number = i - memory[current_number]
        else:
            next_number = 0

        memory[current_number] = i

    return current_number


def part_1(puzzle_input):
    return game(puzzle_input, 2020)


def part_2(puzzle_input):
    return game(puzzle_input, 30000000)


print(part_1(puzzle_input))
print(part_2(puzzle_input))
