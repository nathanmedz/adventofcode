import argparse
from collections import defaultdict


def seperate_valid(rule_dict, lines):
    valid = []
    invalid = []
    for line in lines:
        for i in line:
            afters = rule_dict.get(i)
            if not afters:
                continue
            if any(a in line and line.index(a) < line.index(i) for a in afters):
                invalid.append(line)
                break
        else:
            valid.append(line)
    return valid, invalid


def reorder_line(rule_dict, line):
    for i in line:
        afters = rule_dict.get(i)
        if not afters:
            continue
        for a in afters:
            if a not in line:
                continue
            a_idx = line.index(a)
            i_idx = line.index(i)
            if a_idx < i_idx:
                line[a_idx], line[i_idx] = line[i_idx], line[a_idx]
                return reorder_line(rule_dict, line)
    else:
        return line


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            rules, lines = f.read().strip().split("\n\n")
            rules = [list(map(int, i.split("|"))) for i in rules.split("\n")]
            lines = [list(map(int, i.split(","))) for i in lines.split("\n")]
            return rules, lines

    def part1(self):
        rules, lines = self.parse()
        rule_dict = defaultdict(list)
        for rule in rules:
            rule_dict[rule[0]].append(rule[1])
        valid, _ = seperate_valid(rule_dict, lines)
        return sum([v[len(v) // 2] for v in valid])

    def part2(self):
        rules, lines = self.parse()
        rule_dict = defaultdict(list)
        for rule in rules:
            rule_dict[rule[0]].append(rule[1])
        _, invalid = seperate_valid(rule_dict, lines)

        return sum([reorder_line(rule_dict, v)[len(v) // 2] for v in invalid])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    if args.part == 2:
        print(solver.part2())
    else:
        print(solver.part1())
