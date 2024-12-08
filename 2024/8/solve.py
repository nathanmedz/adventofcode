import argparse
from collections import defaultdict
from adventofcode.helpers.solver_base import SolverBase


class Solver(SolverBase):
    def part1(self):
        input_map = self.parse_as_dict()
        letter_locs = defaultdict(list)
        antinodes = set()
        for coords, char in input_map.items():
            if char != ".":
                letter_locs[char].append(coords)

        for char, nodes in letter_locs.items():
            while nodes:
                node = nodes.pop()
                for other in nodes:
                    possible_antinodes = [
                        (2 * node[0] - other[0], 2 * node[1] - other[1]),
                        (2 * other[0] - node[0], 2 * other[1] - node[1]),
                    ]
                    for poss in possible_antinodes:
                        if poss in input_map:
                            antinodes.add(poss)

        return len(antinodes)

    def part2(self):
        input_map = self.parse_as_dict()
        letter_locs = defaultdict(list)
        antinodes = set()
        for coords, char in input_map.items():
            if char != ".":
                letter_locs[char].append(coords)

        for char, nodes in letter_locs.items():
            while nodes:
                node = nodes.pop()
                for other in nodes:
                    rise = other[1] - node[1]
                    run = other[0] - node[0]
                    for direction in [1, -1]:
                        poss = node if direction == 1 else other
                        while True:
                            poss = (
                                poss[0] + direction * run,
                                poss[1] + direction * rise,
                            )
                            if poss not in input_map:
                                break
                            antinodes.add(poss)
        return len(antinodes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    if args.part == 2:
        print(solver.part2())
    else:
        print(solver.part1())
