from shared import get_number_groups

number_groups: list[list[int]] = list(get_number_groups('data/1.txt'))
group_sums = [sum(group) for group in number_groups]

def part1():
    print(max(group_sums))

def part2():
    print(sum(sorted(group_sums, reverse=True)[:3]))

part1()
part2()

