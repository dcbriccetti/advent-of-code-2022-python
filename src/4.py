from shared import get_lines

class Range:
    def __init__(self, range_string: str):
        self.start, self.stop = [int(n) for n in range_string.split('-')]

    def __repr__(self):
        return f'{self.start}-{self.stop}'

    def contains(self, other: 'Range') -> bool:
        return other.start >= self.start and other.stop <= self.stop

    def overlaps(self, other: 'Range') -> bool:
        return self.start <= other.start <= self.stop or self.start <= other.stop <= self.stop

num_contained = 0
num_overlaps = 0
for line in get_lines('../data/4.txt'):
    r1, r2 = [Range(r) for r in line.split(',')]
    if r1.contains(r2) or r2.contains(r1):
        num_contained += 1
    if r1.overlaps(r2) or r2.overlaps(r1):
        num_overlaps += 1
print(f'{num_contained=}, {num_overlaps=}')
