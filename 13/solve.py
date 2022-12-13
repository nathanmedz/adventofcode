
import json


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    elif isinstance(left, int) and not isinstance(right, int):
        return compare([left], right)
    elif isinstance(right, int) and not isinstance(left, int):
        return compare(left, [right])
    else:
        for i in range(min([len(left), len(right)])):
            res = compare(left[i], right[i])
            if res in [True, False]:
                return res
        if len(left) > len(right):
            return False
    return True


def part1():
    pairs = []
    with open('input.txt') as f:
        while True:
            line_1 = f.readline()
            line_2 = f.readline()
            if not line_1 or not line_2:
                break

            new_pair = [json.loads(line_1.strip()), json.loads(line_2.strip())]
            pairs.append(new_pair)
            f.readline()

    correct_pairs = []
    for i, [left, right] in enumerate(pairs, 1):
        if compare(left, right):
            correct_pairs.append(i)
    print(sum(correct_pairs))


def bubbleSort(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(l - i - 1):
            res = compare(arr[j], arr[j+1])
            # print(res, arr[j], arr[j+1])
            if not res:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def part2():
    pairs = [[[2]], [[6]]]
    with open('input.txt') as f:
        while True:
            line_1 = f.readline()
            line_2 = f.readline()
            if not line_1 or not line_2:
                break

            pairs.append(json.loads(line_1.strip()))
            pairs.append(json.loads(line_2.strip()))
            f.readline()

    bubbleSort(pairs)
    first = pairs.index([[2]]) + 1
    second = pairs.index([[6]]) +1
    print(first * second)


if __name__ == '__main__':
    part1()
    part2()
