
def part1():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
    for line in map(str.strip, lines):
        a, b = line.split(',')
        a = set(range(int(a.split('-')[0]), int(a.split('-')[1]) + 1))
        b = set(range(int(b.split('-')[0]), int(b.split('-')[1]) + 1))
        if a.issubset(b) or b.issubset(a):
            total += 1
    print(total)


def part2():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
    for line in map(str.strip, lines):
        a, b = line.split(',')
        a = set(range(int(a.split('-')[0]), int(a.split('-')[1]) + 1))
        b = set(range(int(b.split('-')[0]), int(b.split('-')[1]) + 1))
        if a.intersection(b) or b.intersection(a):
            total += 1
    print(total)


if __name__ == '__main__':
    part1()