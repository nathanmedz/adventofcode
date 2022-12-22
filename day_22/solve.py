class Node:
    directions = {
         90: [1, 0],
        180: [0, 1],
        270: [-1, 0],
        0: [0, -1],
    }
    def __init__(self, x, y, grove, grove_x, grove_y, side_length=50):
        self.x = x
        self.y = y
        self.direction = 90
        self.grove = grove
        self.grove_x = grove_x
        self.grove_y = grove_y
        self.side_length = side_length

    @property
    def section(self):
        if self.side_length <= self.x < self.side_length * 2 and 0 <= self.y < self.side_length:
            return 1
        if self.side_length * 2 <= self.x < self.side_length * 3 and 0 <= self.y <  self.side_length:
            return 2
        if self.side_length <= self.x < self.side_length * 2 and self.side_length <= self.y <  self.side_length * 2:
            return 3
        if self.side_length <= self.x < self.side_length * 2 and self.side_length * 2 <= self.y <  self.side_length * 3:
            return 4
        if 0 <= self.x < self.side_length and self.side_length * 2 <= self.y <  self.side_length * 3:
            return 5
        return 6

    @property
    def normalized_coords(self):
        return self.x % 50, self.y % 50

    def denormalize(self, normalized_x, normalized_y, section):
        section_map = {
            1: (self.side_length, 0),
            2: (2 * self.side_length, 0),
            3: (self.side_length, self.side_length),
            4: (self.side_length, 2 * self.side_length),
            5: (0, 2 * self.side_length),
            6: (0, 3 * self.side_length)
        }
        return normalized_x + section_map[section][0], normalized_y + section_map[section][1]

    def transfer_face(self):
        x, y = self.normalized_coords
        new_direction = self.direction
        if self.section == 1:
            if self.direction == 0:
                new_x, new_y = self.denormalize(0, x, 6)
                new_direction = 90
            elif self.direction == 270:
                new_x, new_y = self.denormalize(0, self.side_length -1 - y, 5)
                new_direction = 90
        if self.section == 2:
            if self.direction == 0:
                new_x, new_y = self.denormalize(x, self.side_length - 1, 6)
            elif self.direction == 90:
                new_x, new_y = self.denormalize(self.side_length - 1, self.side_length -1 - y, 4)
                new_direction = 270
            elif self.direction == 180:
                new_x, new_y = self.denormalize(self.side_length - 1, x, 3)
                new_direction = 270
        if self.section == 3:
            if self.direction == 90:
                new_x, new_y = self.denormalize(y, self.side_length - 1, 2)
                new_direction = 0
            elif self.direction == 270:
                new_x, new_y = self.denormalize(y, 0, 5)
                new_direction = 180
        if self.section == 4:
            if self.direction == 90:
                new_x, new_y = self.denormalize(self.side_length - 1, self.side_length - 1 - y, 2)
                new_direction = 270
            elif self.direction == 180:
                new_x, new_y = self.denormalize(self.side_length - 1, x, 6)
                new_direction = 270
        if self.section == 5:
            if self.direction == 0:
                new_x, new_y = self.denormalize(0, x, 3)
                new_direction = 90
            elif self.direction == 270:
                new_x, new_y = self.denormalize(0, self.side_length - 1 - y, 1)
                new_direction = 90
        if self.section == 6:
            if self.direction == 90:
                new_x, new_y = self.denormalize(y, self.side_length - 1, 4)
                new_direction = 0
            elif self.direction == 180:
                new_x, new_y = self.denormalize(x, 0, 2)
            elif self.direction == 270:
                new_x, new_y = self.denormalize(y, 0, 1)
                new_direction = 180
        return new_x, new_y, new_direction

    def move(self, n):
        x, y = self.directions[self.direction]
        for i in range(n):
            new_x, new_y = self.x + x, self.y + y
            loc_val = self.grove.get((new_x, new_y))
            if not loc_val in ['#', '.']:
                if self.direction == 90:
                    new_x = min(temp_x for temp_x in range(self.grove_x) if self.grove.get((temp_x, new_y)) in ['#', '.'])
                elif self.direction == 180:
                    new_y = min(temp_y for temp_y in range(self.grove_y) if self.grove.get((new_x, temp_y)) in ['#', '.'])
                elif self.direction == 270:
                    new_x = max(temp_x for temp_x in range(self.grove_x) if self.grove.get((temp_x, new_y)) in ['#', '.'])
                else:
                    new_y = max(temp_y for temp_y in range(self.grove_y) if self.grove.get((new_x, temp_y)) in ['#', '.'])
                loc_val = self.grove.get((new_x, new_y))
            if loc_val == '#':
                return self.x, self.y
            else:
                self.x, self.y = new_x, new_y

    def move_cube(self, n):
        for i in range(n):
            x, y = self.directions[self.direction]
            new_direction = self.direction
            new_x, new_y = self.x + x, self.y + y
            loc_val = self.grove.get((new_x, new_y))
            if not loc_val in ['#', '.']:
                new_x, new_y, new_direction = self.transfer_face()
                loc_val = self.grove.get((new_x, new_y))
            if loc_val  == '#':
                return self.x, self.y
            else:
                self.x, self.y, self.direction = new_x, new_y, new_direction

    def show_map(self):
        direction_map = {90:'>', 270:'<', 0: '^', 180: 'v'}
        for y in range(self.grove_y):
            for x in range(self.grove_x):
                if self.x == x and self.y == y:
                    print(direction_map[self.direction], end='')
                else:
                    print(self.grove.get((x,y)) or '', end='')
            print('\n', end='')
        print('\n', end='')


    def rotate(self, direction):
        if direction == 'R':
            self.direction = (self.direction + 90) % 360
        else:
            self.direction = (self.direction - 90) % 360


def part1():
    grove, directions, grove_x, grove_y = parse()
    start_x = min(temp_x for temp_x in range(grove_x) if grove.get((temp_x, 0)) in ['#', '.'])
    start = Node(start_x ,0, grove, grove_x, grove_y)
    while directions:
        curr_direction = directions.pop(0)
        if isinstance(curr_direction, int):
            start.move(curr_direction)
        else:
            start.rotate(curr_direction)

    print(4* (start.x + 1) +  1000* (start.y + 1) + (start.direction / 90) - 1)


def part2():
    grove, directions, grove_x, grove_y = parse()
    start_x = min(temp_x for temp_x in range(grove_x) if grove.get((temp_x, 0)) in ['#', '.'])
    start = Node(start_x ,0, grove, grove_x, grove_y)
    while directions:
        curr_direction = directions.pop(0)
        if isinstance(curr_direction, int):
            start.move_cube(curr_direction)
        else:
            start.rotate(curr_direction)

    print(4* (start.x + 1) +  1000* (start.y + 1) + (start.direction / 90) - 1)


def parse():
    grove = {}
    with open('input.txt') as f:
        raw_grove, raw_directions = f.read().split('\n\n')
    grove_x, grove_y = 0, 0
    for y, l in enumerate(raw_grove.split('\n')):
        grove_x = max(len(l) + 1, grove_x)
        grove_y = y + 1
        for x, val in enumerate(l):
            grove[(x, y)] = val
    directions = []
    curr_str = ''
    raw_directions = list(raw_directions.strip())
    while raw_directions:
        curr = raw_directions.pop(0)
        if curr in ['L', 'R']:
            directions.append(int(curr_str))
            curr_str = ''
            directions.append(curr)
        else:
            curr_str += curr

    if curr_str:
        directions.append(int(curr_str))

    return grove, directions, grove_x, grove_y


if __name__ == '__main__':
    part2()
