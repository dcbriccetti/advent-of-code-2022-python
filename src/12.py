from dataclasses import dataclass
from typing import Optional

from shared import get_lines

@dataclass
class Point:
    row: int
    col: int

    def __hash__(self) -> int:
        return hash(self.row) + hash(self.col)

    def __eq__(self, o: 'Point') -> bool:
        return self.row == o.row and self.col == o.col

    def __repr__(self) -> str:
        return f'({self.row}, {self.col})'

@dataclass
class Node:
    loc: Point
    frm: Optional['Node'] = None

start: Point = Point(0, 0)
end: Point = Point(0, 0)

def process_cell(irow: int, icol: int, ch: str) -> int:
    global start, end
    match ch:
        case 'S':
            c = 'a'
            start = Point(irow, icol)
        case 'E':
            c = 'z'
            end = Point(irow, icol)
        case _:
            c = ch
    return ord(c) - ord('a') + 1

heights = [
    [process_cell(r, c, char) for c, char in enumerate(line)]
    for r, line in enumerate(get_lines('/Users/daveb/devel/AOC-2022/data/12_test.txt'))
]

q = [Node(start, None)]
seen: set[Point] = {start}

# print(heights)
num_rows = len(heights)
num_cols = len(heights[0])
print(start, end, q, seen, num_rows, num_cols)


def enqueue_surrounding_candidates(around: Node):
    around_height = heights[around.loc.row][around.loc.col]
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r = around.loc.row + dr
        c = around.loc.col + dc
        if 0 <= r < num_rows and 0 <= c < num_cols:
            discovered_point = Point(r, c)
            if discovered_point not in seen:
                candidate_height = heights[r][c]
                height_diff = candidate_height - around_height
                if height_diff <= 1:
                    seen.add(discovered_point)
                    q.append(Node(discovered_point, around))

while q:
    node = q.pop(0)
    # print(f'popped: {node}')
    if node.loc == end:
        print('found end')
        break
    enqueue_surrounding_candidates(node)

moves = 0
n = node
with open('path.txt', 'w') as f:
    while n.frm:
        f.write(f'{n.loc.row} {n.loc.col} {heights[n.loc.row][n.loc.col]}\n')
        moves += 1
        n = n.frm
    f.write(f'{n.loc.row} {n.loc.col} {heights[n.loc.row][n.loc.col]}\n')

    print(moves)
