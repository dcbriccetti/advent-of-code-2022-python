from dataclasses import dataclass
from shared import get_string_groups

@dataclass
class Monkey:
    items: list[int]
    operator: str
    operand_str: str
    div_by: int
    throw_tos: list[int]
    inspections: int = 0

    @staticmethod
    def from_input(m: list[str]) -> 'Monkey':
        items = [int(s) for s in m[1][18:].split(', ')]
        operator = m[2][23]
        operand = m[2][25:]
        div_by = int(m[3].split()[-1])
        throw_to = [int(m[n].split()[-1]) for n in (4, 5)]
        return Monkey(items, operator, operand, div_by, throw_to)

    def act(self, monkeys: list['Monkey']) -> None:
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            operand: int = item if self.operand_str == 'old' else int(self.operand_str)
            new_val = item * operand if self.operator == '*' else item + operand
            new_val //= 3
            throw_to = self.throw_tos[new_val % self.div_by != 0]
            print(f'Throwing {new_val} to monkey {throw_to}')
            monkeys[throw_to].items.append(new_val)


monkeys = [Monkey.from_input(group) for group in get_string_groups('../data/11.txt')]

for _ in range(20):
    for i, m in enumerate(monkeys):
        print('Monkey', i)
        m.act(monkeys)

inspections = sorted([m.inspections for m in monkeys])
print(inspections[-1] * inspections[-2])
