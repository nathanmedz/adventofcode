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
                puzzle_lines = []
                for line in lines.split('\n'):
                    puzzle_lines.append(line)
                data.append(puzzle_lines)
        return data

    @staticmethod
    def get_column_value(puzzle, bit_count=0):
        rows = [row.replace('.', '0',).replace('#', '1') for row in puzzle]
        columns = [''] * len(rows[0])
        for row in rows:
            for idx, char in enumerate(row):
                columns[idx] += char

        reversed_rows = rows[::-1]

        for idx in range(len(rows)//2):
            if (int(''.join(rows[:idx+1]), 2) ^ int(''.join(rows[idx+1:(idx*2) + 2][::-1]), 2)).bit_count() == bit_count:
                return 100*(idx + 1)
            if (int(''.join(reversed_rows[:idx+1]), 2) ^ int(''.join(reversed_rows[idx+1:(idx*2) + 2][::-1]), 2)).bit_count() == bit_count:
                return 100*(len(rows) - idx - 1)

        reversed_columns = columns[::-1]
        for idx in range(len(columns)//2):
            if (int(''.join(columns[:idx+1]), 2) ^ int(''.join(columns[idx+1:(idx*2) + 2][::-1]), 2)).bit_count() == bit_count:
                return idx + 1
            if (int(''.join(reversed_columns[:idx+1]), 2) ^ int(''.join(reversed_columns[idx+1:(idx*2) + 2][::-1]), 2)).bit_count() == bit_count:
                return len(columns) - idx - 1

    def part1(self):
        return sum([Solver.get_column_value(i, 0) for i in self.data])

    def part2(self):
        return sum([Solver.get_column_value(i, 1) for i in self.data])


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
