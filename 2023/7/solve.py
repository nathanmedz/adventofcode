import argparse
from collections import defaultdict
from functools import cmp_to_key


class Solver:
    hand_grouping_map = {
        '55555': 6,
        '44441': 5,
        '33322': 4,
        '33311': 3,
        '22221': 2,
        '22111': 1,
        '11111': 0,
    }

    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        out = []
        with open(file, 'r') as f:
            for line in f.readlines():
                hand, bet = line.split()
                out.append((hand, bet))
        return out

    def compare(self, item1, item2):
        for a, b in zip(item1['numbered_hand'], item2['numbered_hand']):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        return 0

    def part1(self):
        data = self.parse()
        parsed = defaultdict(list)

        for hand, bet in data:
            numbered_hand = [i.replace('A', '14').replace('K', '13').replace('Q', '12').replace('J', '11').replace('T', '10') for i in hand]
            parsed_hand = ''.join(sorted([str(numbered_hand.count(i)) for i in numbered_hand], reverse=True))
            parsed[Solver.hand_grouping_map[parsed_hand]].append({'bet': bet,  'numbered_hand': numbered_hand})

        sorted_hands = []
        for i in range(7):
            sorted_hands.extend(sorted(parsed[i], key=cmp_to_key(self.compare)))

        total = 0
        for idx, hand in enumerate(sorted_hands):
            val = (idx + 1) * int(hand['bet'])
            total += val

        return total

    def part2(self):
        data = self.parse()
        parsed = defaultdict(list)

        for hand, bet in data:
            numbered_hand = [i.replace('A', '14').replace('K', '13').replace('Q', '12').replace('T', '10').replace('J', '0') for i in hand]

            if 'J' in hand:
                hand_counts = sorted([(letter, hand.count(letter)) for letter in hand], key=lambda x: x[1], reverse=True)
                for letter, count in hand_counts:
                    if letter != 'J':
                        hand = [i.replace('J', letter) for i in hand]
                        alt_numbered_hand = [i.replace('A', '14').replace('K', '13').replace('Q', '12').replace('T', '10') for i in hand]
                        break
                else:
                    alt_numbered_hand = ['0'] * 5

                parsed_hand = ''.join(sorted([str(alt_numbered_hand.count(i)) for i in alt_numbered_hand], reverse=True))
            else:
                parsed_hand = ''.join(sorted([str(numbered_hand.count(i)) for i in numbered_hand], reverse=True))
            parsed[Solver.hand_grouping_map[parsed_hand]].append({'bet': bet, 'numbered_hand': numbered_hand, 'hand': hand, 'parsed_hand':parsed_hand})

        sorted_hands = []
        for i in range(7):
            sorted_hands.extend(sorted(parsed[i], key=cmp_to_key(self.compare)))

        total = 0
        for idx, hand in enumerate(sorted_hands):
            val = (idx + 1) * int(hand['bet'])
            total += val

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
