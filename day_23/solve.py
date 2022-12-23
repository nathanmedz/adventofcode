import operator
from collections import defaultdict


def part1():
    grove = parse()
    move_priority = [
        [(0, -1), (-1, -1), (1, -1)],
        [(0, 1), (-1, 1), (1, 1)],
        [(-1, 0), (-1, 1), (-1, -1)],
        [(1, 0), (1, 1), (1, -1)],
    ]
    for _ in range(10):
        grove, finished = do_moves(grove, move_priority)
        move_priority.append(move_priority.pop(0))

    print(sum_grove(grove))


def part2():
    grove = parse()
    move_priority = [
        [(0, -1), (-1, -1), (1, -1)],
        [(0, 1), (-1, 1), (1, 1)],
        [(-1, 0), (-1, 1), (-1, -1)],
        [(1, 0), (1, 1), (1, -1)],
    ]
    total = 0
    while True:
        grove, finished = do_moves(grove, move_priority)
        total += 1
        if finished:
            break
        move_priority.append(move_priority.pop(0))
    print(total)


def parse():
    grove = set()
    with open('input.txt') as f:
        for y, l in enumerate(f.readlines()):
            for x, val in enumerate(l.strip()):
                if val == '#':
                    grove.add((x, y))

    return grove

def do_moves(grove, move_priority):
    new_locs = defaultdict(list)
    all_directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]
    for loc in grove:
        for direction in all_directions:
            if tuple(map(operator.add, loc, direction)) in grove:
                break
        else:
            new_locs[loc].append(loc)
            continue

        for directions in move_priority:
            for direction in directions:
                if tuple(map(operator.add, loc, direction)) in grove:
                    break
            else:
                new_locs[tuple(map(operator.add, loc, directions[0]))].append(loc)
                break
        else:
            new_locs[loc].append(loc)


    new_grove = set()
    for new_loc, old_loc in new_locs.items():
        if len(old_loc) == 1:
            new_grove.add(new_loc)
        else:
            for loc in old_loc:
                new_grove.add(loc)

    return new_grove, grove == new_grove


def sum_grove(grove, debug=False):
    min_x = min(x for x,y in grove)
    min_y = min(y for x,y in grove)
    max_x = max(x for x,y in grove)
    max_y = max(y for x,y in grove)
    total = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in grove:
                if debug:
                    print('#', end='')
            else:
                if debug:
                    print('.', end='')
                total += 1
        if debug:
            print('\n', end='')
    if debug:
        print('\n\n')
    return total

if __name__ == '__main__':
    part2()
