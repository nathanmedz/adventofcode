def do_moves(n, directions, print_steps=False):
    direction_idx = 0
    stack = set()
    top_stack = 0
    for piece_idx in range(n):
        piece = get_coords(piece_idx % 5, (3, top_stack + 4))
        top_stack, direction_idx = drop_piece(stack, piece, top_stack, direction_idx, directions, print_steps)
    return top_stack

def drop_piece(stack, piece, top_stack, direction_idx, directions, print_steps=False):
    while True:
        if print_steps:
            show_stack(stack, piece)
        direction = directions[direction_idx]
        direction_idx = (direction_idx + 1) % len(directions)
        moved_piece = move_piece(piece, direction)
        collision = check_collision(moved_piece, stack)
        if collision in [True, None]:
            moved_piece = piece
        if print_steps:
            show_stack(stack, moved_piece)
        piece = move_piece(moved_piece, 'down')
        if check_collision(piece, stack):
            stack.update(moved_piece)
            top_stack = max(top_stack, get_height(moved_piece))
            if print_steps:
                show_stack(stack, set())
            return top_stack, direction_idx


def find_repeat(directions):
    piece_idx = 0
    direction_idx = 0
    stack = set()
    top_stack = 0
    progression = {}
    while True:
        piece = get_coords(piece_idx % 5, (3, top_stack + 4))
        prog_coord = (piece_idx %5, direction_idx)
        if progression.get(prog_coord):
            if progression.get(prog_coord)[2]:
                return progression.get(prog_coord)[0], piece_idx
            else:
                progression[prog_coord] = piece_idx, direction_idx, True
        else:
            progression[prog_coord] = piece_idx, direction_idx, False
        top_stack, direction_idx = drop_piece(stack, piece, top_stack, direction_idx, directions)

        piece_idx += 1


def part1():
    with open('input.txt') as f:
        directions = [i for i in f.readline().strip()]
    print(do_moves(2022, directions))

def part2():
    with open('input.txt') as f:
        directions = [i for i in f.readline().strip()]
    total_iters = 1000000000000

    repeat_start, repeat_end = find_repeat(directions)
    repeat_interval = repeat_end - repeat_start
    initial_total = do_moves(repeat_start, directions)
    repeat_value = do_moves(repeat_start + repeat_interval, directions) - initial_total
    num_repeats = (total_iters - repeat_start) // repeat_interval
    num_remaining = (total_iters - repeat_start ) % repeat_interval
    repeat_total = num_repeats * repeat_value
    remaining_total = do_moves(repeat_start + num_remaining, directions) - initial_total
    print(repeat_total + initial_total + remaining_total)




def show_stack(stack, piece):
    top_stack = get_height(stack)

    for y in range(top_stack + 5, max(0, top_stack - 10), -1):
        for x in range(9):
            if x == 0 or x == 8:
                print('|', end='')
            else:
                if (x, y) in stack:
                    print('#', end='')
                elif (x, y) in piece:
                    print('@', end='')
                else:
                    print('.', end='')

        print('\n', end='')
    print('+-------+\n')



def check_collision(piece, stack):
    for coord in piece:
        if coord[0] == 0 or coord[0] == 8:
            return None
        if coord[1] == 0 or coord in stack:
            return True
    return False

def move_piece(piece, direction):
    directions = {
        '>': (1, 0),
        '<': (-1, 0),
        'down': (0, -1)
    }
    return {(x + directions[direction][0], y + directions[direction][1]) for (x, y) in piece}


def get_height(stack):
    if not stack:
        return 0
    return max(y for (x,y) in stack)

def get_coords(idx, bottom_left):
    x , y = bottom_left
    if idx == 0:
        return {(x, y), (x+1, y), (x+2, y), (x+3, y)}
    elif idx == 1:
        return {(x, y+1), (x+1, y+1), (x+2, y+1), (x+1, y), (x+1, y+2)}
    elif idx == 2:
        return {(x, y), (x+1, y), (x+2, y), (x+2, y+1), (x+2, y+2)}
    elif idx == 3:
        return {(x, y), (x, y+1), (x, y+2), (x, y+3)}
    elif idx == 4:
        return {(x, y), (x, y+1), (x + 1, y+1), (x+1, y)}


if __name__ == '__main__':
    part2()