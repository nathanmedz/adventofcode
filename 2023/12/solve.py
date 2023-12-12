import argparse
from functools import cache


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.springs, self.groups = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        springs, groups = [], []
        with open(file, 'r') as f:
            for line in f.readlines():
                s, g = line.strip('\n').split()
                groups.append(tuple(int(i) for i in g.split(',')))
                springs.append(s)
        return springs, groups

    @staticmethod
    def calc_line_total(s, g):
        line_total = 0
        possible_arrangements = [s]
        while possible_arrangements:
            curr_arrangement = possible_arrangements.pop(0)
            curr_str = ''.join(curr_arrangement)
            if '?' not in curr_arrangement:
                if Solver.is_solution(curr_str, g):
                    line_total += 1
                continue
            else:
                idx = curr_arrangement.index('?')
                for j in ['.', '#']:
                    curr_arrangement[idx] = j
                    if Solver.solution_is_possible(curr_str, g):
                        possible_arrangements.append(curr_arrangement.copy())
        return line_total

    @staticmethod
    def solution_is_possible(spring_line, groups):
        curr_counts = []
        consec = 0
        for i, char in enumerate(spring_line):
            if char == '#':
                consec += 1
            elif char == '.':
                if consec > 0:
                    curr_counts.append(consec)
                    consec = 0
            elif char == '?':
                break

        for c, g in zip(curr_counts, groups):
            if c != g:
                return False

        return True

    @staticmethod
    def is_solution(spring_line, groups):
        return tuple(len(i) for i in spring_line.split('.') if i) == groups

    def part1(self):
        total = 0
        for s, g in zip(self.springs, self.groups):
            t = Solver.calc_line_total([i for i in s], g)
            total += t

        return total

    @cache
    @staticmethod
    def count_valid_arrangements(springs, groups, curr_block):
        if not springs:
            if not groups and curr_block == 0:
                return 1
            if len(groups) == 1 and groups[0] == curr_block:
                return 1
            return 0

        curr_spring, rest_springs = springs[0], springs[1:]
        curr_group, *rest_groups = groups or [0]
        if curr_spring == '?':
            return Solver.count_valid_arrangements('.'+rest_springs, groups, curr_block) + Solver.count_valid_arrangements('#'+rest_springs, groups, curr_block)
        elif curr_spring == '.':
            if curr_block != 0 and curr_block != curr_group:
                return 0
            if curr_block:
                return Solver.count_valid_arrangements(rest_springs, tuple(rest_groups), 0)
            else:
                return Solver.count_valid_arrangements(rest_springs, groups, 0)
        else:
            if curr_block > curr_group:
                return 0
            return Solver.count_valid_arrangements(rest_springs, groups, curr_block+1)

    def part2(self):
        total = 0
        for s, g in zip(self.springs, self.groups):
            s += '?'
            s = (s*5)[:-1]
            g = g*5

            total += Solver.count_valid_arrangements(s, g, 0)
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
