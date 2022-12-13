from dataclasses import dataclass

from shared import get_lines

@dataclass
class Point2D:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

    def __eq__(self, o: 'Point2D') -> bool:
        return self.x == o.x and self.y == o.y

    def moved(self, dir: str) -> 'Point2D':
        dx, dy = {
            'R': ( 1,  0),
            'L': (-1,  0),
            'U': ( 0,  1),
            'D': ( 0, -1),
        }[dir]
        return Point2D(self.x + dx, self.y + dy)

    def subtract(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x - other.x, self.y - other.y)

def move_tail(tail: Point2D, head: Point2D) -> Point2D:
    diff = head.subtract(tail)
    if tail == head:  # Same pos, no need to move
        return tail
    if diff.y == 0 and abs(diff.x) == 1:
        return tail  # Tail is adjacent horizontally, no move
    if diff.x == 0 and abs(diff.y) == 1:
        return tail  # Tail is adjacent vertically, no move
    if abs(diff.x) == 1 and abs(diff.y) == 1:
        return tail  # Tail is diagonally adjacent, no move
    limited_dx = 0 if diff.x == 0 else diff.x // abs(diff.x)
    limited_dy = 0 if diff.y == 0 else diff.y // abs(diff.y)
    return Point2D(tail.x + limited_dx, tail.y + limited_dy)

hp = Point2D(0, 0)
tp = Point2D(0, 0)
tail_visited: set[Point2D] = {tp}

for line in get_lines('../data/9.txt'):
    cmd, num_str = line.split()
    num = int(num_str)
    for _ in range(num):
        hp = hp.moved(cmd)
        tp = move_tail(tp, hp)
        tail_visited.add(tp)

print(len(tail_visited))
