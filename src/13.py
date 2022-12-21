from enum import Enum, auto
from functools import cmp_to_key
from pathlib import Path

sum_ordered_indexes = 0
data = Path('../data/13.txt').read_text().rstrip()
groups = data.split('\n\n')

class State(Enum):
    ORDERED = auto()
    UNORDERED = auto()
    UNKNOWN = auto()

def ordered(leftx: list, rightx: list) -> State:
    left = list(leftx)
    right = list(rightx)
    while left and right:
        li = left.pop(0)
        ri = right.pop(0)
        if isinstance(li, int) and isinstance(ri, list):
            li = [li]
        elif isinstance(li, list) and isinstance(ri, int):
            ri = [ri]
        if all(isinstance(item, list) for item in (li, ri)):
            recursive_result: State = ordered(li, ri)
            if recursive_result != State.UNKNOWN:
                return recursive_result
        elif li < ri:
            return State.ORDERED
        elif li > ri:
            return State.UNORDERED
    return State.ORDERED if right and not left else \
        State.UNORDERED if left and not right else \
        State.UNKNOWN

for i, group in enumerate(groups, 1):
    left, right = [eval(p) for p in group.split('\n')]
    if ordered(left, right) == State.ORDERED:
        sum_ordered_indexes += i

print(f'{sum_ordered_indexes=}')

def compare(a, b) -> int:
    match ordered(a, b):
        case State.ORDERED:
            return -1
        case State.UNORDERED:
            return 1
        case State.UNKNOWN:
            return 0

lines = [eval(line) for line in data.split('\n') if line] + [[2], [6]]
packets = sorted(lines, key=cmp_to_key(compare))
indexes = [i for i, p in enumerate(packets, 1) if p in ([2], [6])]
product_of_indexes = indexes[0] * indexes[1]
print(f'{product_of_indexes=}')
