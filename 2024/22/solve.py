import argparse
from helpers.solver_base import SolverBase
from collections import defaultdict


def iterate(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def mix(num, secret):
    return num ^ secret


def prune(secret):
    return secret % 16777216


class Solver(SolverBase):
    def part1(self):
        total = 0
        for line in self.parse_as_lines():
            secret = int(line)
            for _ in range(2000):
                secret = iterate(secret)
            print(secret)
            total += secret
        return total

    def part2(self):
        all_dicts = {}
        all_changes = set()
        for line in self.parse_as_lines():
            secret = int(line)
            change_dict = {}
            changes = ()
            for _ in range(2000):
                old, secret = secret, iterate(secret)
                old_price, secret_price = old % 10, secret % 10
                price_change = secret_price - old_price
                if len(changes) == 4:
                    changes = changes[1:] + (price_change,)
                else:
                    changes = changes + (price_change,)
                if len(changes) < 4:
                    continue
                else:
                    all_changes.add(changes)
                if changes not in change_dict:
                    change_dict[changes] = secret_price
            all_dicts[line] = change_dict

        change_totals = {change: 0 for change in all_changes}
        for change in all_changes:
            for line, change_dict in all_dicts.items():
                change_totals[change] += change_dict.get(change) or 0

        return sorted(change_totals.items(), key=lambda x: x[1])[-1][1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
