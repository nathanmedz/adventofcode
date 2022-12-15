
def parse_input():
    beacons = set()
    sensors = {}
    with open('input.txt') as f:
        for line in f:
            line = line.strip().split()
            sensor = int(line[2].replace('x=', '').replace(',', '')), int(line[3].replace('y=', '').replace(':', ''))
            beacon = int(line[8].replace('x=', '').replace(',', '')), int(line[9].replace('y=', '').replace(':', ''))
            distance = manhattan_distance(sensor, beacon)
            beacons.add(beacon)
            sensors[sensor] = distance

    return beacons, sensors

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def part1():
    beacons, sensors = parse_input()
    total = 0
    y = 2000000
    for x in range(0, 4000000):
        spot = (x, y)
        if spot in beacons:
            continue
        for sensor, distance in sensors.items():
            if manhattan_distance(spot, sensor) <= distance:
                total += 1
                break

    print(total)

def part2():
    beacons, sensors = parse_input()
    r = 4000000
    for y in range(0 , r + 1):
        x = -1
        while x <= r:
            x += 1
            spot = (x, y)
            for sensor, distance in sensors.items():
                this_distance = manhattan_distance(spot, sensor)
                if this_distance <= distance:
                    x = sensor[0] + distance - abs(y - sensor[1])
                    break
            else:
                return x * 4000000 + y



if __name__ == '__main__':
    print(part2())
