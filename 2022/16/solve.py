import sys
class Node:
    def __init__(self, links, rate, id_str):
        self.links = links
        self.rate = int(rate)
        self.id_str = id_str

def parse_input():
    nodes = {}
    with open('input.txt') as f:
        for line in f:
            line = line.strip().split()
            nodes[line[1]] = Node([i.replace(',', '') for i in line[9:]], line[4].split('=')[-1].replace(';', ''), line[1])
    return nodes


def calc_distances(matrix, source):
    queue = [source]
    visited_nodes = {source}
    distances = {d: sys.maxsize for d in matrix.keys()}
    while queue:
        node = queue.pop(0)
        if node == source:
            distances[node] = 0
        for i in matrix[node].links:
            if i not in visited_nodes:
                distances[i] = min(distances[node] + 1, distances[i])
                queue.append(i)
                visited_nodes.add(i)
    return distances

def part1():
    def dfs_nodes(current_node, opened_nodes, current_time, total, rate):
        max_time = 30
        current_time += 1
        total += rate
        if current_node.id_str not in opened_nodes:
            rate += current_node.rate
            opened_nodes.add(current_node.id_str)

        unvisited_nodes = [i for i in worth_opening if i.id_str not in opened_nodes]
        outcomes = []
        for n in unvisited_nodes:
            distance_to_node = all_distances[current_node.id_str][n.id_str]
            if max_time - current_time <= distance_to_node:
                continue
            new_total = total + min(distance_to_node, max_time - current_time + 1) * rate
            outcomes.append(dfs_nodes(n, opened_nodes.copy(), current_time + distance_to_node, new_total, rate))

        if len(outcomes) == 0:
            return total + rate * (max_time - current_time + 1)

        return max(outcomes)

    matrix = parse_input()
    all_distances = {}
    for n in matrix.values():
        all_distances[n.id_str] = calc_distances(matrix, n.id_str)
    worth_opening = [i for i in matrix.values() if i.rate > 0]
    print(dfs_nodes(matrix['AA'], set(), 0, 0, 0))

def part2():
    def dfs_nodes(current_node, elephant_node, opened_nodes, current_time, elephant_time, total):
        current_time += 1
        elephant_time += 1
        max_time = 26
        if current_node.id_str not in opened_nodes:
            total += current_node.rate * (max_time - current_time + 1)
            opened_nodes.add(current_node.id_str)
        if elephant_node.id_str not in opened_nodes:
            total += elephant_node.rate * (max_time - elephant_time + 1)
            opened_nodes.add(elephant_node.id_str)

        unvisited_nodes = [i for i in worth_opening if i.id_str not in opened_nodes]
        me_nodes = []
        el_nodes = []
        outcomes = []
        for n in unvisited_nodes:
            me_distance_to_node = all_distances[current_node.id_str][n.id_str]
            if max_time - current_time > me_distance_to_node:
                me_nodes.append(n)
            el_distance_to_node = all_distances[elephant_node.id_str][n.id_str]
            if max_time - elephant_time > el_distance_to_node:
                el_nodes.append(n)

        for me in me_nodes:
            for el in el_nodes:
                me_distance_to_node = all_distances[current_node.id_str][me.id_str]
                el_distance_to_node = all_distances[elephant_node.id_str][el.id_str]
                outcomes.append(dfs_nodes(me, el, opened_nodes.copy(), current_time + me_distance_to_node, elephant_time + el_distance_to_node, total))

        if len(outcomes) == 0:
            return total

        return max(outcomes)


    matrix = parse_input()
    all_distances = {}
    for n in matrix.values():
        all_distances[n.id_str] = calc_distances(matrix, n.id_str)
    worth_opening = [i for i in matrix.values() if i.rate > 0]
    print(dfs_nodes(matrix['AA'],matrix['AA'], set(), 0, 0, 0))


if __name__ == '__main__':
    part2()
