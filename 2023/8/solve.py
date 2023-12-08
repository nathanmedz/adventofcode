import argparse
import math


class Solver:

    def __init__(self, test=False):
        self.test = test
        self.data, self.directions = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        data = {}
        with open(file, 'r') as f:
            lines = f.readlines()
            directions = lines[0].strip('\n')
            for line in lines[2:]:
                source, target = line.strip('\n').split('=')
                data[source.strip()] = (target.strip(' (').strip(')').split(', '))

        return data, directions

    def distance_to_end_node(self, curr):
        i = 0
        while True:
            for direction in self.directions:
                i += 1
                curr = self.data[curr][{'L': 0, 'R': 1}[direction]]
                if curr[-1] == 'Z':
                    return i

    def part1(self):
        return self.distance_to_end_node('AAA')

    def part2(self):
        start_nodes = [i for i in self.data.keys() if i[-1] == 'A']
        return math.lcm(*[self.distance_to_end_node(start) for start in start_nodes])


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
