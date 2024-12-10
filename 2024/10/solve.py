import argparse
from adventofcode.helpers.solver_base import SolverBase


class Solver(SolverBase):
    def part1(self):
        grid = self.parse_as_dict()
        ans = 0
        for loc, char in grid.items():
            if char == "0":
                distinct, _ = bfs(grid, loc)
                ans += distinct
        return ans

    def part2(self):
        grid = self.parse_as_dict()
        ans = 0
        for loc, char in grid.items():
            if char == "0":
                _, total = bfs(grid, loc)
                ans += total
        return ans


directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def bfs(grid, start):
    queue = [[start]]
    distinct = set()
    total = 0
    while queue:
        path = queue.pop(0)
        current = path[-1]
        curr_int = int(grid[current])
        if curr_int == 9:
            total += 1
            distinct.add(current)
            continue
        for d in directions:
            next_pos = (current[0] + d[0], current[1] + d[1])
            if next_pos not in grid or next_pos in path:
                continue
            next_int = int(grid[next_pos])

            if next_int - curr_int == 1:
                new_path = path.copy()
                new_path.append(next_pos)
                queue.append((new_path))

    return len(distinct), total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
