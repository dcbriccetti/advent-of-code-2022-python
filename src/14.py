from dataclasses import dataclass
from enum import Enum, auto
from itertools import pairwise
from typing import Optional
from shared import get_lines, sign

ABYSS_CHECK_LIMIT = 1000

class Matter(Enum):
    ROCK = auto()
    SAND = auto()

@dataclass
class Point:
    x: int
    y: int

    @staticmethod
    def from_str(s: str) -> 'Point':
        return Point(*[int(p) for p in s.split(',')])

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def point_towards(self, other: 'Point') -> 'Point':
        dx = sign(other.x - self.x)
        dy = sign(other.y - self.y)
        return Point(self.x + dx, self.y + dy)

    def __eq__(self, o: 'Point') -> bool:
        return self.x == o.x and self.y == o.y

    def __add__(self, o: 'Point'):
        return Point(self.x + o.x, self.y + o.y)

@dataclass
class Sand:
    loc: Point
    drops = [Point(x, y) for x, y in [(0, 1), (-1, 1), (1, 1)]]

    def moved(self):
        can_go = [self.loc + drop for drop in self.drops if self.loc + drop not in space]
        return Sand(can_go[0]) if can_go else None

def add_rocks():
    for line in lines:
        points = line.split(' -> ')
        for fm_to_pair in pairwise(points):
            current, last = [Point.from_str(i) for i in fm_to_pair]
            while current != last:
                space[current] = Matter.ROCK
                current = current.point_towards(last)
        space[current] = Matter.ROCK

def move_sand():
    sand_falls_before_abyss = 0
    while True:
        sand_falls_before_abyss += 1
        sand = Sand(Point(500, 0))
        moving = True
        while moving and sand.loc.y < ABYSS_CHECK_LIMIT:
            sand_at_new_loc = sand.moved()
            if sand_at_new_loc:
                sand = sand_at_new_loc  # print(f'sand now at {sand.loc}')
            else:
                # print('sand rests')
                space[sand.loc] = Matter.SAND
                moving = False
        if moving:
            sand_falls_before_abyss -= 1
            break
    print(f'{sand_falls_before_abyss=}')

def save_cave_to_file(min_x: int, max_x: int, min_y: int, max_y: int):
    with open('caves.txt', 'w') as f:
        for y in range(min_y, max_y + 1):
            line = ''
            for x in range(min_x, max_x + 1):
                item: Optional[Matter] = space.get(Point(x, y))
                line += 'o' if item == Matter.SAND else '#' if item == Matter.ROCK else '.'
            assert len(line) == max_x - min_x + 1
            f.write(line + '\n')

def get_cave_dimensions() -> (int, int, int, int):
    xs = [k.x for k, v in space.items()]
    ys = [k.y for k, v in space.items()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    print(f'{min_x=}, {max_x=}, {min_y=}, {max_y=}')
    return min_x, max_x, min_y, max_y

space: dict[Point, Matter] = dict()
lines = get_lines('../data/14.txt')

add_rocks()
min_x, max_x, min_y, max_y = get_cave_dimensions()
floor_y = max_y + 2
move_sand()
save_cave_to_file(min_x, max_x, min_y, max_y)
