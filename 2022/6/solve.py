def part1():
    with open('input.txt') as f:
        line = f.readline()
        for i in range(3, len(line)):
            chars = line[i - 4:i]
            if len(set(chars)) == 4:
                print(i)
                break


def part2():
    with open('input.txt') as f:
        line = f.readline()
        for i in range(13, len(line)):
            chars = line[i - 14:i]
            if len(set(chars)) == 14:
                print(i)
                break


if __name__ == '__main__':
    part2()