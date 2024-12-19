import argparse
from helpers.solver_base import SolverBase
import functools


class Solver(SolverBase):
    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            towels, designs = f.read().split("\n\n")
            towels = tuple(towels.strip().split(", "))
            designs = tuple(designs.strip().split("\n"))
            return towels, designs

    def part1(self):
        towels, designs = self.parse()
        return sum([1 for design in designs if count_design(design, towels)])

    def part2(self):
        towels, designs = self.parse()
        return sum([count_design(design, towels) for design in designs])


@functools.cache
def count_design(design, towels):
    if design == "":
        return True
    return sum(
        count_design(design.replace(towel, "", 1), towels)
        for towel in towels
        if design.startswith(towel)
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
