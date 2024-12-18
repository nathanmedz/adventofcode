import argparse
from helpers.solver_base import SolverBase
from helpers.utils import adj4, move
from heapq import heapify, heappop, heappush


class Solver(SolverBase):
    def part1(self):
        if self.test:
            max_bytes = 12
            x = 7
        else:
            max_bytes = 1024
            x = 71
        grid = {(i, j): "." for i in range(x) for j in range(x)}
        i = 0
        for line in self.parse_as_lines():
            if i >= max_bytes:
                break
            i += 1
            a, b = line.split(",")
            a, b = int(a), int(b)
            grid[(a, b)] = "#"
        return djikstra((0, 0), (x - 1, x - 1), grid)

    def part2(self):
        if self.test:
            x = 7
        else:
            x = 71
        grid = {(i, j): "." for i in range(x) for j in range(x)}
        for line in self.parse_as_lines():
            a, b = line.split(",")
            a, b = int(a), int(b)
            grid[(a, b)] = "#"
            if not djikstra((0, 0), (x - 1, x - 1), grid):
                return (a, b)

        return djikstra((0, 0), (x - 1, x - 1), grid)


def djikstra(start, end, grid):
    distances = {node: float("inf") for node in grid.keys()}
    distances[start] = 0

    pq = [(0, start)]
    heapify(pq)

    visited = set()
    while pq:
        score, curr = heappop(pq)
        if curr == end:
            return score

        if curr in visited:
            continue
        visited.add(curr)
        for d in adj4:
            next_pos = move(curr, d)
            if next_pos not in grid or grid[next_pos] == "#":
                continue
            next_score = score + 1
            if next_score < distances[next_pos]:
                distances[next_pos] = next_score
                heappush(pq, (next_score, next_pos))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
