
def mix(initial, n=1):
    l = len(initial)
    index_map = [i for i in range(l)]
    for _ in range(n):
        for initial_idx, val in enumerate(initial):
            if val == 0:
                continue
            current_idx = index_map.index(initial_idx)
            final_idx = (current_idx + val) % (l - 1)
            swap_idx = index_map.pop(current_idx)
            index_map.insert(final_idx, swap_idx)

    return [initial[i] for i in index_map]

def part1():
    initial = parse()
    mixed = mix(initial, 1)
    print(sum([mixed[(mixed.index(0)+n) % len(initial)] for n in (1000, 2000, 3000)]))


def part2():
    key = 811589153
    initial = [i* key for i in parse()]
    mixed = mix(initial, 10)
    print(sum([mixed[(mixed.index(0)+n) % len(initial)] for n in (1000, 2000, 3000)]))


def parse():
    with open('input.txt') as f:
        return [int(l.strip()) for l in f.readlines()]


if __name__ == '__main__':
    part2()
