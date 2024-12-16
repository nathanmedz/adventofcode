adj4 = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
)


def turn(vec, direction="R"):
    if direction == "R":
        return (-vec[1], vec[0])
    else:
        return (vec[1], -vec[0])


def move(curr, direction):
    return (curr[0] + direction[0], curr[1] + direction[1])
