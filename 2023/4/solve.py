import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        out = {}
        with open(file, 'r') as f:
            for line in f.read().strip().split('\n'):
                winning_numbers, my_numbers = line.split(' | ')
                card_number, winning_numbers = winning_numbers.split(':')
                card_number = int(card_number.strip('Card '))
                my_numbers = {int(i) for i in my_numbers.split(' ') if i}
                winning_numbers = {int(i) for i in winning_numbers.split(': ')[-1].split(' ') if i}
                out[card_number] = {'my_numbers': my_numbers, 'winning_numbers': winning_numbers}
        return out

    def part1(self):
        total = 0
        data = self.parse()
        for card_number, line in data.items():
            winners = line.get('my_numbers').intersection(line.get('winning_numbers'))
            if len(winners):
                total += 2**(max(0, len(line.get('my_numbers').intersection(line.get('winning_numbers'))) -1))

        return total

    def part2(self):
        data = self.parse()
        card_count = {int(i): 1 for i in data.keys()}
        for card_number, line in data.items():
            winners = len(line.get('my_numbers').intersection(line.get('winning_numbers')))
            for i in range(1, winners + 1):
                card_count[card_number + i] = card_count[card_number + i] + card_count[card_number]

        return sum(i for i in card_count.values())


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
