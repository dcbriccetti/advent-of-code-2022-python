from shared import get_lines

class ORange:
    def __init__(self, range_string: str):
        self.start, self.stop = [int(n) for n in range_string.split('-')]

    def __repr__(self):
        return f'{self.start}-{self.stop}'

    def contains(self, other: 'ORange') -> bool:
        return other.start >= self.start and other.stop <= self.stop

lines = get_lines('../data/4.txt')

num_contained = 0
for line in lines:
    r1, r2 = [ORange(r) for r in line.split(',')]
    if r1.contains(r2) or r2.contains(r1):
        num_contained += 1
print(num_contained)
