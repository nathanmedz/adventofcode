import argparse
from collections import defaultdict


class Solver:
    def __init__(self, test=False):
        self.test = test
        self.data = self.parse()

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        with open(file, 'r') as f:
            return f.read().strip('\n').split(',')


    def part1(self):
        total = 0
        for bunch in self.data:
            total += _hash(bunch)
        return total

    def part2(self):
        total = 0
        boxes = defaultdict(list)
        for bunch in self.data:
            if '=' in bunch:
                label , focal_length = bunch.split('=')
                box_id = _hash(label)
                box_contents = boxes[box_id]
                for item in box_contents:
                    if item.get(label):
                        item[label] = int(focal_length)
                        break
                else:
                    box_contents.append({label: int(focal_length)})
            else:
                label = bunch.strip('-')
                box_id = _hash(label)
                box_contents = boxes[box_id]
                for item in box_contents:
                    if item.get(label):
                        box_contents.remove(item)
                        break

        for box_idx, lenses in boxes.items():
            for i, lens in enumerate(lenses):
                total += (box_idx + 1) * (i+1) * list(lens.values())[0]

        return total


def _hash(bunch):
    curr = 0
    for char in bunch:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr


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
