import argparse
from collections import defaultdict
from helpers.solver_base import SolverBase


def step(robots, iters, lx, ly):
    for robot in robots:
        robot["px"] = (robot["px"] + robot["vx"] * iters) % lx
        robot["py"] = (robot["py"] + robot["vy"] * iters) % ly
    return robots


def make_robo_dict(robots, lx, ly):
    robot_map = defaultdict(list)
    for robot in robots:
        coords = (robot["px"], robot["py"])
        robot_map[coords].append(coords)
    robo_dict = {"x": defaultdict(int), "y": defaultdict(int)}

    for y in range(ly):
        for x in range(lx):
            if (x, y) in robot_map:
                robo_dict["x"][x] += 1
                robo_dict["y"][y] += 1
    return robo_dict


def print_robots(robots, lx, ly):
    robot_map = defaultdict(list)
    for robot in robots:
        coords = (robot["px"], robot["py"])
        robot_map[coords].append(coords)
    robo_list = []
    for y in range(ly):
        for x in range(lx):
            if (x, y) in robot_map:
                print(len(robot_map[(x, y)]), end="")
            else:
                print(".", end="")
        print("\r")
    return robo_list


class Solver(SolverBase):
    def parse(self):
        robots = []
        for line in self.parse_as_lines():
            r, v = line.strip().split(" ")
            r = r.strip("p=").split(",")
            v = v.strip("v=").split(",")
            robots.append(
                {
                    "px": int(r[0]),
                    "py": int(r[1]),
                    "vx": int(v[0]),
                    "vy": int(v[1]),
                }
            )
        return robots

    def part1(self):
        robots = self.parse()
        iters = 100
        if self.test:
            lx = 11
            ly = 7
        else:
            lx = 101
            ly = 103

        robots = step(robots, iters, lx, ly)

        quadrants = [0, 0, 0, 0]
        for robot in robots:
            px, py = robot["px"], robot["py"]
            if py < ly // 2:
                if px < lx // 2:
                    quadrants[0] += 1
                elif px > lx // 2:
                    quadrants[1] += 1
            elif py > ly // 2:
                if px < lx // 2:
                    quadrants[2] += 1
                elif px > lx // 2:
                    quadrants[3] += 1

        total = 1
        for i in quadrants:
            total *= i
        return total

    def part2(self):
        robots = self.parse()
        if self.test:
            lx = 11
            ly = 7
        else:
            lx = 101
            ly = 103

        total = 0
        while True:
            total += 1
            robots = step(robots, 1, lx, ly)
            robo_dict = make_robo_dict(robots, lx, ly)
            if any([i > lx // 4 for i in robo_dict["x"].values()]) and any(
                [i > ly // 4 for i in robo_dict["y"].values()]
            ):
                print_robots(robots, lx, ly)
                return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    solver = Solver(args.test)
    print(solver.part2() if args.part == 2 else solver.part1())
