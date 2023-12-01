import string

scoring = string.ascii_lowercase + string.ascii_uppercase


def part1():
    with open('input.txt') as f:
        max_food = 0
        for elf_obj in f.read().split('\n\n'):
            max_food = max(sum(int(i) for i in elf_obj.strip().split('\n')), max_food)

    print(max_food)

def part2():
    elf_food = []
    with open('input.txt') as f:
        for elf_obj in f.read().split('\n\n'):
            elf_food.append(sum(int(i) for i in elf_obj.strip().split('\n')))

    print(sum(sorted(elf_food)[-3:]))

if __name__ == '__main__':
    part2()