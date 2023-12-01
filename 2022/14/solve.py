import sys

def solve(grid, source, bottom_grid, part_2=False):
    total = 0
    while True:
        res = try_move(grid, source, bottom_grid, source, part_2)
        if not res:
            break
        else:
            grid[res] = True
            total += 1
    return total


def build_grid():
    grid = {}
    bottom_grid = - sys.maxsize
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip().split(' -> ')
            for i in range(len(line) - 1):
                x1, y1 = line[i].split(',')
                x2, y2 = line[i + 1].split(',')
                x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
                bottom_grid = max(bottom_grid, max(y1, y2))
                if x1 == x2:
                    for j in range(min(y1, y2), max(y1, y2) + 1):
                        grid[(x1, j)] = True
                elif y1 == y2:
                    for j in range(min(x1, x2), max(x1, x2) + 1):
                        grid[(j, y1)] = True


    return grid, bottom_grid


def try_move(grid, curr, bottom_grid, source, part_2=False):
    curr_x, curr_y = curr
    if curr_y > bottom_grid and not part_2:
        return False
    if not grid.get((curr_x, curr_y + 1)):
        curr_y += 1
        return try_move(grid, (curr_x, curr_y), bottom_grid, source, part_2)
    elif not grid.get((curr_x - 1, curr_y + 1)):
        curr_y += 1
        curr_x -= 1
        return try_move(grid, (curr_x, curr_y), bottom_grid, source, part_2)
    elif not grid.get((curr_x + 1, curr_y + 1)):
        curr_y += 1
        curr_x += 1
        return try_move(grid, (curr_x, curr_y), bottom_grid, source, part_2)
    elif (curr_x, curr_y) == source:
        return False

    return curr_x, curr_y

def part1():
    grid, bottom_grid = build_grid()
    total = solve(grid, (500, 0), bottom_grid)
    print(total)

def part2():
    grid, bottom_grid = build_grid()
    for i in range(0, 1000):
        grid[(i, bottom_grid + 2)] = True

    total = solve(grid, (500, 0), bottom_grid, True)
    print(total + 1)


if __name__ == '__main__':
    part1()
