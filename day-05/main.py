import itertools

puzzle_input = []

with open('day-5/input.txt', 'r') as file:
    puzzle_input = [i.strip() for i in file.readlines()]


def get_seat_id(entry):
    codes = convert_to_codes(entry)
    row = decode_range(list(range(0, 128)), codes[:7])
    column = decode_range(list(range(0, 8)), codes[7:])
    seat_id = row * 8 + column

    return seat_id


def convert_to_codes(letters):
    result = []
    for c in letters:
        if c == 'F':
            result.append(0)
        elif c == 'B':
            result.append(1)
        elif c == 'L':
            result.append(0)
        elif c == 'R':
            result.append(1)

    return result


def decode_range(range, codes):
    current_part = range
    for code in codes:
        current_part = split_list(current_part)[code]

    return current_part[0]


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def part_1(puzzle_input):
    return max([get_seat_id(entry) for entry in puzzle_input])


def part_2(puzzle_input):
    first_seat = min([get_seat_id(entry) for entry in puzzle_input])
    last_seat = max([get_seat_id(entry) for entry in puzzle_input])
    possible_seats = list(range(first_seat, last_seat + 1))
    taken_seats = [get_seat_id(entry) for entry in puzzle_input]

    return [item for item in possible_seats if item not in taken_seats][0]


print(part_1(puzzle_input))
print(part_2(puzzle_input))
