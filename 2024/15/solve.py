import argparse
from helpers.solver_base import SolverBase, input_as_dict


direction_map = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


def get_moves(curr, direction, grid):
    to_move = [curr]
    while True:
        next = move(curr, direction)
        if grid[next] == "#":
            return []
        elif grid[next] == ".":
            return to_move
        else:
            to_move.append(next)
        curr = next


def move(curr, direction):
    return (curr[0] + direction[0], curr[1] + direction[1])


def print_grid(grid):
    len_x, len_y = max([i[0] for i in grid.keys()]), max([i[1] for i in grid.keys()])
    for y in range(len_y + 1):
        print("".join([grid[x, y] for x in range(len_x + 1)]))


def get_vertical_moves(curr, direction, grid):
    # hack to get this to work as an ordered set
    to_move = {curr: True}
    curr_y = curr[1]
    while True:
        open = 0
        x_coords = list(set([i[0] for i in to_move if i[1] == curr_y]))
        for x in x_coords:
            next = move((x, curr_y), direction)
            if grid[next] == "#":
                return []
            elif grid[next] == ".":
                open += 1
            elif grid[next] == "[":
                to_move[next] = True
                to_move[move(next, (1, 0))] = True
            else:
                to_move[next] = True
                to_move[move(next, (-1, 0))] = True
        if open == len(x_coords):
            return list(to_move.keys())
        else:
            curr_y = curr_y + direction[1]


def transform(grid):
    new_grid = {}
    for coord, char in grid.items():
        new_coord = (coord[0] * 2, coord[1])
        if char == "#":
            new_grid[new_coord] = "#"
            new_grid[move(new_coord, (1, 0))] = "#"
        elif char == "O":
            new_grid[new_coord] = "["
            new_grid[move(new_coord, (1, 0))] = "]"
        elif char == ".":
            new_grid[new_coord] = "."
            new_grid[move(new_coord, (1, 0))] = "."
        elif char == "@":
            new_grid[new_coord] = "@"
            new_grid[move(new_coord, (1, 0))] = "."
    return new_grid


class Solver(SolverBase):
    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            grid, instructions = f.read().split("\n\n")
            grid = input_as_dict(grid.strip("\n").split("\n"))
            for coord, char in grid.items():
                if char == "@":
                    start = coord
                    break
            else:
                raise ValueError("Start not found")
            return grid, instructions.replace("\n", ""), start

    def part1(self):
        grid, instructions, start = self.parse()
        curr = start
        for instruction in instructions:
            direction = direction_map[instruction]
            moves = get_moves(curr, direction, grid)
            if moves:
                for i in moves[:0:-1]:
                    char = grid[i]
                    new = move(i, direction)
                    grid[new] = char
                grid[curr] = "."
                curr = move(curr, direction)
                grid[curr] = "@"

        return sum(
            [coord[0] + 100 * coord[1] for coord, char in grid.items() if char == "O"]
        )

    def part2(self):
        grid, instructions, start = self.parse()
        grid = transform(grid)
        start = (start[0] * 2, start[1])

        curr = start
        for instruction in instructions:
            direction = direction_map[instruction]
            if direction in ((1, 0), (-1, 0)):
                moves = get_moves(curr, direction, grid)
            else:
                moves = get_vertical_moves(curr, direction, grid)

            if moves:
                for i in moves[:0:-1]:
                    char = grid[i]
                    new = move(i, direction)
                    grid[new] = char
                    grid[i] = "."
                grid[curr] = "."
                curr = move(curr, direction)
                grid[curr] = "@"

        return sum(
            [coord[0] + 100 * coord[1] for coord, char in grid.items() if char == "["]
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
