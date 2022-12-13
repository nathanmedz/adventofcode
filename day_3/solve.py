import string

scoring = string.ascii_lowercase + string.ascii_uppercase


def part1():
    with open('input.txt') as f:
        lines = f.readlines()

    total = 0
    for line in map(str.strip, lines):
        middle = int(len(line)/2)
        first, second = set(line[:middle]), set(line[middle:])
        overlap = first.intersection(second)
        for i in overlap:
            total += scoring.index(i) + 1

    print(total)


def part2():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()

    while lines:
        a, b, c = set(lines.pop().strip('\n')),set(lines.pop().strip('\n')),set(lines.pop().strip('\n'))
        overlap = a.intersection(b).intersection(c)
        for i in overlap:
            total += scoring.index(i) + 1

    print(total)


if __name__ == '__main__':
    part1()