from shared import get_lines

x = 1
c = 0

class Summer:
    check_cycles = [20, 60, 100, 140, 180, 220]

    def __init__(self):
        self.sum = 0

    def sum_if_time(self, cycle: int, x: int):
        if cycle in Summer.check_cycles:
            strength = cycle * x
            self.sum += strength
            print(f'{c=}, {x=}, {strength=}, {self.sum=}')

summer = Summer()

for line in get_lines('../data/10.txt'):
    print(line)
    if line == 'noop':
        c += 1
        summer.sum_if_time(c, x)
    elif line.startswith('addx '):
        v = int(line.split()[1])
        c += 1
        summer.sum_if_time(c, x)
        c += 1
        summer.sum_if_time(c, x)
        x += v
    print(f'{c=}, {x=}')

print(summer.sum)
