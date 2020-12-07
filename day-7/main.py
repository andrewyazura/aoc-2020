def find_node_in_list(name, l):
    for i in l:
        if i.name == name:
            return i

    return False


def remove_bag(string):
    string = string.replace('bags', '') if 'bags' in string else string
    string = string.replace('bag', '') if 'bag' in string else string
    return string.strip()


class LinkedList:
    def __init__(self, name):
        self.name = name
        self.next = {}

    def add_next(self, next_node, amount):
        self.next[next_node] = amount

    def contains(self, name):
        if find_node_in_list(name, self.next):
            return True

        for child in self.next:
            if child.contains(name):
                return True

        return False

    def cost(self):
        cost = 1

        for child in self.next:
            cost += self.next[child] * child.cost()

        return cost - 1

    def __repr__(self):
        return f'<LinkedListNode:{self.name}>'


with open('day-7/input.txt', 'r') as file:
    puzzle_input_raw = [i.strip() for i in file.readlines()]

puzzle_input = {}
for entry in puzzle_input_raw:
    parent, other = entry.split(' contain ')

    parent = remove_bag(parent)
    puzzle_input[parent] = {}
    for child in other.split(', '):
        if child == 'no other bags.':
            continue

        amount, name = child.replace('.', '').split(' ', 1)
        name = remove_bag(name)
        puzzle_input[parent][name] = int(amount)


puzzle_objects = []

for bag in puzzle_input:
    node = LinkedList(bag)
    puzzle_objects.append(node)

for bag in puzzle_input:
    parent = find_node_in_list(bag, puzzle_objects)

    for i in puzzle_input[bag]:
        child = find_node_in_list(i, puzzle_objects)
        parent.add_next(child, puzzle_input[bag][i])


def part_1(puzzle_input):
    return sum([bag.contains('shiny gold') for bag in puzzle_input])


def part_2(puzzle_input):
    bag = find_node_in_list('shiny gold', puzzle_input)
    return bag.cost()


print(part_1(puzzle_objects))
print(part_2(puzzle_objects))
