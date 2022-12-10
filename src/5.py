from pathlib import Path

def load_stacks():
    stacks = [[] for _ in range(10)]  # 0 is unused
    for stack_line in stack.split('\n')[:-1]:
        for stack_index in range(1, 10):
            crate_name_pos = 1 + (stack_index - 1) * 4
            if crate_name_pos < len(stack_line):
                if (crate_name := stack_line[crate_name_pos]) != ' ':
                    stacks[stack_index].append(crate_name)
    return stacks

for part in range(1, 3):
    stack, move_lines = Path('../data/5.txt').read_text().rstrip().split('\n\n')
    stacks = load_stacks()
    print(stacks)

    for move_line in move_lines.split('\n'):
        parts = move_line.split()
        num_move = int(parts[1])
        move_from = int(parts[3])
        move_to = int(parts[5])
        # print(f'{num_move=} {move_from=} {move_to=}')
        for i, m in enumerate(range(num_move)):
            pop_index = num_move - i - 1 if part == 2 else 0
            stacks[move_to].insert(0, stacks[move_from].pop(pop_index))

    for stack in stacks[1:]:
        if stack:
            print(stack[0], end='')
    print()
