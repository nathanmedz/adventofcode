import argparse
import re


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        with open(file, 'r') as f:
            for line in f.read().strip().split('\n'):
                yield line

    def part1(self):
        total = 0
        for line in self.parse():
            line = re.sub('[^0-9.]', '', line)
            total += int(line[0] + line[-1])

        return total

    def part2(self):
        total = 0
        number_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                      'eight': '8', 'nine': '9'}
        number_map.update({str(i): str(i) for i in range(1, 10)})
        for line in self.parse():
            index_map = []
            for str_number, int_number in number_map.items():
                index_map.extend([(m.start(), int_number) for m in re.finditer(str_number, line)])
            index_map.sort()
            total += int(index_map[0][1] + index_map[-1][1])

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
