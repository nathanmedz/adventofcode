import argparse
import functools
from helpers.solver_base import SolverBase


@functools.cache
def transform(rock):
    if rock == 0:
        return (1,)
    elif len(str(rock)) % 2 == 0:
        str_rock = str(rock)
        return (
            int(str_rock[: len(str_rock) // 2]),
            int(str_rock[len(str_rock) // 2 :]),
        )
    else:
        return (rock * 2024,)


@functools.cache
def step(rocks, curr, max_iter):
    if curr == max_iter:
        return len(rocks)
    return sum([step(transform(rock), curr + 1, max_iter) for rock in rocks])


class Solver(SolverBase):
    def part1(self):
        rocks = (int(i) for i in self.parse_as_line().split())
        return step(rocks, 0, 25)

    def part2(self):
        rocks = (int(i) for i in self.parse_as_line().split())
        return step(rocks, 0, 75)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
