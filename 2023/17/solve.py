import argparse
import sys


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        with open(file, 'r') as f:
            return [i.strip('\n') for i in f.readlines()]

    def part1(self):
        nodes = self.data
        end = (len(nodes[-1]) -1, len(nodes) -1)
        visited = {}

        nodes_to_visit = [((1, 0), (1, 0), 0, 0), ((0,1), (0, 1), 0, 0)]
        end_cost = sys.maxsize
        while nodes_to_visit:
            curr_node, curr_direction, path_cost, num_straight = nodes_to_visit.pop(0)
            curr_x, curr_y = curr_node
            if curr_x < 0 or curr_y < 0:
                continue
            try:
                curr_cost = int(nodes[curr_y][curr_x])
            except IndexError:
                continue

            path_cost += curr_cost
            if curr_node == end:
                end_cost = min(end_cost, path_cost)

            node_id = (curr_node, curr_direction)
            if prev := visited.get(node_id):
                prev_cost, prev_straight = prev
                if prev_cost <= path_cost and prev_straight <= num_straight:
                    continue

            visited[node_id] = (path_cost, num_straight)

            next_directions = [(curr_direction[1], curr_direction[0]), (-curr_direction[1], -curr_direction[0])]
            for direction in next_directions:
                next_x, next_y = direction
                next_node = (curr_x + next_x, curr_y + next_y)
                nodes_to_visit.append((next_node, direction, path_cost, 0))
            if num_straight < 2:
                next_node = (curr_x + curr_direction[0], curr_y + curr_direction[1])
                nodes_to_visit.append((next_node, curr_direction, path_cost, num_straight + 1))
            nodes_to_visit.sort(key=lambda x: x[2])
        return end_cost

    def part2(self):
        nodes = self.data
        end = (len(nodes[-1]) -1, len(nodes) -1)
        visited = {}
        start_cost = - 1 * int(nodes[0][0])
        nodes_to_visit = [((0, 0), (1, 0), start_cost), ((0, 0), (0, 1), start_cost)]
        end_cost = sys.maxsize
        while nodes_to_visit:
            curr_node, curr_direction, path_cost = nodes_to_visit.pop(0)
            curr_x, curr_y = curr_node
            if curr_x < 0 or curr_y < 0:
                continue
            try:
                curr_cost = int(nodes[curr_y][curr_x])
            except IndexError:
                continue

            path_cost += curr_cost
            if curr_node == end:
                if path_cost < end_cost:
                    end_cost = path_cost

            node_id = (curr_node, curr_direction)
            if prev_cost := visited.get(node_id):
                if prev_cost <= path_cost:
                    continue

            visited[node_id] = path_cost

            next_directions = [(curr_direction[1], curr_direction[0]), (-curr_direction[1], -curr_direction[0])]
            for direction in next_directions:
                direction_cost = path_cost
                for i in range(1, 11):
                    next_node = (curr_x + direction[0] * i, curr_y + direction[1] * i)
                    next_x, next_y = next_node
                    if next_x < 0 or next_y < 0:
                        continue
                    try:
                        next_cost = int(nodes[next_y][next_x])
                    except IndexError:
                        break
                    if i >= 4:
                        nodes_to_visit.append((next_node, direction, direction_cost))
                    direction_cost += next_cost
            nodes_to_visit.sort(key=lambda x: x[2])

        return end_cost


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
