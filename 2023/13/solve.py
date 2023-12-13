import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        data = []
        with open(file, 'r') as f:
            for lines in f.read().split('\n\n'):
                data.append([line for line in lines.split('\n')])
        return data

    @staticmethod
    def get_score(puzzle, bit_count=0):
        rows = [row.replace('.', '0',).replace('#', '1') for row in puzzle]
        reversed_rows = rows[::-1]

        for idx in range(len(rows)//2):
            if (int(''.join(rows[:idx+1]), 2) ^ int(''.join(rows[idx+1:(idx*2) + 2][::-1]), 2)).bit_count() == bit_count:
                return idx + 1
            if (int(''.join(reversed_rows[:idx+1]), 2) ^ int(''.join(reversed_rows[idx+1:(idx*2) + 2][::-1]), 2)).bit_count() == bit_count:
                return len(rows) - idx - 1
        return 0

    @staticmethod
    def transpose(rows):
        return [''.join(i) for i in zip(*rows)]

    def part1(self):
        return sum(100*Solver.get_score(i, 0) + solver.get_score(Solver.transpose(i), 0) for i in self.data)

    def part2(self):
        return sum(100*Solver.get_score(i, 1) + solver.get_score(Solver.transpose(i), 1) for i in self.data)


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
