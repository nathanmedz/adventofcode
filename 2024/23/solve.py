from helpers.solver_base import SolverBase, _get_args
from collections import defaultdict


class Solver(SolverBase):
    def parse(self):
        connections = defaultdict(set)
        groups = set()
        for line in self.parse_as_lines():
            a, b = line.split("-")
            groups.add(tuple(sorted([a, b])))
            connections[a].add(b)
            connections[b].add(a)
        return groups, connections

    def part1(self):
        groups, connections = self.parse()
        groups = grow_groups(groups, connections)
        return len([g for g in groups if any([i.startswith("t") for i in g])])

    def part2(self):
        groups, connections = self.parse()
        while True:
            groups = grow_groups(groups, connections)
            if len(groups) == 1:
                return ",".join(list(groups)[0])


def grow_groups(groups, connections):
    new_groups = set()
    for group in groups:
        overlap = connections[group[0]]
        for g in group[1:]:
            overlap = overlap.intersection(connections[g])
        for i in overlap:
            new_group = tuple(sorted(list(group) + [i]))
            new_groups.add(new_group)
    return new_groups


if __name__ == "__main__":
    args = _get_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
