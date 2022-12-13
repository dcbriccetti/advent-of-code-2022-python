from dataclasses import dataclass
from shared import get_lines, sign
import numpy as np

def part1() -> None:
    @dataclass
    class Tree:
        height: int
        visible = False

        def __repr__(self):
            return f'{self.height}{str(self.visible)[0]}'

    def scan(row_start: int, row_end: int, col_start: int, col_end: int) -> None:
        irow = row_start
        icol = col_start
        dr = sign(row_end - row_start)
        dc = sign(col_end - col_start)
        maxh = -1

        while irow != row_end or icol != col_end:
            t = forest[irow, icol]
            if t.height > maxh:
                t.visible = True
            if t.height > maxh:
                maxh = t.height
            irow += dr
            icol += dc

    def scan_all() -> None:
        for irow in range(0, rows):  # for every row
            scan(irow, irow, 0, cols - 1)  # scan left to right
            scan(irow, irow, cols - 1, 0)  # scan right to left

        for icol in range(0, cols):  # for every col
            scan(0, rows - 1, icol, icol)  # scan down
            scan(rows - 1, 0, icol, icol)  # scan up

    forest = np.array([[Tree(int(char)) for char in line] for line in get_lines('../data/8.txt')])
    rows, cols = forest.shape
    scan_all()
    print(forest)

    num_visible = 0
    for r in range(rows):
        for c in range(cols):
            if forest[r, c].visible:
                num_visible += 1
    print(num_visible)

def part2() -> None:
    def find_scenic_score(irow: int, icol: int):
        height = forest[irow, icol]

        lsc = 0
        for ic in range(icol - 1, -1, -1):
            lsc += 1
            if forest[irow, ic] >= height:
                break

        rsc = 0
        for ic in range(icol + 1, cols):
            rsc += 1
            if forest[irow, ic] >= height:
                break

        usc = 0
        for ir in range(irow - 1, -1, -1):
            usc += 1
            if forest[ir, icol] >= height:
                break

        dsc = 0
        for ir in range(irow + 1, rows):
            dsc += 1
            if forest[ir, icol] >= height:
                break

        score = lsc * rsc * usc * dsc
        print(f'{lsc=} {rsc=} {usc=} {dsc} = {score}')
        return score

    forest = np.array([[int(char) for char in line] for line in get_lines('../data/8.txt')])
    rows, cols = forest.shape
    highest_score = 0
    for irow in range(1, rows - 1):
        for icol in range(1, cols - 1):
            score = find_scenic_score(irow, icol)
            if score > highest_score:
                highest_score = score
    print(highest_score)

# part1()
part2()
