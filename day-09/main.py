import itertools

with open('day-09/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.readlines()]


def solution(numbers, n, result):
    a = [numbers] * n
    for i in itertools.product(*a):
        if len(set(i)) != 1 and sum(i) == result:
            return i

    return False


def part_1(puzzle_input):
    for pointer in range(25, len(puzzle_input)):
        last_nums = puzzle_input[pointer - 25:pointer]

        if not solution(last_nums, 2, puzzle_input[pointer]):
            return puzzle_input[pointer]


def part_2(puzzle_input, invalid_number):
    for i in range(2, len(puzzle_input)):
        for pointer in range(len(puzzle_input)):
            if pointer + i > len(puzzle_input):
                continue

            possible_nums = puzzle_input[pointer:pointer + i]
            if sum(possible_nums) == invalid_number:
                return sum([min(possible_nums), max(possible_nums)])


part_1_result = part_1(puzzle_input)
print(part_1_result)
print(part_2(puzzle_input, part_1_result))
