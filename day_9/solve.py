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
        current_tail = (current_tail[0] + int(x/2 + math.copysign(.5, x)), current_tail[1] + int(y/2 + math.copysign(.5, y)))
    return current_tail


def move_head(current_head, direction):
    return current_head[0] + direction[0], current_head[1] + direction[1]


def part1():
    visited = {(0, 0)}
    current_head, current_tail = (0, 0), (0, 0)
    with open('input.txt') as f:
        for line in f.readlines():
            direction_str, num = line.strip().split(' ')
            for i in range(int(num)):
                current_head = move_head(current_head, directions[direction_str])
                current_tail = move_tail(current_head, current_tail)
                visited.add(current_tail)

    print(len(visited))


def part2():
    visited = {(0, 0)}
    knot_list = [(0, 0)] * 10
    with open('input.txt') as f:
        for line in f.readlines():
            direction_str, num = line.strip().split(' ')
            for _ in range(int(num)):
                knot_list[0] = move_head(knot_list[0], directions[direction_str])
                for i in range(len(knot_list) - 1):
                    knot_list[i+1] = move_tail(knot_list[i], knot_list[i+1])

                visited.add(knot_list[-1])

    print(len(visited))


if __name__ == '__main__':
    part2()
