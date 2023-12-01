
def str_to_snafu(line):
    return sum([5**i * {'2':2, '1':1, '0':0, '-':-1, '=': -2}[char] for i, char in enumerate(line[::-1])])

def snafu_to_str(snafu):
    char_map = {2:'2', 1:'1', 0:'0', -1:'-', -2:'='}
    output = ''
    i = 0
    while snafu != 0:
        out = snafu % (5 ** (i+1)) // (5 ** i)
        if out > 2:
            out -= 5
        snafu -= out * (5**i)
        output += char_map[out]
        i+= 1
    return output[::-1]

def part1():
    total = 0
    with open('input.txt') as f:
        for line in f.readlines():
            total += str_to_snafu(line.strip())
    print(total, snafu_to_str(total))

def part2():
    pass

if __name__ == '__main__':
    part1()
