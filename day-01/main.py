import itertools

import numpy

puzzle_input = []

with open('day-1/input.txt', 'r') as file:
    puzzle_input = [int(i.strip()) for i in file.readlines()]


def solution(numbers, n, result):
    a = [numbers] * n
    for i in itertools.product(*a):
        if sum(i) == result:
            return numpy.prod(i)


def part_1(puzzle_input):
    return solution(puzzle_input, 2, 2020)


def part_2(puzzle_input):
    return solution(puzzle_input, 3, 2020)


print(part_1(puzzle_input))
print(part_2(puzzle_input))
