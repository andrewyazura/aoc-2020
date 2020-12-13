import numpy

puzzle_input = []

with open('day-03/input.txt', 'r') as file:
    puzzle_input = [i.strip() for i in file.readlines()]


def check_slope(grid, row_shift, column_shift=1):
    trees = 0
    shift = row_shift

    for row in grid[column_shift::column_shift]:
        if row[shift] == '#':
            trees += 1

        shift = (shift + row_shift) % len(row)

    return trees


def part_1(puzzle_input):
    return check_slope(puzzle_input, 3)


def part_2(puzzle_input):
    trees = [check_slope(puzzle_input, shift, 1) for shift in range(1, 8, 2)]
    trees.append(check_slope(puzzle_input, 1, 2))

    return numpy.prod(trees)


print(part_1(puzzle_input))
print(part_2(puzzle_input))
