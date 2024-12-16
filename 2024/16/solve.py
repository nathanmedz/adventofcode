import argparse
from helpers.solver_base import SolverBase
from helpers.utils import adj4, turn, move
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
        score, _ = djikstra(start, end, grid)
        return score

    def part2(self):
        start, end, grid = self.parse()
        _, seats = djikstra(start, end, grid)
        return seats


def get_possibilities(grid, coord, score, direction):
    poss = []
    next = move(coord, direction)
    if grid[next] != "#":
        poss.append((next, direction, score + 1))
    for _ in range(3):
        direction = turn(direction)
        next = move(coord, direction)
        if grid[next] != "#":
            poss.append((coord, direction, score + 1000))
    return poss


def djikstra(start, end, grid):
    distances = {}
    for node in grid.keys():
        for direction in adj4:
            distances[(node, direction)] = float("inf")

    direction = (1, 0)
    distances[(start, direction)] = 0

    pq = [(0, start, direction, [start])]
    heapify(pq)

    visited = set()
    best = float("inf")
    seats = set()

    while pq:
        score, curr, direction, path = heappop(pq)
        if curr == end:
            best = min(score, best)
            if best == score:
                for i in path:
                    seats.add(i)
            else:
                break

        if (curr, direction) in visited and distances[(curr, direction)] < score:
            continue

        visited.add((curr, direction))
        possibilities = get_possibilities(grid, curr, score, direction)
        for poss in possibilities:
            next_pos, next_direction, next_score = poss
            if next_score <= distances[(next_pos, next_direction)]:
                distances[(next_pos, next_direction)] = next_score
                heappush(pq, (next_score, next_pos, next_direction, path + [next_pos]))

    return best, len(seats)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
