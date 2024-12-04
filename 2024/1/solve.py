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
        left, right = zip(
            *[(int(a), int(b)) for a, b in (line.split() for line in self.parse())]
        )

        return sum([abs(a - b) for a, b in zip(sorted(left), sorted(right))])

    def part2(self):
        left, right = zip(
            *[(int(a), int(b)) for a, b in (line.split() for line in self.parse())]
        )
        return sum(i * right.count(i) for i in left)


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
