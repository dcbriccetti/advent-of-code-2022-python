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
        print(f'size of {self.name}: {tot}')
        collector(tot)
        return tot

@dataclass
class File:
    name: str
    size: int
    parent: Dir

lines = get_lines('../data/7.txt')
root_dir = Dir('/')
current_dir = root_dir

for line in lines:
    parts = line.split()
    print(line)
    if line == '$ cd /':
        current_dir = root_dir
    elif line == '$ cd ..':
        current_dir = current_dir.parent
    elif line.startswith('$ cd '):
        for child in current_dir.children:
            if isinstance(child, Dir) and child.name == parts[2]:
                current_dir = child
                break
    elif line == '$ ls':
        pass
    elif parts[0] == 'dir':
        current_dir.children.append(Dir(parts[1], current_dir))
    elif parts[0].isnumeric():
        current_dir.children.append(File(parts[1], int(parts[0]), current_dir))
    else:
        print('oops')

sum_of_sizes = 0
def collector(size: int):
    global sum_of_sizes
    if size <= 100_000:
        sum_of_sizes += size

print(root_dir.size(collector))
print(sum_of_sizes)
