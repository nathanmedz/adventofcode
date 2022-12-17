
def part1():
    result_map = {
        "A": { "X": 4, "Y": 8, "Z": 3 },
        "B": { "X": 1, "Y": 5, "Z": 9 },
        "C": { "X": 7, "Y": 2, "Z": 6 }
    }
    with open('input.txt') as f:
        total = 0
        for line in f.readlines():
            a, b = line.strip('\n').split(' ')
            total += result_map[a][b]

    print(total)

def part2():
    result_map = {
        "A": { "X": 3, "Y": 4, "Z": 8 },
        "B": { "X": 1, "Y": 5, "Z": 9 },
        "C": { "X": 2, "Y": 6, "Z": 7 }
    }
    with open('input.txt') as f:
        total = 0
        for line in f.readlines():
            a, b = line.strip('\n').split(' ')
            total += result_map[a][b]

    print(total)




if __name__ == '__main__':
    part1()