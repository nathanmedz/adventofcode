import argparse
from adventofcode.helpers.solver_base import SolverBase


def create_map(data):
    out = []
    block = True
    i = 0
    for d in data:
        if block:
            out.extend([[str(i)] for _ in range(int(d))])
            i += 1
        else:
            out.extend([["."] for _ in range(int(d))])
        block = not block
    return out


def count_total(out):
    total = 0
    for i, j in enumerate(out):
        if j[0] == ".":
            return total
        total += i * int(j[0])
    return total


class Solver(SolverBase):
    def part1(self):
        data = self.parse_as_line()
        out = create_map(data)
        left = 0
        right = len(out) - 1
        while left <= right:
            if out[left][0] != ".":
                left += 1
            elif out[right][0] == ".":
                right -= 1
            else:
                out[left], out[right] = out[right], out[left]
                left += 1
                right -= 1

        return count_total(out)

    def part2(self):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
