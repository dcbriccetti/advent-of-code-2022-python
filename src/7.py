from dataclasses import dataclass, field
from typing import Optional, Union

from shared import get_lines

@dataclass
class Dir:
    name: str
    parent: Optional['Dir'] = None
    children: list[Union['Dir', 'File']] = field(default_factory=list)

    def size(self, collector: (int, None)) -> int:
        tot = 0
        for child in self.children:
            tot += (child.size(collector) if isinstance(child, Dir) else child.size)
        collector(tot)
        return tot

@dataclass
class File:
    name: str
    size: int
    parent: Dir

def build_directory_structure():
    root_dir = Dir('/')
    current_dir = root_dir
    for line in get_lines('../data/7.txt'):
        parts = line.split()
        if line == '$ cd /':
            current_dir = root_dir
        elif line == '$ cd ..':
            current_dir = current_dir.parent
        elif line.startswith('$ cd '):
            current_dir = \
            [child for child in current_dir.children if isinstance(child, Dir) and child.name == parts[2]][0]
        elif line == '$ ls':
            pass
        elif parts[0] == 'dir':
            current_dir.children.append(Dir(parts[1], current_dir))
        elif parts[0].isnumeric():
            current_dir.children.append(File(parts[1], int(parts[0]), current_dir))
        else:
            print('oops')
    return root_dir

def compute_results():
    class Collector:
        def __init__(self):
            self.sum_of_sizes = 0
            self.sizes: list[int] = []

        def collect(self, size: int):
            self.sizes.append(size)
            if size <= 100_000:
                self.sum_of_sizes += size

    collector = Collector()
    print(f'{root_dir.size(collector.collect)=}')
    print(f'{collector.sum_of_sizes=}')
    collector.sizes.sort()
    unused_space = 70_000_000 - collector.sizes[-1]
    needed_space = 30_000_000 - unused_space
    print(f'{unused_space=}, {needed_space=}')
    candidates = [s for s in collector.sizes if s >= needed_space]
    print(f'{candidates[0]=}')

root_dir = build_directory_structure()
compute_results()
