

class Monkey:
    def __init__(self, items, operation, test_val, true_target, false_target):
        self.items = items
        self.operation = operation
        self.test_val = test_val
        self.pass_targets = {True: true_target, False: false_target}
        self.inspections = 0

    def do_round(self, divide_worry=True, prod_mods=1):
        for worry in self.items:
            worry = self.operation(worry)
            if divide_worry:
                worry //= 3
            else:
                worry %= prod_mods
            all_monkeys[self.pass_targets[worry % self.test_val == 0]].items.append(worry)
            self.inspections += 1
        self.items = []


all_monkeys = [
    Monkey([98, 97, 98, 55, 56, 72], lambda x: x * 13, 11, 4, 7),
    Monkey([73, 99, 55, 54, 88, 50, 55], lambda x: x + 4, 17, 2, 6),
    Monkey([67, 98], lambda x: x * 11, 5, 6, 5),
    Monkey([82, 91, 92, 53, 99], lambda x: x + 8, 13, 1, 2),
    Monkey([52, 62, 94, 96, 52, 87, 53, 60], lambda x: x * x, 19, 3, 1),
    Monkey([94, 80, 84, 79], lambda x: x + 5, 2, 7, 0),
    Monkey([89], lambda x: x + 1, 3, 0, 5),
    Monkey([70, 59, 63], lambda x: x + 3, 7, 4, 3)
]


def part1():
    for i in range(20):
        for monkey in all_monkeys:
            monkey.do_round()

    sorted_sol = sorted([i.inspections for i in all_monkeys])[-2:]
    print(sorted_sol[0] * sorted_sol[1])


def part2():
    prod_mods = 1
    for monkey in all_monkeys:
        prod_mods *= monkey.test_val

    for i in range(10000):
        for monkey in all_monkeys:
            monkey.do_round(False, prod_mods)

    sorted_sol = sorted([i.inspections for i in all_monkeys])[-2:]
    print(sorted_sol[0] * sorted_sol[1])


if __name__ == '__main__':
    part2()