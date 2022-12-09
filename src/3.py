from shared import get_lines

sacks = get_lines('../data/3.txt')

def part1():
    print(sum(find_priority(sack) for sack in sacks))

def find_priority(sack):
    half_len = len(sack) // 2
    compartment1 = sack[:half_len]
    compartment2 = sack[half_len:]
    compartment1_chars = set(compartment1)
    in_both: str = [c for c in compartment2 if c in compartment1_chars][0]
    sub_val, offset = ('a', 0) if in_both.islower() else ('A', 26)
    priority = ord(in_both) - ord(sub_val) + 1 + offset
    return priority

part1()
