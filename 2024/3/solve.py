import argparse
from operator import mul
from functools import reduce
import re


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
        for line in self.parse():
            for match in re.finditer(r"mul\((\d{1,3})\,(\d{1,3})\)", line):
                total += reduce(mul, [int(i) for i in match.groups()])
        return total

    def part2(self):
        total = 0
        for line in self.parse():
            re_line = re.sub(r"don't\(\).*?do\(\)", "", "do()" + line)
            re_line = re_line.split("don't()")[0]
            for match in re.finditer(r"mul\((\d{1,3})\,(\d{1,3})\)", re_line):
                groups = [int(i) for i in match.groups()]
                total += reduce(mul, groups)
        return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", type=bool, default=False)
    args = parser.parse_args()
    solver = Solver(args.test)
    if args.part == 2:
        print(solver.part2())
    else:
        print(solver.part1())
