import argparse
import math


class Solver:

    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        data = []
        with open(file, 'r') as f:
            for line in f.readlines():
                data.append([int(i) for i in line.strip('\n').split()])
        return data

    def part1(self):
        total = 0
        for line in self.data:
            all_lines = Solver.reduce_line(line)

            for idx in range(len(all_lines) - 1, -1, -1):
                curr_line = all_lines[idx]
                if idx == len(all_lines) - 1:
                    curr_line.append(0)
                else:
                    curr_line.append(all_lines[idx + 1][-1] + curr_line[-1])
            total += all_lines[0][-1]
        return total

    @staticmethod
    def reduce_line(line):
        all_lines = [line]
        while set(all_lines[-1]) != {0}:
            line1 = all_lines[-1]
            new_line = [line1[i + 1] - line1[i] for i in range(len(line1) - 1)]
            all_lines.append(new_line)
        return all_lines

    def part2(self):
        total = 0
        for line in self.data:
            all_lines = Solver.reduce_line(line)

            for idx in range(len(all_lines) - 1, -1, -1):
                curr_line = all_lines[idx]
                if idx == len(all_lines) - 1:
                    curr_line.insert(0, 0)
                else:
                    curr_line.insert(0, curr_line[0] - all_lines[idx + 1][0])
            total += all_lines[0][0]
        return total


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int, default=1)
    parser.add_argument('--test', type=bool, default=False)
    args = parser.parse_args()
    solver = Solver(args.test)
    if args.part == 2:
        print(solver.part2())
    else:
        print(solver.part1())
