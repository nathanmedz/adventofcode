def input_as_dict(lines):
    out = {}
    for y, line in enumerate(lines):
        for x, j in enumerate(list(line)):
            out[(x, y)] = j
    return out


class SolverBase:
    def __init__(self, test=False):
        self.test = test

    def parse_as_dict(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            return input_as_dict(f.read().strip().split("\n"))

    def parse_as_lines(self):
        file = "test.txt" if self.test else "input.txt"
        with open(file, "r") as f:
            for line in f.read().strip().split("\n"):
                yield line
