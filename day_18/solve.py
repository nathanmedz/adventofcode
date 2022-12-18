import operator

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def part1():
    squares = parse()
    print(sum(len({tuple(map(operator.add, s, d)) for d in directions}.difference(squares)) for s in squares))


def part2():
    squares = parse()
    max_x, max_y, max_z = 0, 0, 0
    for s in squares:
        max_x, max_y, max_z = max(max_x, s[0]), max(max_y, s[1]), max(max_z, s[2])

    air_pockets = set()
    for x in range(0, max_x):
        for y in range(0, max_y):
            for z in range(0, max_z):
                if (x, y, z) not in squares:
                    air_pockets.add((x, y, z))

    for pocket in air_pockets:
        if not exits_matrix(squares, pocket, max_x, max_y, max_z):
            squares.add(pocket)

    print(sum(len({tuple(map(operator.add, s, d)) for d in directions}.difference(squares)) for s in squares))


def exits_matrix(matrix, node, max_x, max_y, max_z):
    queue = [node]
    visited_nodes = set()
    while queue:
        node = queue.pop(0)
        if node in visited_nodes:
            continue
        for d in directions:
            new_x, new_y, new_z = tuple(map(operator.add, node, d))
            if any([new_x > max_x, new_y > max_y, new_z > max_z, new_x < 0, new_y < 0, new_z < 0]):
                return True
            next_loc = (new_x, new_y, new_z)
            if next_loc in matrix:
                continue
            queue.append(next_loc)

        visited_nodes.add(node)

    return False


def parse():
    squares = set()
    with open('input.txt') as f:
        for line in f.readlines():
            l = line.strip().split(',')
            squares.add(tuple(map(int, l)))

    return squares

if __name__ == '__main__':
    part2()
