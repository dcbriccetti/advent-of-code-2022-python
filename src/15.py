import re
from dataclasses import dataclass
from typing import Iterable, Optional

from shared import get_lines

INTERESTING_ROW = 2_000_000

@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

    def __eq__(self, o: 'Point') -> bool:
        return self.x == o.x and self.y == o.y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def manhattan_distance(self, other: 'Point') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def points_within_manhattan_distance(self, distance: int) -> Iterable['Point']:
        top = self.y - distance
        for y in range(top, self.y + distance + 1):
            if y != INTERESTING_ROW:
                continue
            y_dist_from_sensor = abs(y - self.y)
            avail_x = distance - y_dist_from_sensor
            for x in range(self.x - avail_x, self.x + avail_x + 1):
                if x == self.x and y == self.y:  # The sensor is here
                    print('sensor here')
                    continue
                yield Point(x, y)

def signed_num(num: str, sign: Optional[str]) -> int:
    return int(num) * (-1 if sign == '-' else 1)

no_beacons_at: set[Point] = set()
beacons_at: set[Point] = set()

for line in get_lines('../data/15.txt'):
    print(line)
    m = re.match(r'Sensor at x=(-?)(\d+), y=(-?)(\d+): .*x=(-?)(\d+), y=(-?)(\d+)', line)
    g = m.groups()
    sensor = Point(signed_num(g[1], g[0]), signed_num(g[3], g[2]))
    beacon = Point(signed_num(g[5], g[4]), signed_num(g[7], g[6]))
    beacons_at.add(beacon)
    distance = sensor.manhattan_distance(beacon)
    no_beacons_at.update(sensor.points_within_manhattan_distance(distance))

print(len(no_beacons_at) - len([b for b in beacons_at if b.y == INTERESTING_ROW]))
