import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        out = []
        with open(file, 'r') as f:
            for line in f.read().strip().split('\n'):
                out.append(line)
        return out

    @staticmethod
    def check_int(val):
        try:
            return int(val)
        except ValueError:
            return None

    @staticmethod
    def check_symbols_around(maze, start_x, start_y, len_x):
        for y in [start_y - 1, start_y, start_y + 1]:
            if y < 0:
                continue
            for x in range(start_x - 1, start_x + len_x + 1):
                if x < 0:
                    continue
                try:
                    check_loc = maze[y][x]
                    if check_loc != '.' and Solver.check_int(check_loc) is None:
                        return True
                except IndexError:
                    pass
        return False

    @staticmethod
    def get_number_at_loc(maze, x, y):
        start = x
        if Solver.check_int(maze[y][x]) is None:
            return None
        else:
            while True:
                if start == 0:
                    break
                left_num = Solver.check_int(maze[y][start - 1])
                if left_num is not None:
                    start = start - 1
                else:
                    break

            end = start
            while True:
                if end > len(maze[y]): break
                right_num = Solver.check_int(maze[y][end + 1])
                if right_num is not None:
                    end = end + 1
                else:
                    break

        return int(maze[y][start:end+1])

    @staticmethod
    def check_numbers_around(maze, start_x, start_y):
        numbers_found = []
        for y in range(start_y - 1, start_y + 2):
            if y < 0:
                continue
            for x in range(start_x - 1, start_x + 2):
                if x < 0:
                    continue
                try:
                    num = Solver.get_number_at_loc(maze, x, y)
                    if num is not None:
                        numbers_found.append(num)
                except IndexError:
                    pass
        return numbers_found

    def part1(self):
        data = self.parse()
        total = 0
        for y, line in enumerate(data):
            start = None
            for x, val in enumerate(line):
                if Solver.check_int(val) is not None:
                    if start is None:
                        start = x
                elif start is not None:
                    if Solver.check_symbols_around(data, start, y, x - start):
                        total += int(line[start:x])
                    start = None
            if start is not None:
                if Solver.check_symbols_around(data, start, y, len(line) - start):
                    total += int(line[start:len(line)])

        return total

    def part2(self):
        data = self.parse()
        total = 0
        for y, line in enumerate(data):
            for x, val in enumerate(line):
                if val == '*':
                    vals = list(set(Solver.check_numbers_around(data, x, y)))
                    if len(vals) == 2:
                        total += vals[0] * vals[1]
        return total


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
