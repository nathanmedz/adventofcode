import argparse
from adventofcode.helpers.solver_base import SolverBase
from sympy.core.numbers import Integer
from sympy import Eq, symbols
from sympy.solvers import solve


def parse_x_y(line):
    x, y = line.split(":")[-1].strip().split(", ")
    return int(x.strip("X").strip("+").strip("=")), int(
        y.strip("Y").strip("+").strip("=")
    )


class Solver(SolverBase):
    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        out = []
        with open(file, "r") as f:
            blocks = f.read().strip("\n").split("\n\n")
            for block in blocks:
                lines = block.split("\n")
                ax, ay = parse_x_y(lines[0])
                bx, by = parse_x_y(lines[1])
                px, py = parse_x_y(lines[2])
                out.append({"A": (ax, ay), "B": (bx, by), "P": (px, py)})
        return out

    def part1(self):
        wins = []
        for data in self.parse():
            possible = []
            px, py = data["P"]
            ax, ay = data["A"]
            bx, by = data["B"]
            for i in range(100, -1, -1):
                req_x, req_y = px - i * bx, py - i * by
                if req_x < 0 or req_y < 0:
                    continue
                if req_x % ax == 0 and req_y % ay == 0 and req_x // ax == req_y // ay:
                    possible.append((req_x // ax, i))

            score = 999999999999
            found = False
            for poss in possible:
                score = min(3 * poss[0] + poss[1], score)
                found = True

            if found:
                wins.append(score)
        return sum(wins)

    def part2(self):
        wins = []
        for data in self.parse():
            px, py = data["P"][0] + 10000000000000, data["P"][1] + 10000000000000
            ax, ay = data["A"]
            bx, by = data["B"]
            a, b = symbols("a b")
            eq1 = Eq((px - (bx * (py - (ay * a)) / by)) / ax - a, 0)
            eq2 = Eq((py - (ay * (px - (bx * b)) / ax)) / by - b, 0)
            sols = solve([eq1, eq2])
            if all([isinstance(i, Integer) for i in sols.values()]):
                wins.append(3 * int(sols[a]) + int(sols[b]))

        return sum(wins)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
