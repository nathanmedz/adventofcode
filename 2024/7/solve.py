import argparse
from operator import mul, add


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            for line in f.read().strip().split("\n"):
                total, vals = line.split(":")
                vals = [int(i) for i in vals.split()]
                total = int(total)
                yield total, vals

    def part1(self):
        return sum(
            [
                total
                for total, vals in self.parse()
                if bfs(total, vals.pop(0), vals.copy(), [mul, add])
            ]
        )

    def part2(self):
        return sum(
            [
                total
                for total, vals in self.parse()
                if bfs(total, vals.pop(0), vals.copy(), [mul, add, cat])
            ]
        )


def bfs(total, current, vals, ops):
    queue = [[current, vals]]
    while queue:
        current, vals = queue.pop(0)
        if current == total:
            return True
        if current > total or not vals:
            continue
        next_vals = vals.copy()
        next_val = next_vals.pop(0)
        for op in ops:
            new_current = op(current, next_val)
            queue.append([new_current, next_vals])


def cat(a, b):
    return int(f"{a}{b}")


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
