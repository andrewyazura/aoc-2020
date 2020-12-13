from string import ascii_lowercase

with open('day-06/input.txt', 'r') as file:
    puzzle_input = [i.splitlines() for i in file.read().split('\n\n')]


def char_in_nested_list(char, nested_list):
    for item in nested_list:
        if char not in item:
            return False

    return True


def part_1(puzzle_input):
    group_answers = []
    for group in puzzle_input:
        answers = ''.join(group)
        group_answers.append(set(answers))

    return sum([len(i) for i in group_answers])


def part_2(puzzle_input):
    group_answers = []
    for group in puzzle_input:
        answers = []

        for char in ascii_lowercase:
            if char_in_nested_list(char, group):
                answers.append(char)

        group_answers.append(set(answers))

    return sum([len(i) for i in group_answers])


print(part_1(puzzle_input))
print(part_2(puzzle_input))
