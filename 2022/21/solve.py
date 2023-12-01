import sympy


def part1():
    monkeys = parse()

    def rec(key):
        vals = monkeys[key]
        if len(vals) == 1:
            return int(vals[0])
        else:
            return eval(f'{rec(vals[0])}{vals[1]}{rec(vals[2])}')

    print(rec('root'))


def part2():
    monkeys = parse()
    x = sympy.symbols('x')

    def rec(key):
        if key == 'humn':
            return x
        vals = monkeys[key]
        if len(vals) == 1:
            return int(vals[0])
        else:
            return f'({rec(vals[0])}{vals[1]}{rec(vals[2])})'

    root_node = monkeys['root']
    l_side, r_side = eval(rec(root_node[0])), eval(rec(root_node[2]))

    print(sympy.solve(l_side - r_side, x))


def parse():
    monkeys = {}
    with open('input.txt') as f:
        for l in map(str.strip, f.readlines()):
            l = l.split(' ')
            key = l[0].strip(':')
            vals = l[1:]
            monkeys[key] = vals
    return monkeys


if __name__ == '__main__':
    part2()
