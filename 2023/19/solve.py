import argparse
import math
import re
from collections import defaultdict
from functools import reduce


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        out = {'workflows': {}, 'ratings': []}
        with open(file, 'r') as f:
            workflows, ratings = f.read().split('\n\n')
            for line in workflows.split('\n'):
                id_str, directions = line.strip('}').split('{')
                direction_list = []
                for d in directions.split(','):
                    if ':' not in d:
                        condition, target = 'True', d
                    else:
                        condition, target = d.split(':')
                    direction_list.append((condition,target))
                out['workflows'][id_str] = direction_list
            for line in ratings.split('\n'):
                line = line.strip("{").strip('}').split(',')
                out['ratings'].append({i.split('=')[0]: int(i.split('=')[1]) for i in line})

        return out

    def part1(self):
        total = 0
        workflows = self.data.get('workflows')
        for rating in self.data.get('ratings'):
            x, m, a, s = rating['x'], rating['m'], rating['a'], rating['s']
            curr_workflow = workflows.get('in')
            rejected, accepted = False, False
            while True:
                if rejected:
                    break
                elif accepted:
                    total += sum([x, m, a, s])
                    break
                for cond, target in curr_workflow:
                    if eval(cond):
                        if target == 'A':
                            accepted = True
                        elif target == 'R':
                            rejected = True
                        else:
                            curr_workflow = workflows[target]
                        break
        return total

    def part2(self):
        workflows = self.data.get('workflows')
        ranges = {
            key: [[[], [], [], []]] for key in workflows.keys()
        }
        ranges['A'] = [[[], [], [], []]]
        ranges['R'] = [[[], [], [], []]]

        ranges['in'] = [
            [[i for i in range(1, 4001)], [i for i in range(1, 4001)], [i for i in range(1, 4001)], [i for i in range(1, 4001)] ]
        ]
        char_idx_map = {'x': 0, 'm':1, 'a':2, 's':3}
        while True:
            range_keys = [i for i in ranges.keys()]
            if is_finished(ranges):
                break
            for key in range_keys:
                if key in {'R', 'A'}:
                    continue
                curr_id = key
                curr_workflow = workflows.get(curr_id)
                for cond, target in curr_workflow:
                    if cond == 'True':
                        ranges[target].extend(ranges[curr_id])
                        ranges[curr_id] = [[[], [], [], []]]
                        break
                    else:
                        char = cond[0]
                        cond = cond.replace('a', 'i').replace('x', 'i').replace('m', 'i').replace('s', 'i')
                        all_ranges = ranges[curr_id]
                        for local_ranges in all_ranges:
                            curr_range = local_ranges[char_idx_map[char]]
                            pos_range = [i for i in curr_range if eval(cond)]
                            neg_range = [i for i in curr_range if not eval(cond)]
                            range_to_add = []
                            for key in 'xmas':
                                if key == char:
                                    range_to_add.append(pos_range)
                                else:
                                    range_to_add.append(local_ranges[char_idx_map[key]])
                            if any(i for i in range_to_add):
                                ranges[target].append(range_to_add)
                            local_ranges[char_idx_map[char]] = neg_range

        return sum(reduce(lambda x, y: x * y, [len(i) for i in loc_ranges]) for loc_ranges in ranges['A'])


def calc_total(ranges):
    total = 0
    for key, values in ranges.items():
        for loc_ranges in values:
            total += reduce(lambda x, y: x * y, [len(i) for i in loc_ranges])
    return total


def is_finished(ranges):
    total = 0
    for key in ['R', 'A']:
        for loc_ranges in ranges[key]:
            total += reduce(lambda x, y: x * y, [len(i) for i in loc_ranges])
    return total == 256000000000000


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
