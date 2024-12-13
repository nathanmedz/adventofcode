import argparse
from adventofcode.helpers.solver_base import SolverBase


directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]


def search_around(data, coord):
    seen = set()
    seen.add(coord)
    char = data[coord]
    queue = [coord]
    while queue:
        x, y = queue.pop()
        for d in directions:
            new = (x + d[0], y + d[1])
            if new not in seen and new in data and data[new] == char:
                seen.add(new)
                queue.append(new)
    return seen


def get_area(coords):
    return len(coords)


def get_perimiter(coords):
    perimiter = 0
    for coord in coords:
        x, y = coord
        for dx, dy in directions:
            if (x + dx, y + dy) not in coords:
                perimiter += 1
    return perimiter


def get_groups(data):
    groups = {}
    to_search = list(data.copy().keys())
    while to_search:
        for coord in to_search:
            seen = search_around(data, coord)
            groups[coord] = seen

            for i in seen:
                to_search.remove(i)
            break
    return groups


def get_corners(coords):
    corners = 0
    for coord in coords:
        neighbors = []
        x, y = coord
        for dx, dy in directions:
            if (x + dx, y + dy) in coords:
                neighbors.append((x + dx, y + dy))
        if not neighbors:
            return 4
        elif len(neighbors) == 1:
            corners += 2
        elif len(neighbors) == 2:
            if (
                len(set([i[0] for i in neighbors])) == 1
                or len(set([i[1] for i in neighbors])) == 1
            ):
                continue
            else:
                corners += 1
                n1 = neighbors[0]
                n2 = neighbors[1]
                adj = (n1[0] + n2[0] - x, n1[1] + n2[1] - y)
                if adj not in coords:
                    corners += 1
        elif len(neighbors) == 3:
            n_x = [i[0] for i in neighbors]
            n_y = [i[1] for i in neighbors]
            for n in neighbors:
                if n_x.count(n[0]) == 1 and n_y.count(n[1]) == 1:
                    desired = n
                    break
            else:
                raise ValueError
            trans = (desired[0] - coord[0], desired[1] - coord[1])
            if len(set(n_x)) == 2:
                diags = [[trans[0], -1], [trans[0], 1]]
            else:
                diags = [[-1, trans[1]], [1, trans[1]]]

            for dx, dy in diags:
                new = (x + dx, y + dy)
                if new not in coords:
                    corners += 1
        else:
            diags = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
            for dx, dy in diags:
                new = (x + dx, y + dy)
                if new not in coords:
                    corners += 1

    return corners


class Solver(SolverBase):
    def part1(self):
        data = self.parse_as_dict()
        groups = get_groups(data)

        return sum(
            [get_area(coords) * get_perimiter(coords) for coords in groups.values()]
        )

    def part2(self):
        data = self.parse_as_dict()
        groups = get_groups(data)
        # for coord, coords in groups.items():
        #     print(data[coord], get_area(coords), get_corners(coords))
        return sum(
            [get_area(coords) * get_corners(coords) for coords in groups.values()]
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
