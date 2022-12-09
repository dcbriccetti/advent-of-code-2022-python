from pathlib import Path
from typing import Iterator


def get_numbers(filename) -> Iterator[int]:
    lines = Path(filename).read_text().rstrip().split('\n')
    return (int(line) for line in lines)


def list_to_int(nums_in_strings: list[str]) -> list[int]:
    return [int(num_in_string) for num_in_string in nums_in_strings]


def get_number_groups(filename) -> Iterator[list[int]]:
    groups: list[str] = Path(filename).read_text().rstrip().split('\n\n')
    return (list_to_int(group.split('\n')) for group in groups)

def get_string_groups(filename) -> Iterator[list[str]]:
    groups: list[str] = Path(filename).read_text().rstrip().split('\n')
    return (group.split() for group in groups)
