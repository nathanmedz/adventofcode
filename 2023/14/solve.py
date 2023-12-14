import argparse


def transpose(rows):
    return [''.join(i) for i in zip(*rows)]


def tilt(rows):
    return transpose(['#'.join(''.join(sorted(part, reverse=True)) for part in column.split('#')) for column in transpose(rows)])


def rotate(data):
    return [''.join(i[::-1]) for i in transpose(data)]


def spin(data, cycles=1):
    for i in range(4*cycles):
        data = rotate(tilt(data))
    return data


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        data = []
        with open(file, 'r') as f:
            for line in f.readlines():
                data.append(line.strip('\n'))
        return data

    def part1(self):
        tilted = tilt(self.data)
        total = sum([row.count('O') * (i + 1) for i, row in enumerate(tilted[::-1])])
        return total

    def part2(self):
        res_map = {}
        data = self.data
        cycle_idx = 0
        while True:
            data = spin(data)
            if tuple(data) in res_map:
                cycle_length = cycle_idx - res_map[tuple(data)]
                break
            else:
                res_map[tuple(data)] = cycle_idx
            cycle_idx += 1

        needed_rotations = ((1000000000 - cycle_idx) % cycle_length) - 1
        for i in range(needed_rotations):
            data = spin(data)

        return sum([row.count('O') * (i + 1) for i, row in enumerate(data[::-1])])


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
