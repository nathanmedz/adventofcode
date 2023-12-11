import argparse
import math


class Solver:
    direction_map = {
        (1, 0): {'-': (1, 0), '7': (1, 1), 'J': (1, -1)},
        (-1, 0): {'-': (-1, 0), 'F': (-1, 1), 'L': (-1, -1)},
        (0, 1): {'|': (0, 1), 'J': (-1, 1), 'L': (1, 1)},
        (0, -1): {'|': (0, 1), '7': (-1, -1), 'F': (1, -1)}
    }
    possible_directions = {
        '-': [(1, 0), (-1, 0)],
        '|': [(0, 1), (0, -1)],
        'F': [(1, 0), (0, 1)],
        '7': [(-1, 0), (0, 1)],
        'J': [(-1, 0), (0, -1)],
        'L': [(1, 0), (0, -1)],
        'S': [(0, 1), (0, -1), (1, 0), (-1, 0)],
    }

    def __init__(self, test=False):
        self.test = test
        self.data, self.starting_position = self.parse()
        # solution by inspection but I can't be bothered to write the logic to do this
        self.data[self.starting_position[1]][self.starting_position[0]] = '|'

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        data = []
        with open(file, 'r') as f:
            for y, line in enumerate(f.readlines()):
                l = []
                line = line.strip('\n')
                for x, char in enumerate(line):
                    if char == 'S':
                        starting_position = (x, y)
                    l.append(char)

                data.append(l)
        return data, starting_position

    def find_visited_nodes(self):
        visited_nodes = {}
        unvisited_nodes =[(self.starting_position, 0)]
        while unvisited_nodes:
            current_node, current_steps = unvisited_nodes.pop(0)
            visited_nodes[current_node] = current_steps
            current_node_val = self.data[current_node[1]][current_node[0]]
            for direction in self.possible_directions[current_node_val]:
                new_x = current_node[0] + direction[0]
                new_y = current_node[1] + direction[1]
                if new_y < 0 or new_y >= len(self.data):
                    continue
                if new_x < 0 or new_x >= len(self.data[new_y]):
                    continue
                next_node = (new_x, new_y)
                next_node_val = self.data[new_y][new_x]
                if next_node in visited_nodes:
                    continue
                if next_node_val not in self.direction_map[direction].keys():
                    continue
                if (next_node, current_steps+1) in unvisited_nodes:
                    continue
                unvisited_nodes.append((next_node, current_steps+1))
        return visited_nodes

    def part1(self):
        visited_nodes = self.find_visited_nodes()
        return max(visited_nodes.values())

    def part2(self):

        loop_nodes = self.find_visited_nodes()
        uncontained_nodes = set()
        possible_contained_nodes = set()
        contained_nodes = set()
        # edges
        for y in range(len(self.data)):
            row = self.data[y]
            if y == 0 or y == len(self.data) - 1:
                x_range = range(len(row) + 1)
            else:
                x_range = [0, len(row) - 1]
            for x in x_range:
                if (x, y) not in loop_nodes:
                    uncontained_nodes.add((x, y))
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                current_node = (x, y)
                if current_node not in uncontained_nodes and current_node not in loop_nodes:
                    possible_contained_nodes.add(current_node)

        while possible_contained_nodes:
            current_node = possible_contained_nodes.pop()
            if current_node in uncontained_nodes:
                continue
            visited_in_search = [current_node]
            is_contained = True
            unvisited_neighbors = []
            for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x = current_node[0] + direction[0]
                new_y = current_node[1] + direction[1]
                next_node = (new_x, new_y)
                if next_node not in loop_nodes:
                    unvisited_neighbors.append(next_node)
            while unvisited_neighbors:
                current_node = unvisited_neighbors.pop(0)
                if current_node in visited_in_search:
                    continue
                for direction in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_x = current_node[0] + direction[0]
                    new_y = current_node[1] + direction[1]
                    if new_y < 0 or new_y >= len(self.data):
                        continue
                    if new_x < 0 or new_x >= len(self.data[new_y]):
                        continue
                    next_node = (new_x, new_y)
                    if next_node in visited_in_search:
                        continue
                    if next_node in uncontained_nodes:
                        is_contained = False
                        uncontained_nodes.add(current_node)
                    elif next_node not in loop_nodes:
                        unvisited_neighbors.append(next_node)
                visited_in_search.append(current_node)
            if is_contained:
                # check squeeze
                visited_in_squeeze = set()
                for node in visited_in_search:
                    unvisited_neighbors = [
                        (node[0] + .5, node[1] - .5),
                        (node[0] + .5, node[1] + .5),
                        (node[0] - .5, node[1] - .5),
                        (node[0] - .5, node[1] + .5)
                    ]
                    if not is_contained:
                        break
                    while unvisited_neighbors:
                        if not is_contained:
                            break
                        point = unvisited_neighbors.pop(0)
                        visited_in_squeeze.add(point)
                        for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            if self.can_squeeze(point, direction):
                                new_point = (point[0] + direction[0], point[1] + direction[1])
                                if new_point in visited_in_squeeze:
                                    continue

                                if self.touches_outside(new_point, uncontained_nodes):
                                    is_contained = False
                                    break
                                if new_point not in loop_nodes and new_point not in unvisited_neighbors:
                                    unvisited_neighbors.append(new_point)

            for node in visited_in_search:
                if is_contained:
                    contained_nodes.add(node)
                    try:
                        possible_contained_nodes.remove(node)
                    except KeyError:
                        pass
                else:
                    uncontained_nodes.add(node)

        self.print_uncontained(uncontained_nodes, contained_nodes)
        print(len(contained_nodes))

    def print_uncontained(self, uncontained_nodes, contained_nodes):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                current_node = (x, y)
                if current_node in uncontained_nodes:
                    self.data[y][x] = '0'
                elif current_node in contained_nodes:
                    self.data[y][x] = 'I'

        print('\n'.join(''.join(line) for line in self.data))
        print('\n')

    def can_squeeze(self, location, direction):
        x, y = location
        try:
            if direction == (1, 0):
                upper = self.data[int(y - .5)][int(x + .5)]
                lower = self.data[int(y + .5)][int(x + .5)]
                return not (upper in ['|', 'F', '7'] and lower in ['|', 'J', 'L'])
            elif direction == (-1, 0):
                upper = self.data[int(y - .5)][int(x - .5)]
                lower = self.data[int(y + .5)][int(x - .5)]
                return not (upper in ['|', 'F', '7'] and lower in ['|', 'J', 'L'])
            elif direction == (0, 1):
                upper = self.data[int(y + .5)][int(x - .5)]
                lower = self.data[int(y + .5)][int(x + .5)]
                return not(upper in ['-', 'L', 'F'] and lower in ['-', '7', 'J'])
            elif direction == (0, -1):
                upper = self.data[int(y - .5)][int(x - .5)]
                lower = self.data[int(y - .5)][int(x + .5)]
                return not(upper in ['-', 'L', 'F'] and lower in ['-', '7', 'J'])
        except IndexError:
            return False

    def touches_outside(self, point, outside_points):
        touch_points = [
            (point[0] + .5, point[1] - .5),
            (point[0] + .5, point[1] + .5),
            (point[0] - .5, point[1] - .5),
            (point[0] - .5, point[1] + .5)
        ]
        for point in touch_points:
            if point in outside_points:
                return True
        return False



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
