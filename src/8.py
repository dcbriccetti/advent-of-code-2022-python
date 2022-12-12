from dataclasses import dataclass

from shared import get_lines
import numpy as np

@dataclass
class Tree:
    height: int
    hflags = 0

    def __repr__(self):
        return f'{self.height}-{self.hflags:X}'

a = np.array([[Tree(int(char)) for char in line] for line in get_lines('../data/8_test.txt')])
rows, cols = a.shape

def scan(row_start: int, row_end: int, col_start: int, col_end: int, flag: int):
    def sign(num: int) -> int:
        return 0 if num == 0 else num // abs(num)

    irow = row_start
    icol = col_start
    dr = sign(row_end - row_start)
    dc = sign(col_end - col_start)
    maxh = 0

    while irow != row_end or icol != col_end:
        t = a[irow, icol]
        if t.height < maxh:
            t.hflags |= flag
        elif t.height > maxh:
            maxh = t.height
        irow += dr
        icol += dc

def scan_all() -> None:
    for irow in range(0, rows):  # for every row
        scan(irow, irow, 0, cols-1, 1)  # scan left to right
        scan(irow, irow, cols-1, 0, 2)  # scan right to left

    for icol in range(0, cols):  # for every col
        scan(0, rows-1, icol, icol, 4)  # scan down
        scan(rows-1, 0, icol, icol, 8)  # scan up

scan_all()
print(a)