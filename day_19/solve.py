import functools


def part1():
    blueprints = parse()
    total = 0
    for i, blueprint in enumerate(blueprints, 1):
        max_costs = (0, 0, 0, 999)
        for j, costs in enumerate(blueprint):
            max_costs = tuple(max(max_costs[k], costs[k]) for k in range(4))
        total += i * dfs_nodes(0, (0,0,0,0), (1, 0, 0, 0), blueprint, max_costs, 25)
        print(f'{i} Done')
    print(total)

def part2():
    blueprints = parse()[:3]
    total = 1
    for i, blueprint in enumerate(blueprints, 1):
        max_costs = (0, 0, 0, 999)
        for j, costs in enumerate(blueprint):
            max_costs = tuple(max(max_costs[k], costs[k]) for k in range(4))
        total *= dfs_nodes(0, (0,0,0,0), (1, 0, 0, 0), blueprint, max_costs, 33)
        print(f'{i} Done')
    print(total)

def parse():
    blueprints = []
    with open('input.txt') as f:
        for line in f.readlines():
            l = line.strip().split(' ')
            blueprints.append((
                (int(l[6]), 0, 0, 0),
                (int(l[12]), 0, 0, 0),
                (int(l[18]), int(l[21]), 0, 0),
                (int(l[27]), 0, int(l[30]), 0)
            ))
    return blueprints

@functools.cache
def dfs_nodes(current_time, resources, rates, blueprint, max_costs, max_time, skip=False):
    current_time += 1
    if current_time >= max_time:
        return resources[3]

    # build geode if possible
    if all([resources[res_idx] >= res_cost for res_idx,res_cost in enumerate(blueprint[3])]):
        new_res = tuple([resources[resource_idx] - i + rates[resource_idx] for resource_idx, i in enumerate(blueprint[3])])
        new_rates = tuple([rate + int(res_idx == 3) for res_idx , rate  in enumerate(rates)])
        return dfs_nodes(current_time, new_res, new_rates, blueprint, max_costs, max_time)

    outcomes = []
    for resource_idx, resource_costs in enumerate(blueprint):
        if all([resources[res_idx] >= res_cost for res_idx,res_cost in enumerate(resource_costs)]):
            if rates[resource_idx] >= max_costs[resource_idx]:
                continue
            old_res = tuple([resources[resource_idx] - rates[resource_idx] for resource_idx, i in enumerate(resource_costs)])
            if all([old_res[res_idx] >= res_cost for res_idx,res_cost in enumerate(resource_costs)]) and skip:
                continue
            new_res = tuple([resources[resource_idx] - i + rates[resource_idx] for resource_idx, i in enumerate(resource_costs)])
            new_rates = tuple([rate + int(res_idx == resource_idx) for res_idx , rate  in enumerate(rates)])
            outcomes.append(dfs_nodes(current_time, new_res, new_rates, blueprint, max_costs, max_time))


    resources = tuple([i + rates[resource_idx] for resource_idx, i in enumerate(resources)])
    outcomes.append(dfs_nodes(current_time, resources, rates, blueprint, max_costs, max_time, True))

    return max(outcomes)


if __name__ == '__main__':
    part2()