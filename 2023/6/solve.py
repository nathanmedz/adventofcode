import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        with open(file, 'r') as f:
            lines = f.readlines()
            times = [int(i) for i in lines[0].split(':')[-1].split()]
            distances = [int(i) for i in lines[1].split(':')[-1].split()]
            return zip(times, distances)

    def part1(self):
        data = self.parse()
        total = 1
        for time, distance in data:
            for i in range(time):
                if (time - i) * i > distance:
                    total *= time - i*2 + 1
                    break
        return total

    def part2(self):
        data = [i for i in self.parse()]
        total = 1
        time = int(''.join(str(i[0]) for i in data))
        distance = int(''.join(str(i[1]) for i in data))
        for i in range(time):
            if (time - i) * i > distance:
                total *= time - i*2 + 1
                break
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
