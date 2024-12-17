import argparse
from helpers.solver_base import SolverBase


class Solver(SolverBase):
    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            registers, program = f.read().strip().split("\n\n")
            a, b, c = registers.split("\n")
            a = int(a.split(": ")[-1])
            b = int(b.split(": ")[-1])
            c = int(c.split(": ")[-1])
            program = [int(i) for i in program.split(": ")[-1].split(",")]
            return a, b, c, program

    def part1(self):
        a, b, c, program = self.parse()
        print(a, b, c, program)

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
