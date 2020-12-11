import copy
from pprint import pprint

with open('day-11/input.txt', 'r') as file:
    puzzle_input = [list(i.strip()) for i in file.readlines()]

taken = '#'
empty = 'L'
floor = '.'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point:{self.x}:{self.y}>'


def is_occupied(grid, point):
    if point_in_grid(grid, point):
        return True if grid[point.y][point.x] == taken else False

    return False


def direction_occupied(grid, point, direction):
    curr_point = Point(point.x + direction[0], point.y + direction[1])

    while point_in_grid(grid, curr_point):
        if grid[curr_point.y][curr_point.x] == empty:
            return False

        if grid[curr_point.y][curr_point.x] == taken:
            return True

        curr_point = Point(
            curr_point.x + direction[0], curr_point.y + direction[1])

    return False


def is_empty(grid, point):
    if point_in_grid(grid, point):
        return True if grid[point.y][point.x] == empty else False

    return False


def is_floor(grid, point):
    if point_in_grid(grid, point):
        return True if grid[point.y][point.x] == floor else False

    return False


def point_in_grid(grid, point):
    return 0 <= point.y < len(grid) and 0 <= point.x < len(grid[point.y])


def count_occupied(grid):
    counter = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == taken:
                counter += 1

    return counter


def count_occupied_neighbors(grid, point):
    taken = 0
    taken += is_occupied(grid, Point(point.x, point.y - 1))
    taken += is_occupied(grid, Point(point.x, point.y + 1))

    taken += is_occupied(grid, Point(point.x - 1, point.y))
    taken += is_occupied(grid, Point(point.x + 1, point.y))

    taken += is_occupied(grid, Point(point.x + 1, point.y - 1))
    taken += is_occupied(grid, Point(point.x + 1, point.y + 1))

    taken += is_occupied(grid, Point(point.x - 1, point.y - 1))
    taken += is_occupied(grid, Point(point.x - 1, point.y + 1))

    return taken


def count_occupied_directions(grid, point):
    taken = 0
    taken += direction_occupied(grid, point, (0, -1))
    taken += direction_occupied(grid, point, (0, +1))

    taken += direction_occupied(grid, point, (-1, 0))
    taken += direction_occupied(grid, point, (+1, 0))

    taken += direction_occupied(grid, point, (+1, -1))
    taken += direction_occupied(grid, point, (+1, +1))

    taken += direction_occupied(grid, point, (-1, -1))
    taken += direction_occupied(grid, point, (-1, +1))

    return taken


def populate_grid(data_grid, count_method, empty_on):
    apply_grid = copy.deepcopy(data_grid)

    for y in range(len(data_grid)):
        for x in range(len(data_grid[0])):
            current_point = Point(x, y)

            if is_floor(data_grid, current_point):
                continue

            if is_empty(data_grid, current_point) \
                    and count_method(data_grid, current_point) == 0:
                apply_grid[current_point.y][current_point.x] = taken

            if is_occupied(data_grid, current_point) \
                    and count_method(data_grid, current_point) >= empty_on:
                apply_grid[current_point.y][current_point.x] = empty

    return apply_grid


def part_1(puzzle_input):
    grid = copy.deepcopy(puzzle_input)
    old_grid = []

    while grid != old_grid:
        old_grid = copy.deepcopy(grid)
        grid = populate_grid(old_grid, count_occupied_neighbors, 4)

    return count_occupied(grid)


def part_2(puzzle_input):
    grid = copy.deepcopy(puzzle_input)
    old_grid = []

    while grid != old_grid:
        old_grid = copy.deepcopy(grid)
        grid = populate_grid(old_grid, count_occupied_directions, 5)

    return count_occupied(grid)


print(part_1(puzzle_input))
print(part_2(puzzle_input))
