from dataclasses import dataclass
from shared import get_lines, sign

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

def move_tail_segment(segment: Point2D, following: Point2D) -> Point2D:
    diff = following.subtract(segment)
    if segment == following:  # Same pos, no need to move
        return segment
    if diff.y == 0 and abs(diff.x) == 1:
        return segment  # Segment is adjacent horizontally, no move
    if diff.x == 0 and abs(diff.y) == 1:
        return segment  # Segment is adjacent vertically, no move
    if abs(diff.x) == 1 and abs(diff.y) == 1:
        return segment  # Segment is diagonally adjacent, no move
    limited_dx = sign(diff.x)
    limited_dy = sign(diff.y)
    return Point2D(segment.x + limited_dx, segment.y + limited_dy)

for tail_segments in (1, 9):
    origin = Point2D(0, 0)
    hp = origin
    tp = [origin for _ in range(tail_segments)]
    tail_visited: set[Point2D] = {tp[-1]}

    for line in get_lines('../data/9.txt'):
        cmd, num_str = line.split()
        num = int(num_str)
        for _ in range(num):
            hp = hp.moved(cmd)
            tp[0] = move_tail_segment(tp[0], hp)
            for i in range(1, tail_segments):
                tp[i] = move_tail_segment(tp[i], tp[i - 1])
            tail_visited.add(tp[-1])

    print(len(tail_visited))
