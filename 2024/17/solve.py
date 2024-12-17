import argparse
from helpers.solver_base import SolverBase


def solve(a, b, c, program):
    out = []
    ops = [0, 1, 2, 3, a, b, c]
    pointer = 0
    while True:
        if pointer >= len(program):
            return out
        inst = program[pointer]
        literal_op = program[pointer + 1]
        combo_op = ops[literal_op]
        if inst == 0:
            ops[4] = int(ops[4] / 2**combo_op)
        elif inst == 1:
            ops[5] = ops[5] ^ literal_op
        elif inst == 2:
            ops[5] = combo_op % 8
        elif inst == 3:
            if ops[4] != 0:
                pointer = literal_op
                continue
        elif inst == 4:
            ops[5] = ops[5] ^ ops[6]
        elif inst == 5:
            out.append(combo_op % 8)
        elif inst == 6:
            ops[5] = int(ops[4] / 2**combo_op)
        elif inst == 7:
            ops[6] = int(ops[4] / 2**combo_op)

        pointer += 2


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
        return ",".join([str(i) for i in solve(a, b, c, program)])

    def part2(self):
        _, b, c, program = self.parse()
        i = 0
        digits = 1
        while True:
            sol = solve(i, b, c, program)
            if sol == program:
                return i
            if sol[-digits:] == program[-digits:]:
                i *= 8
                digits += 1
                continue
            i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
