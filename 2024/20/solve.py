import argparse
from helpers.solver_base import SolverBase
from helpers.utils import adj4, move
from heapq import heapify, heappop, heappush


class Solver(SolverBase):
    def parse(self):
        grid = self.parse_as_dict()
        start, end = None, None
        for coord, char in grid.items():
            if char == "S":
                start = coord
            elif char == "E":
                end = coord
        return start, end, grid

    def part1(self):
        start, end, grid = self.parse()
        path = djikstra(start, end, grid)
        return search_cheats(100, 2, path)

    def part2(self):
        start, end, grid = self.parse()
        path = djikstra(start, end, grid)
        return search_cheats(100, 20, path)


def search_cheats(gap, secs, path):
    cheats = set()
    for idx, coord in enumerate(path):
        possible_targets = path[idx + gap :]
        for target in possible_targets:
            distance = dist(coord, target)
            if distance <= secs:
                time_saved = path.index(target) - idx - distance
                if time_saved >= gap:
                    cheats.add((coord, target))

    return len(cheats)


def dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def djikstra(start, end, grid):
    distances = {node: float("inf") for node in grid.keys()}
    distances[start] = 0

    pq = [(0, [start])]
    heapify(pq)

    visited = set()
    while pq:
        score, path = heappop(pq)
        curr = path[-1]
        if curr == end:
            return path

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
                heappush(pq, (next_score, path + [next_pos]))
    return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
