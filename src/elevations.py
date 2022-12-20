from pathlib import Path

def get_lines(filename: str) -> list[str]:
    return Path(filename).read_text().rstrip().split('\n')

def to_num(ch: str) -> int:
    match ch:
        case 'S':
            c = 'a'
        case 'E':
            c = 'z'
        case _:
            c = ch
    return ord(c) - ord('a') + 1

heights = [[to_num(char) for char in line] for line in get_lines('/Users/daveb/devel/AOC-2022/data/12_test.txt')]
for ir in range(len(heights)):
    for ic in range(len(heights[0])):
        print(f'translate([{ic},{ir},0]) {{')
        print(f'  cube([1, 1, {heights[ir][ic]}]);')
        print('}')
