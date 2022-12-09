from shared import get_lines

sacks = get_lines('../data/3.txt')

def part1():
    print(sum(find_sack_priority(sack) for sack in sacks))

def part2():
    print(sum(find_group_priorities()))

def groups():
    for i in range(0, len(sacks), 3):
        yield sacks[i:i+3]

def find_group_priorities():
    for group in groups():
        group_sets = [set(sack) for sack in group]
        char_in_common = list(group_sets[0] & group_sets[1] & group_sets[2])[0]
        yield find_char_priority(char_in_common)

def find_sack_priority(sack):
    half_len = len(sack) // 2
    compartment1 = sack[:half_len]
    compartment2 = sack[half_len:]
    compartment1_chars = set(compartment1)
    in_both: str = [c for c in compartment2 if c in compartment1_chars][0]
    priority = find_char_priority(in_both)
    return priority


def find_char_priority(in_both: str) -> int:
    sub_val, offset = ('a', 0) if in_both.islower() else ('A', 26)
    priority = ord(in_both) - ord(sub_val) + 1 + offset
    return priority

part1()
part2()
