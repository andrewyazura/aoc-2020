with open('day-12/input.txt', 'r') as file:
    puzzle_input = [i.strip() for i in file.readlines()]


def part_1(puzzle_input):
    x = 0
    y = 0
    d = 1
    directions = ['N', 'E', 'S', 'W']

    for entry in puzzle_input:
        direction, value = entry[0], int(entry[1:])

        if direction == 'F':
            direction = directions[int(d)]

        if direction == 'N':
            y += value

        elif direction == 'S':
            y -= value

        elif direction == 'W':
            x -= value

        elif direction == 'E':
            x += value

        elif direction == 'L':
            d -= value / 90
            d %= len(directions)

        elif direction == 'R':
            d += value / 90
            d %= len(directions)

    return abs(x) + abs(y)


def part_2(puzzle_input):
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = 1

    for entry in puzzle_input:
        direction, value = entry[0], int(entry[1:])

        if direction == 'F':
            x += waypoint_x * value
            y += waypoint_y * value

        elif direction == 'N':
            waypoint_y += value

        elif direction == 'S':
            waypoint_y -= value

        elif direction == 'W':
            waypoint_x -= value

        elif direction == 'E':
            waypoint_x += value

        elif direction == 'L':
            waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, -value)

        elif direction == 'R':
            waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, value)

    return abs(x) + abs(y)


def rotate(wx, wy, angle):
    turns = (angle // 90) % 4

    if turns == 1:
        return wy, -wx
    elif turns == 2:
        return -wx, -wy
    elif turns == 3:
        return -wy, wx


print(part_1(puzzle_input))
print(part_2(puzzle_input))
