from typing import Iterable
from shared import get_lines

def part1() -> None:
    print(sum(find_sack_priority(sack) for sack in sacks))

def part2() -> None:
    print(sum(find_group_priorities()))

def groups() -> Iterable[str]:
    for i in range(0, len(sacks), 3):
        yield sacks[i:i+3]

def find_group_priorities() -> Iterable[int]:
    for group in groups():
        group_sets = [set(sack) for sack in group]
        char_in_common = list(group_sets[0] & group_sets[1] & group_sets[2])[0]
        yield find_char_priority(char_in_common)

def find_sack_priority(sack: str) -> int:
    half_len = len(sack) // 2
    compartment1, compartment2 = sack[:half_len], sack[half_len:]
    compartment1_chars = set(compartment1)
    char_in_both: str = [c for c in compartment2 if c in compartment1_chars][0]
    return find_char_priority(char_in_both)


def find_char_priority(char: str) -> int:
    subtract_val, offset = ('a', 0) if char.islower() else ('A', 26)
    return ord(char) - ord(subtract_val) + 1 + offset

sacks: list[str] = get_lines('../data/3.txt')

part1()
part2()
