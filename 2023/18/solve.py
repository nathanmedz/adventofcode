import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()
        self.direction_map = {
            'R': (1, 0),
            'U': (0, -1),
            'D': (0, 1),
            'L': (-1, 0)
        }
        self.hex_dir_map = {
            0: (1, 0),
            3: (0, -1),
            1: (0, 1),
            2: (-1, 0)
        }

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        out = []
        with open(file, 'r') as f:
            for line in f.readlines():
                direction, num, colour = line.strip('\n').split(' ')
                out.append([direction, int(num), colour.strip(')').strip('(')])
        return out

    def part1(self):
        curr = (0, 0)
        perimiter = 0
        sorted_points = [curr]
        for line in self.data:
            direction_str, num_steps, colour = line
            x, y = self.direction_map[direction_str]
            curr = (curr[0] + x * num_steps, curr[1] + y * num_steps)
            sorted_points.append(curr)
            perimiter += num_steps

        area = area_by_shoelace(sorted_points)
        # picks theorem
        return (area + 1) + perimiter/2

    def part2(self):
        curr = (0, 0)
        perimiter = 0
        sorted_points = [curr]
        for line in self.data:
            _, _, colour = line
            num_steps = int(colour[1:6], 16)
            direction_str = int(colour[-1])
            x, y = self.hex_dir_map[direction_str]
            curr = (curr[0] + x * num_steps, curr[1] + y * num_steps)
            sorted_points.append(curr)
            perimiter += num_steps
        area = area_by_shoelace(sorted_points)
        # picks theorem
        return (area + 1) + perimiter/2


def area_by_shoelace(sorted_points):
    x, y = zip(*sorted_points)
    return abs(sum(i * j for i, j in zip(x, y[1:] + y[:1])) - sum(i * j for i, j in zip(x[1:] + x[:1], y))) / 2


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
