import argparse
from adventofcode.helpers.solver_base import SolverBase


class Solver(SolverBase):
    def part1(self):
        for line in self.parse_as_lines():
            pass

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
