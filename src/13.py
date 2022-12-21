from enum import Enum, auto
from pathlib import Path

sum_ordered_indexes = 0
groups = Path('../data/13.txt').read_text().rstrip().split('\n\n')

class State(Enum):
    ORDERED = auto()
    UNORDERED = auto()
    UNKNOWN = auto()

def ordered(left: list, right: list) -> State:
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
    if right and not left:
        return State.ORDERED
    if left and not right:
        return State.UNORDERED
    return State.UNKNOWN

for i, group in enumerate(groups, 1):
    left, right = [eval(p) for p in group.split('\n')]
    print(left, right)
    if ordered(left, right) == State.ORDERED:
        sum_ordered_indexes += i

print(sum_ordered_indexes)
