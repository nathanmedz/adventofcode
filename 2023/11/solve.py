import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        with open(file, 'r') as f:
            return set((x, y) for y, line in enumerate(f.readlines()) for x, char in enumerate(line.strip('\n')) if char == '#')

    @staticmethod
    def distance_between(a, b):
        return abs(a[1] - b[1]) + abs(a[0] - b[0])

    def expand_galaxies(self, expand_by):
        x_range = range(max(i[0] for i in self.data) + 1)
        y_range = range(max(i[1] for i in self.data) + 1)
        empty_x = [i for i in x_range if i not in [j[0] for j in self.data]]
        empty_y = [i for i in y_range if i not in [j[1] for j in self.data]]
        galaxies = set()
        for point in self.data:
            increase_x = 0
            increase_y = 0
            for i in empty_y:
                if i < point[1]:
                    increase_y += expand_by
            for i in empty_x:
                if i < point[0]:
                    increase_x += expand_by
            galaxies.add((point[0] + increase_x, point[1] + increase_y))
        return galaxies

    def part1(self):
        galaxies = self.expand_galaxies(1)
        return sum(Solver.distance_between(a, b) for a in galaxies for b in galaxies if a != b) // 2

    def part2(self):
        galaxies = self.expand_galaxies(999999)
        return sum(Solver.distance_between(a, b) for a in galaxies for b in galaxies if a != b) // 2


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
