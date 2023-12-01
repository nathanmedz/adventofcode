import string
import sys

scoring_map = {j: i for i, j in enumerate(string.ascii_lowercase)}
scoring_map['S'] = 0
scoring_map['E'] = 25


def build_matrix():
    matrix = []
    with open('input.txt') as f:
        for line in f.readlines():
            row = [i for i in line.strip()]
            matrix.append(row)

    return matrix


def bfs(matrix, node):
    queue = [[node]]
    visited_nodes = set()
    while queue:
        current_path = queue.pop(0)
        node = current_path[-1]
        curr_x, curr_y = node
        current_el = matrix[curr_y][curr_x]

        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        if node in visited_nodes:
            continue
        for [x, y] in directions:
            new_x, new_y = curr_x + x, curr_y + y
            if new_x < 0 or new_x >= len(matrix[0]) or new_y < 0 or new_y >= len(matrix):
                continue
            next_el = matrix[new_y][new_x]
            next_loc = (new_x, new_y)
            if scoring_map.get(next_el) - scoring_map.get(current_el) > 1 or next_loc in visited_nodes:
                continue
            if next_el == 'E':
                return len(current_path)

            new_path = current_path.copy()
            new_path.append(next_loc)
            queue.append(new_path)

        visited_nodes.add(node)
    return sys.maxsize


def part1():
    min_length = sys.maxsize
    matrix = build_matrix()
    for y, row in enumerate(matrix):
        for x, i in enumerate(row):
            if i == 'S':
                min_length = min(min_length, bfs(matrix, (x,y)))

    print(min_length)


def part2():
    min_length = sys.maxsize
    matrix = build_matrix()
    for y, row in enumerate(matrix):
        for x, i in enumerate(row):
            if i == 'a' or i == 'S':
                min_length = min(min_length, bfs(matrix, (x,y)))

    print(min_length)


if __name__ == '__main__':
    part2()