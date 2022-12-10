from pathlib import Path

stacks = [[] for i in range(10)]  # 0 is unused
stack, instructions = Path('../data/5.txt').read_text().rstrip().split('\n\n')
for stack_line in stack.split('\n')[:-1]:
    for stack_index in range(1, 10):
        crate_name_pos = 1 + (stack_index - 1) * 4
        if crate_name_pos < len(stack_line):
            if (crate_name := stack_line[crate_name_pos]) != ' ':
                stacks[stack_index].append(crate_name)
            print(crate_name, end='')
    print()
print(stacks)

for move_line in instructions.split('\n'):
    parts = move_line.split()
    num_move = int(parts[1])
    move_from = int(parts[3])
    move_to = int(parts[5])
    print(f'{num_move=} {move_from=} {move_to=}')
    for m in range(num_move):
        stacks[move_to].insert(0, stacks[move_from].pop(0))

for stack in stacks[1:]:
    if stack:
        print(stack[0], end='')
print()
