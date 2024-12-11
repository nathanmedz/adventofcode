import argparse
from adventofcode.helpers.solver_base import SolverBase


def transform(rock):
    if rock == 0:
        return [1]
    elif len(str(rock)) % 2 == 0:
        str_rock = str(rock)
        return [
            int(str_rock[: len(str_rock) // 2]),
            int(str_rock[len(str_rock) // 2 :]),
        ]
    else:
        return [rock * 2024]


def step(rocks):
    stepped = []
    for rock in rocks:
        stepped.extend(transform(rock))

    return stepped


class Solver(SolverBase):
    def part1(self):
        rocks = [int(i) for i in self.parse_as_line().split()]
        for _ in range(25):
            rocks = step(rocks)
        return len(rocks)

    def part2(self):
        for line in self.parse_as_lines():
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
