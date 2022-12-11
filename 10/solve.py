
def part1():
    cycle = 0
    x = 1
    total = 0
    with open('input.txt') as f:
        for line in f.readlines():
            cycle += 1
            line = line.strip().split(' ')
            if cycle == 20 or (cycle - 20) % 40 == 0:
                total += cycle * x
            if line[0] == 'noop':
                continue
            else:
                cycle += 1
                if cycle == 20 or (cycle - 20) % 40 == 0:
                    total += cycle * x
                x += int(line[1])

    print(total)


def part2():
    cycle = 0
    x = 1
    with open('input.txt') as f:
        for line in f.readlines():
            if (abs((cycle % 40) - x) <= 1):
                print('#', end='')
            else:
                print('.', end="")
            cycle += 1
            line = line.strip().split(' ')
            if cycle % 40 == 0:
                print('\n', end='')
            if line[0] == 'noop':
                continue
            else:
                if (abs((cycle % 40) - x) <= 1):
                    print('#', end='')
                else:
                    print('.', end="")
                cycle += 1
                if cycle % 40 == 0:
                    print('\n', end='')
                x += int(line[1])


if __name__ == '__main__':
    part2()