from helpers.solver_base import SolverBase, _get_args


class Solver(SolverBase):
    def part1(self):
        for line in self.parse_as_lines():
            pass

    def part2(self):
        for line in self.parse_as_lines():
            pass


if __name__ == "__main__":
    args = _get_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
