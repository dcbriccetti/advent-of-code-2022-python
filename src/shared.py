from pathlib import Path
from typing import Iterator

def get_numbers(filename) -> Iterator[int]:
    return (int(line) for line in get_lines(filename))

def get_lines(filename: str) -> list[str]:
    return Path(filename).read_text().rstrip().split('\n')

def list_to_int(nums_in_strings: list[str]) -> list[int]:
    return [int(num_in_string) for num_in_string in nums_in_strings]

def get_number_groups(filename: str) -> Iterator[list[int]]:
    groups: list[str] = get_blank_separated_groups(filename)
    return (list_to_int(group.split('\n')) for group in groups)

def get_string_groups(filename: str) -> Iterator[list[str]]:
    groups: list[str] = get_blank_separated_groups(filename)
    return (group.split('\n') for group in groups)

def get_blank_separated_groups(filename: str) -> list[str]:
    return Path(filename).read_text().rstrip().split('\n\n')

def sign(num: int) -> int:
    return 0 if num == 0 else num // abs(num)
