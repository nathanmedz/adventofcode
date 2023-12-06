import argparse


class Solver:
    def __init__(self, test=False):
        self.test = test

    def parse(self):
        file = 'test.txt' if self.test else 'input.txt'
        maps = []
        with open(file, 'r') as f:
            lines = f.readlines()
            seeds = lines[0].strip().split(': ')[-1].split()
            all_lines = ''.join(lines[2:]).split('\n\n')
            for line in all_lines:
                current_map = {}
                for map_row in line.split('\n')[1:]:
                    end, start, length = map_row.split()
                    end, start, length = int(end), int(start), int(length)
                    current_map[range(start, start + length)] = end - start
                maps.append(current_map)
        return {'maps': maps, 'seeds': seeds}

    def part1(self):
        data = self.parse()
        outputs = []
        for seed in data.get('seeds'):
            val = int(seed)
            for m in data.get('maps'):
                for key in m.keys():
                    if val in key:
                        val = val + m[key]
                        break

            outputs.append(val)
        return min(outputs)

    def part2(self):
        data = self.parse()
        seeds = data.get('seeds')
        curr_ranges = {range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])): 0 for i in range(0, len(seeds), 2)}
        for m in data.get('maps'):
            curr_sorted = sorted(curr_ranges.keys(), key=lambda x: x[0])
            map_sorted = sorted(m.keys(), key=lambda x: x[0])
            for seed_range in curr_sorted:
                for map_range in map_sorted:
                    seed_start, seed_end = seed_range[0], seed_range[-1]
                    map_start, map_end = map_range[0], map_range[-1]
                    if seed_start < map_start:
                        if seed_end < map_end:
                            break
                        elif seed_end in map_range:
                            curr_adj = curr_ranges.pop(seed_range)
                            curr_ranges[range(seed_start, map_start)] = curr_adj
                            curr_ranges[range(map_start, seed_end + 1)] = curr_adj + m[map_range]
                            break
                        else:
                            curr_adj = curr_ranges.pop(seed_range)
                            curr_ranges[range(seed_start, map_start)] = curr_adj
                            curr_ranges[range(map_start, map_end + 1)] = curr_adj + m[map_range]
                            seed_range = range(map_end + 1, seed_end + 1)
                            curr_ranges[seed_range] = curr_adj

                    elif seed_start in map_range:
                        if seed_end in map_range:
                            curr_adj = curr_ranges.pop(seed_range)
                            curr_ranges[seed_range] = curr_adj + m[map_range]
                            break
                        else:
                            curr_adj = curr_ranges.pop(seed_range)
                            curr_ranges[range(seed_start, map_end + 1)] = curr_adj + m[map_range]
                            seed_range = range(map_end + 1, seed_end + 1)
                            curr_ranges[seed_range] = curr_adj
            curr_ranges = {range(i[0] + j, i[-1] + j + 1): 0 for i, j in curr_ranges.items()}

        out = 9999999999
        for r, adj in curr_ranges.items():
            out = min(r[0] + adj, out)
        return out


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
