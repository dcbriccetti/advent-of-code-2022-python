from shared import get_lines

heights = [[int(char) for char in line] for line in get_lines('../data/8.txt')]
for ir in range(len(heights)):
    for ic in range(len(heights[0])):
        print(f'translate([{ic},{ir},0]) {{')
        print(f'  cube([1, 1, {heights[ir][ic]}]);')
        print('}')
