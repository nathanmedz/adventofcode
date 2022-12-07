class File:
    def __init__(self, size, name, parent):
        self.size = int(size)
        self.name = name
        self.parent = parent

    def get_size(self):
        return self.size

    def show(self, level=0):
        print(f'{" "*2*level}- {self.name} (file, size={self.size})')


class Directory:
    def __init__(self, name, children, parent):
        self.name = name
        self.children = children
        self.parent = parent

    def get_size(self):
        return sum(i.get_size() for i in self.children)

    def part1(self):
        total_size = 0
        for child in self.children:
            if isinstance(child, Directory):
                child_size = child.get_size()
                if child_size < 100000:
                    total_size += child_size
                total_size += child.part1()

        return total_size

    def part2(self, needed, smallest):
        for child in self.children:
            if isinstance(child, Directory):
                child_size = child.get_size()
                if needed < child_size < smallest:
                    smallest = child_size
                smallest = child.part2(needed, smallest)

        return smallest

    def get_parent(self):
        return self.parent

    def get_child(self, name):
        for i in self.children:
            if i.name == name:
                return i

    def add_child_dir(self, name):
        self.children.append(Directory(name, [], self))

    def add_child_file(self, size, name):
        self.children.append(File(size, name, self))

    def show(self, level=0):
        print(f'{" "*2*level}- {self.name} (dir)')
        for child in self.children:
            child.show(level+1)


def build_tree():
    root_dir = Directory('/', [], None)
    current_dir = root_dir
    with open('input.txt') as f:
        lines = f.readlines()
        for line in map(str.split, lines):
            if line[0] == '$':
                if line[1] == 'cd':
                    if line[2] == '/':
                        current_dir = root_dir
                    elif line[2] == '..':
                        current_dir = current_dir.get_parent()
                    else:
                        current_dir = current_dir.get_child(line[2])
            elif line[0] == 'dir':
                current_dir.add_child_dir(line[1])
            else:
                current_dir.add_child_file(line[0], line[1])
    return root_dir


def part1():
    root_dir = build_tree()
    print(root_dir.part1())


def part2():
    root_dir = build_tree()
    smallest = 99999999
    needed = 30000000 - (70000000 - root_dir.get_size())
    print(root_dir.part2(needed, smallest))


if __name__ == '__main__':
    part2()