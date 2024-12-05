import argparse
import numpy


def transpose(rows):
    return [list("".join(i)) for i in zip(*rows)]


def count_lines(lines):
    total = 0
    for line in lines:
        joined_line = "".join(line)
        total = total + joined_line.count("XMAS") + joined_line.count("SAMX")
    return total


def get_horizontal(lines):
    out = []
    max_x = len(lines[0])
    for x in range(max_x):
        out.append(numpy.diagonal(lines, x))
        out.append(numpy.diagonal(numpy.fliplr(lines), x))
    for x in range(1, max_x):
        out.append(numpy.diagonal(numpy.flipud(lines), x))
        out.append(numpy.diagonal(numpy.flipud(numpy.fliplr(lines)), x))
    return out


def num_around(lines, x, y):
    diags = [([1, 1], [-1, -1]), ([-1, 1], [1, -1])]
    try:
        for i in diags:
            prev_y = y + i[0][1]
            prev_x = x + i[0][0]
            next_y = y + i[1][1]
            next_x = x + i[1][0]
            if any(j < 0 for j in [prev_x, prev_y, next_x, next_y]):
                return False

            a = lines[prev_y][prev_x]
            c = lines[next_y][next_x]
            if sorted([a, c]) != ["M", "S"]:
                return False
    except IndexError:
        return False
    return True


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            for line in f.read().strip().split("\n"):
                yield line

    def part1(self):
        total = 0
        lines = [list(line) for line in self.parse()]
        transposed = transpose(lines)
        total = sum(
            [
                count_lines(lines),
                count_lines(transposed),
                count_lines(get_horizontal(lines)),
            ]
        )
        return total

    def part2(self):
        lines = [list(line) for line in self.parse()]
        total = 0
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "A":
                    total += num_around(lines, x, y)
        return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    if args.part == 2:
        print(solver.part2())
    else:
        print(solver.part1())
