import argparse
from collections import defaultdict


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()
        self.direction_map = {
            '-': {
                (1, 0): [(1, 0)],
                (-1, 0): [(-1, 0)],
                (0, 1): [(1, 0), (-1, 0)],
                (0, -1): [(1, 0), (-1, 0)],
            },
            '|': {
                (1, 0): [(0, 1), (0, -1)],
                (-1, 0): [(0, 1), (0, -1)],
                (0, 1): [(0, 1)],
                (0, -1): [(0, -1)],
            },
            '/': {
                (1, 0): [(0, -1)],
                (-1, 0): [(0, 1)],
                (0, 1): [(-1, 0)],
                (0, -1): [(1, 0)],
            },
            '\\': {
                (1, 0): [(0, 1)],
                (-1, 0): [(0, -1)],
                (0, 1): [(1, 0)],
                (0, -1): [(-1, 0)],
            },
            '.': {
                (1, 0): [(1, 0)],
                (-1, 0): [(-1, 0)],
                (0, 1): [(0, 1)],
                (0, -1): [(0, -1)],
            }
        }

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        with open(file, 'r') as f:
            return [i.strip('\n') for i in f.readlines()]

    def part1(self):
        direction = (1, 0)
        start = (0, 0)
        curr = (start, direction)
        return self.find_num_energized(curr)

    def part2(self):
        total = 0
        for y in range(len(self.data)):
            left_start = [(0, y), (1, 0)]
            right_start = [(len(self.data), y), (-1, 0)]
            total = max(total, self.find_num_energized(left_start))
            total = max(total, self.find_num_energized(right_start))
        for x in range(len(self.data[0])):
            left_start = [(x, 0), (0, 1)]
            right_start = [(x, len(self.data[0])), (0, -1)]
            total = max(total, self.find_num_energized(left_start))
            total = max(total, self.find_num_energized(right_start))

        return total

    def find_num_energized(self, start):
        visited = defaultdict(list)
        nodes_to_visit = [start]
        while nodes_to_visit:
            curr_node, curr_direction = nodes_to_visit.pop(0)
            if curr_direction in (visited.get(curr_node) or []):
                continue

            curr_x, curr_y = curr_node
            if curr_x < 0 or curr_y < 0:
                continue
            try:
                curr_char = self.data[curr_y][curr_x]
            except IndexError:
                continue
            visited[curr_node].append(curr_direction)

            next_directions = self.direction_map[curr_char][curr_direction]
            for direction in next_directions:
                next_x, next_y = direction
                next_node = (curr_x + next_x, curr_y + next_y)
                nodes_to_visit.append((next_node, direction))

        return len(visited.keys())



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int, default=1)
    parser.add_argument('--test', type=bool, default=False)
    args = parser.parse_args()
    solver = Solver(args.test)
    if args.part == 2:
        print(solver.part2())
    else:
        print(solver.part1())
