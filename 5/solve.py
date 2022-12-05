initial_obj = {
    '1': ['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'],
    '2': ['W', 'P', 'Q', 'G', 'S'],
    '3': ['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'],
    '4': ['F', 'Z', 'P', 'C', 'G', 'D', 'L'], '5': ['T', 'P', 'S'],
    '6': ['H', 'D', 'F', 'W', 'R', 'L'],
    '7': ['Z', 'N', 'D', 'C'],
    '8': ['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'],
    '9': ['R', 'M', 'S', 'G', 'Z', 'W', 'V']
}


def part1():
    with open('input.txt') as f:
        lines = f.readlines()

    for line in map(str.strip, lines):
        (_, num, _, source, _, target) = line.split(' ')
        for i in range(int(num)):
            initial_obj[target].append(initial_obj[source].pop())

    out = ''
    for i, j in initial_obj.items():
        out += j.pop()

    print(out)


def part2():
    with open('input.txt') as f:
        lines = f.readlines()

    for line in map(str.strip, lines):
        (_, num, _, source, _, target) = line.split(' ')
        initial_obj[target].extend(initial_obj[source][-1 * int(num):])
        del initial_obj[source][-1 * int(num):]

    out = ''
    for i, j in initial_obj.items():
        out += j.pop()

    print(out)


if __name__ == '__main__':
    part2()