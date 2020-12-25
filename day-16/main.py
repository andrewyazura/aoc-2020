with open('day-16/input.txt', 'r') as file:
    puzzle_input = [i.splitlines() for i in file.read().split('\n\n')]

input_filters = {}
for entry in puzzle_input[0]:
    name, ranges = entry.split(': ')
    input_filters[name] = [[int(i) for i in r.split('-')]
                           for r in ranges.split(' or ')]

your_ticket = [int(i) for i in puzzle_input[1][1].split(',')]
other_tickets = [[int(i) for i in ticket.split(',')]
                 for ticket in puzzle_input[2][1:]]


def valid_value(value, ranges):
    return any([r[0] <= value <= r[1] for r in ranges])


def invalid_value(value, filters):
    return not any([r[0] <= value <= r[1] for ranges in filters.values() for r in ranges])


def part_1(tickets, filters):
    return sum([value for ticket in tickets for value in ticket if invalid_value(value, filters)])


def part_2(my_ticket, tickets, filters):
    valid_tickets = [ticket for ticket in tickets if not any(
        invalid_value(value, filters) for value in ticket)]
    valid_tickets.append(my_ticket)

    prod = 1
    unused_indexes = list(range(len(filters)))
    while unused_indexes:
        columns = [[ticket[i] for ticket in valid_tickets]
                   for i in unused_indexes]

        for name, ranges in filters.items():
            possible_columns = [column for column in columns if all(
                [valid_value(value, ranges) for value in column])]

            if len(possible_columns) == 1:
                index = my_ticket.index(possible_columns[0][-1])
                filters[name] = []
                unused_indexes.remove(index)

                if name.startswith('departure'):
                    prod *= my_ticket[index]

    return prod


print(part_1(other_tickets, input_filters))
print(part_2(your_ticket, other_tickets, input_filters))
