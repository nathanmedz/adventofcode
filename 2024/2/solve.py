import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            for line in f.read().strip().split("\n"):
                yield line

    def part1(self):
        safe_levels = 0
        for line in self.parse():
            levels = [int(i) for i in line.split()]
            level_pairs = [(x, y) for x, y in zip(levels, levels[1:])]
            safe_levels += solver.is_safe(level_pairs)

        return safe_levels

    @staticmethod
    def is_safe(level_pairs):
        if level_pairs[0][0] > level_pairs[0][1]:
            return all(0 < p[0] - p[1] <= 3 for p in level_pairs)
        else:
            return all(0 < p[1] - p[0] <= 3 for p in level_pairs)

    def part2(self):
        safe_levels = 0
        for line in self.parse():
            levels = [int(i) for i in line.split()]
            all_levels = [levels[:i] + levels[i + 1 :] for i in range(len(levels))]
            for level in all_levels:
                level_pairs = [(x, y) for x, y in zip(level, level[1:])]
                if solver.is_safe(level_pairs):
                    safe_levels += 1
                    break

        return safe_levels


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
