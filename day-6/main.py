from string import ascii_lowercase

with open('day-6/input.txt', 'r') as file:
    puzzle_input_raw = [i.strip() if i != '\n' else i
                        for i in file.readlines()]

puzzle_input = [[]]
for entry in puzzle_input_raw:
    if entry == '\n':
        puzzle_input.append([])
        continue

    puzzle_input[-1].append(entry.strip())


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
