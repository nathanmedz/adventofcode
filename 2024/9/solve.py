import argparse

from helpers.solver_base import SolverBase


def create_map(data):
    out = []
    block = True
    i = 0
    for d in data:
        if block:
            out.extend([[str(i)] for _ in range(int(d))])
            i += 1
        else:
            out.extend([["."] for _ in range(int(d))])
        block = not block
    return out


def count_total(out):
    total = 0
    for i, j in enumerate(out):
        int_j = int(j[0] if j[0] != "." else 0)
        total += i * int_j
    return total


def get_block(line, start, char, direction):
    end = start
    while end >= 1 and line[end + 1 * direction][0] == char:
        end += 1 * direction
    if direction == -1:
        start += 1
    else:
        end += 1
    return start, end


class Solver(SolverBase):
    def part1(self):
        data = self.parse_as_line()
        out = create_map(data)
        left = 0
        right = len(out) - 1
        while left <= right:
            if out[left][0] != ".":
                left += 1
            elif out[right][0] == ".":
                right -= 1
            else:
                out[left], out[right] = out[right], out[left]
                left += 1
                right -= 1

        return count_total(out)

    def part2(self):
        data = self.parse_as_line()
        out = create_map(data)
        right = len(out) - 1
        while right > 0:
            block = out[right][0]
            if block != ".":
                right_start, right = get_block(out, right, block, -1)
            else:
                right -= 1
                continue

            block_length = right_start - right
            left_start = None

            for left in range(0, right):
                left_char = out[left][0]
                if left_char == ".":
                    left_start, left = get_block(out, left, left_char, 1)
                else:
                    continue

                left_block_length = left - left_start
                if left_block_length >= block_length:
                    (
                        out[left_start : left_start + block_length],
                        out[right:right_start],
                    ) = (
                        out[right:right_start],
                        out[left_start : left_start + block_length],
                    )

                    break

            right -= 1

        return count_total(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
