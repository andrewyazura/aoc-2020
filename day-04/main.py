from string import ascii_lowercase, digits


class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=''):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def validate(self):
        try:
            return len(self.byr) == 4 and 1920 <= int(self.byr) <= 2002 \
                and len(self.iyr) == 4 and 2010 <= int(self.iyr) <= 2020 \
                and len(self.eyr) == 4 and 2020 <= int(self.eyr) <= 2030 \
                and self._check_height() \
                and self._check_hair_color() \
                and self.ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') \
                and len(self.pid) == 9 and int(self.pid)

        except Exception as e:
            print(e)
            return False

    def _check_height(self):
        if self.hgt[-2:] == 'cm':
            return 150 <= int(self.hgt[:-2]) <= 193

        elif self.hgt[-2:] == 'in':
            return 59 <= int(self.hgt[:-2]) <= 76

        else:
            return False

    def _check_hair_color(self):
        if self.hcl[0] != '#':
            return False

        if len(self.hcl[1:]) != 6:
            return False

        for char in self.hcl[1:]:
            if char not in ascii_lowercase[:6] \
                    and char not in digits:
                return False

        return True


puzzle_input_raw = []

with open('day-04/input.txt', 'r') as file:
    puzzle_input_raw = ' '.join([i.strip() if i != '\n' else i
                                 for i in file.readlines()])

puzzle_input_raw = [[j.split(':') for j in i.split(' ') if j != '']
                    for i in puzzle_input_raw.split('\n')]

puzzle_input = []
for passport in puzzle_input_raw:
    puzzle_input.append({})
    for pair in passport:
        puzzle_input[-1][pair[0]] = pair[1]


def part_1(puzzle_input):
    valid = 0
    for passport in puzzle_input:
        try:
            p = Passport(**passport)
            valid += 1
        except:
            pass

    return valid


def part_2(puzzle_input):
    valid = 0
    for passport in puzzle_input:
        try:
            p = Passport(**passport)
            if p.validate():
                valid += 1
        except:
            pass

    return valid


print(part_1(puzzle_input))
print(part_2(puzzle_input))
