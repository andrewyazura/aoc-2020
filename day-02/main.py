import re

puzzle_input = []

with open('day-02/input.txt', 'r') as file:
    puzzle_input = [i.strip() for i in file.readlines()]

puzzle_template = '(\d+)-(\d+) (\w): (\w+)'
puzzle_regex = re.compile(puzzle_template)


def part_1(puzzle_input):
    valid = 0

    for entry in puzzle_input:
        a, b, letter, password = puzzle_regex.match(entry).groups()
        amount = password.count(letter)

        if int(a) <= amount <= int(b):
            valid += 1

    return valid


def part_2(puzzle_input):
    valid = 0

    for entry in puzzle_input:
        a, b, letter, password = puzzle_regex.match(entry).groups()
        a = int(a) - 1
        b = int(b) - 1

        if (password[a] == letter or password[b] == letter) \
                and not (password[a] == letter and password[b] == letter):
            valid += 1

    return valid


print(part_1(puzzle_input))
print(part_2(puzzle_input))
