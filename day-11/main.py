import copy

with open('day-11/input.txt', 'r') as file:
    puzzle_input = [list(i.strip()) for i in file.readlines()]


class Grid:
    def __init__(self, init_2d_array, threshold):
        self.grid = init_2d_array
        self.threshold = threshold

        self.occupied = '#'
        self.empty = 'L'
        self.floor = '.'

        self.adjacent = [
            (0, 1),
            (0, -1),

            (1, 1),
            (1, 0),
            (1, -1),

            (-1, 1),
            (-1, 0),
            (-1, -1),
        ]

    def process_until_static(self):
        old_grid = None

        while old_grid != self.grid:
            old_grid = copy.deepcopy(self.grid)
            self.process_grid()

        return self.count_occupied()

    def process_grid(self):
        compare_grid = copy.deepcopy(self.grid)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                occupied_around = self.count_occupied_adjacent(
                    compare_grid, x, y)

                if compare_grid[y][x] == self.empty \
                        and occupied_around == 0:
                    self.grid[y][x] = self.occupied

                elif compare_grid[y][x] == self.occupied \
                        and occupied_around >= self.threshold:
                    self.grid[y][x] = self.empty

    def count_occupied_adjacent(self, grid, x, y):
        adjacent = self.get_adjacent(grid, x, y)
        return adjacent.count(self.occupied)

    def get_adjacent(self, grid, x, y):
        return [grid[y + pair[1]][x + pair[0]]
                for pair in self.adjacent
                if self.coords_exist(x + pair[0], y + pair[1])]

    def coords_exist(self, x, y):
        return 0 <= y < len(self.grid) and 0 <= x < len(self.grid[y])

    def count_occupied(self):
        return sum([row.count(self.occupied) for row in self.grid])

    def __repr__(self):
        return f'<Grid:{len(self.grid[0])}:{len(self.grid)}>'


def part_1(puzzle_input):
    grid = Grid(puzzle_input, 4)
    return grid.process_until_static()


print(part_1(puzzle_input))
