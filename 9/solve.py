import math

directions = {
    'L': [-1, 0],
    'D': [0, -1],
    'R': [1, 0],
    'U': [0, 1]
}


def move_tail(current_head, current_tail):
    x, y = current_head[0] - current_tail[0], current_head[1] - current_tail[1]
    if abs(x) > 1 or abs(y) > 1:
        head_direction = [int(x/2 + math.copysign(.5, x/2)), int(y/2 + math.copysign(.5, y/2))]
        current_tail = (current_tail[0] + head_direction[0], current_tail[1] + head_direction[1])
    return current_tail


def part1():
    visited = set()
    visited.add((0,0))
    current_head = (0, 0)
    current_tail = (0, 0)
    with open('input.txt') as f:
        for line in f.readlines():
            l = line.strip().split(' ')
            direction, num = directions[l[0]], l[1]
            for i in range(int(num)):
                current_head = (current_head[0] + direction[0], current_head[1] + direction[1])
                current_tail = move_tail(current_head, current_tail)
                visited.add(current_tail)
    print(len(visited))


def part2():
    visited = set()
    visited.add((0,0))
    num_knots = 10
    knot_list = [(0,0)] * num_knots
    with open('input.txt') as f:
        for line in f.readlines():
            l = line.strip().split(' ')
            direction, num = directions[l[0]], l[1]
            for _ in range(int(num)):
                knot_list[0] = (knot_list[0][0] + direction[0], knot_list[0][1] + direction[1])
                for i, knot in enumerate(knot_list[:-1]):
                    knot_list[i+1] = move_tail(knot_list[i], knot_list[i+1])
                visited.add(knot_list[-1])
    print(len(visited))

if __name__ == '__main__':
    part1()
