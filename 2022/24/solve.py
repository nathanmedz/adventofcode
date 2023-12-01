import sys
from collections import defaultdict


class Blizzard:
    def __init__(self, direction, x, y, valley_dimens):
        self.direction = direction
        self.x = x
        self.y = y
        self.valley_dimens = valley_dimens

    def move(self):
        new_x, new_y = self.x + self.direction[0], self.y + self.direction[1]
        if new_x <= 0 or new_y <= 0 or new_x >= self.valley_dimens[0] -1 or new_y >= self.valley_dimens[1] -1:
            if self.direction == (1, 0):
                new_x = 1
            elif self.direction == (0, 1):
                new_y = 1
            elif self.direction == (-1, 0):
                new_x = self.valley_dimens[0] - 2
            else:
                new_y = self.valley_dimens[1] - 2
        self.x = new_x
        self.y = new_y

def parse():
    blizzards = []
    directions_map = {'>': (1,0), '^': (0, -1), '<': (-1, 0), 'v': (0, 1)}
    with open('input.txt') as f:
        lines = f.readlines()
        for y, l in enumerate(lines):
            for x, val in enumerate(l.strip()):
                if val in directions_map.keys():
                    blizzards.append(Blizzard(directions_map[val], x, y, (len(l.strip()), len(lines))))

    return blizzards, len(l.strip()), len(lines)

def show_map(blizzards, max_x, max_y):
    blizzard_dict = defaultdict(list)
    directions_map = {(1,0):'>', (0, -1):'^', (-1, 0):'<', (0, 1):'v' }
    for blizzard in blizzards:
        blizzard_dict[(blizzard.x, blizzard.y)].append(blizzard)
    for y in range(max_y):
        if y == 0 or y == max_y - 1:
            print(f'{"#"*max_x}\n', end='')
            continue
        for x in range(max_x):
            if x == 0 or x == max_x - 1:
                print('#', end='')
                continue

            if blizzard_dict.get((x, y)):
                loc_blizzard = blizzard_dict.get((x, y))
                if len(loc_blizzard) == 1:
                    print(directions_map[loc_blizzard[0].direction], end='')
                else:
                    print(len(loc_blizzard), end='')
            else:
                print('.', end='')
        print('\n', end='')
    print('\n', end='')


def bfs(max_x, max_y, start, end, horizontal_blizzard_map, vertical_blizzard_map, i=0):
    queue = [[start]]
    visited_nodes = set()
    while queue:
        current_path = queue.pop(0)
        node = current_path[-1]
        curr_x, curr_y = node
        age_counter = len(current_path) + i
        if (curr_x, curr_y, age_counter % (max_x-2), age_counter % (max_y-2)) in visited_nodes:
            continue
        directions = [
            [0,0],
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        for [x, y] in directions:
            new_x, new_y = curr_x + x, curr_y + y
            new_loc = (new_x, new_y)
            if new_loc == end:
                return age_counter
            if new_loc not in {start, end}:
                if new_x <= 0 or new_y <= 0 or new_x >= (max_x -1) or new_y >= (max_y - 1):
                    continue
            blizzards = vertical_blizzard_map[age_counter % (max_y -2)].union(horizontal_blizzard_map[age_counter % (max_x - 2)])
            if new_loc in blizzards:
                continue

            new_path = current_path.copy()
            new_path.append(new_loc)
            queue.append(new_path)

        visited_nodes.add((curr_x, curr_y, age_counter % (max_x-2), age_counter % (max_y-2)))

    return sys.maxsize

def build_blizzard_maps():
    blizzards, max_x, max_y = parse()
    horizontal_blizzard_map = {}
    vertical_blizzard_map = {}
    for i in range(max(max_y, max_x) + 1):
        horizontal_blizzards = [b for b in blizzards if b.direction in [(1, 0), (-1, 0)]]
        horizontal_blizzard_map[i%(max_x-2)] = {(b.x,b.y) for b in horizontal_blizzards}
        vertical_blizzards = [b for b in blizzards if b.direction in [(0, 1), (0, -1)]]
        vertical_blizzard_map[i%(max_y-2)] = {(b.x,b.y) for b in vertical_blizzards}
        for blizzard in blizzards:
            blizzard.move()
    return horizontal_blizzard_map, vertical_blizzard_map


def part1():
    blizzards, max_x, max_y = parse()
    horizontal_blizzard_map, vertical_blizzard_map = build_blizzard_maps()
    start, end = (1,0), (max_x -2, max_y- 1)
    first = bfs(max_x, max_y, start, end, horizontal_blizzard_map, vertical_blizzard_map)
    print(first)


def part2():
    blizzards, max_x, max_y = parse()
    horizontal_blizzard_map, vertical_blizzard_map = build_blizzard_maps()
    start, end = (1,0), (max_x -2, max_y- 1)
    first = bfs(max_x, max_y, start, end, horizontal_blizzard_map, vertical_blizzard_map)
    second = bfs(max_x, max_y, end, start, horizontal_blizzard_map, vertical_blizzard_map, first)
    third = bfs(max_x, max_y, start, end, horizontal_blizzard_map, vertical_blizzard_map, second)
    print(third)


if __name__ == '__main__':
    part1()
