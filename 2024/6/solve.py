import argparse


def input_as_dict(lines):
    out = {}
    for y, line in enumerate(lines):
        for x, j in enumerate(list(line)):
            out[(x, y)] = j
    return out


def turn_right(direction):
    return (-direction[1], direction[0])


def step(grid, x, y, direction, visited):
    new_x, new_y = x + direction[0], y + direction[1]
    next_step = grid.get((new_x, new_y))
    if next_step is None:
        raise ValueError()
    if next_step == "#":
        direction = turn_right(direction)
        return x, y, direction
    else:
        if (new_x, new_y, direction) in visited:
            raise StopIteration()
        visited.add((new_x, new_y, direction))
        return new_x, new_y, direction


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            return input_as_dict(f.read().strip().split("\n"))

    def part1(self):
        grid = self.parse()
        for coords, char in grid.items():
            if char == "^":
                direction = (0, -1)
                x, y = coords
                break

        visited = {(x, y, direction)}
        try:
            while True:
                x, y, direction = step(grid, x, y, direction, visited)
        except ValueError:
            return len(set([(i[0], i[1]) for i in visited]))

    def part2(self):
        grid = self.parse()
        for coords, char in grid.items():
            if char == "^":
                start_direction = (0, -1)
                start_x, start_y = coords
                break

        loops = 0
        for coords, char in grid.items():
            if char == ".":
                x, y, direction = start_x, start_y, start_direction
                visited = {(x, y, direction)}
                new_grid = grid.copy()
                new_grid[coords] = "#"
                try:
                    while True:
                        x, y, direction = step(new_grid, x, y, direction, visited)
                except ValueError:
                    continue
                except StopIteration:
                    loops += 1
        return loops


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
