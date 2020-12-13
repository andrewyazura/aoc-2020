class CodeInterpreter:
    def __init__(self, memory, stop_on_repeat=False):
        self.memory = memory
        self.pointer = 0
        self.accumulator = 0

        self.stop_on_repeat = stop_on_repeat

        self.used_pointers = []
        self.commands = {
            'nop': {'func': self._no_operation},
            'acc': {'func': self._accumulate},
            'jmp': {'func': self._jump}
        }

    def _accumulate(self, param):
        self.accumulator += int(param)
        self.pointer += 1

    def _jump(self, param):
        self.pointer += int(param)

    def _no_operation(self, param):
        self.pointer += 1

    def execute(self):
        while self.pointer < len(self.memory):
            if self.stop_on_repeat and self.pointer in self.used_pointers:
                return self.accumulator, 0

            self.used_pointers.append(self.pointer)
            op_name, param = self.read_instruction()

            op_func = self.commands[op_name]['func']
            op_func(param)

        return self.accumulator, 1

    def read_instruction(self):
        operation, parameter = self.memory[self.pointer].split(' ')
        return operation, int(parameter)


def find_strings_in_list(l, substring):
    pointers = []

    for i in range(len(l)):
        if substring in l[i]:
            pointers.append(i)

    return pointers


with open('day-08/input.txt', 'r') as file:
    puzzle_input = [i.strip() for i in file.readlines()]


def part_1(puzzle_input):
    interpreter = CodeInterpreter(puzzle_input, stop_on_repeat=True)
    return interpreter.execute()[0]


def part_2(puzzle_input):
    count_jmp = find_strings_in_list(puzzle_input, 'jmp')
    count_nop = find_strings_in_list(puzzle_input, 'nop')

    for pointer in count_jmp:
        new_input = puzzle_input.copy()
        new_input[pointer] = new_input[pointer].replace('jmp', 'nop')

        interpreter = CodeInterpreter(new_input, stop_on_repeat=True)
        r = interpreter.execute()
        if r[1] == 1:
            return r[0]

    for pointer in count_nop:
        new_input = puzzle_input.copy()
        new_input[pointer] = new_input[pointer].replace('nop', 'jmp')

        interpreter = CodeInterpreter(new_input, stop_on_repeat=True)
        r = interpreter.execute()
        if r[1] == 1:
            return r[0]


print(part_1(puzzle_input))
print(part_2(puzzle_input))
