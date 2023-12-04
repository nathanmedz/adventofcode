import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        with open(file, 'r') as f:
            for line in f.read().strip().split('\n'):
                id_str, games_str = line.split(': ')
                id_num = int(id_str.strip('Game '))
                games = games_str.split('; ')
                yield {'id': id_num, 'games': games}

    def part1(self):
        maxes = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        total = 0
        for game_row in self.parse():
            id_num = game_row.get('id')
            possible = True
            for game in game_row.get('games'):
                for pull in game.split(', '):
                    num, colour = pull.split(' ')
                    if maxes[colour] < int(num):
                        possible = False
                        break

            if possible:
                total += id_num
        return total

    def part2(self):
        total = 0
        for game_row in self.parse():
            mins = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            for game in game_row.get('games'):
                for pull in game.split(', '):
                    num, colour = pull.split(' ')
                    mins[colour] = max(mins[colour], int(num))
            total += mins['red'] * mins['blue'] * mins['green']
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
