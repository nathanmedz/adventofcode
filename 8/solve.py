
def scenic_score(matrix, i, j):
    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
    ]
    curr_score = 1
    curr_val = int(matrix[i][j])
    for [new_i, new_j] in directions:
        dir_score = 0
        try:
            curr_i, curr_j = i + new_i, j + new_j
            while True:
                if curr_j < 0 or curr_i < 0:
                    raise StopIteration
                try:
                    if int(matrix[curr_i][curr_j]) >= curr_val:
                        dir_score += 1
                        raise StopIteration
                    else:
                        curr_i += new_i
                        curr_j += new_j
                        dir_score += 1
                except IndexError:
                    raise StopIteration
        except StopIteration:
            curr_score *= dir_score

    return curr_score


def is_visible(matrix, i, j):
    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
    ]
    curr_val = int(matrix[i][j])
    for [new_i, new_j] in directions:
        curr_i, curr_j = i + new_i, j + new_j
        while True:
            if curr_j < 0 or curr_i < 0:
                return True
            try:
                if int(matrix[curr_i][curr_j]) >= curr_val:
                    break
                else:
                    curr_i += new_i
                    curr_j += new_j
            except IndexError:
                return True

    return False


def part1():
    with open('input.txt') as f:
        matrix = []
        for line in f.readlines():
            matrix.append([i for i in line.strip('\n')])
        total = 0
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if is_visible(matrix, i, j):
                    total += 1
        print(total)


def part2():
    with open('input.txt') as f:
        matrix = []
        for line in f.readlines():
            matrix.append([i for i in line.strip('\n')])

        total = 0
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                score = scenic_score(matrix, i, j)
                total = max(total, score)

        print(total)


if __name__ == '__main__':
    part2()
