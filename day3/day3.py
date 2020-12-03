filename = "/home/xmbomb/dev/aoc2020/day3/input.txt"


with open(filename, 'r') as file:
    data = file.read().split('\n')


def part1(data, right_amount, down_amount):
    lines, line_length = len(data), len(data[0])
    char_index = 0
    trees = 0
    for i in range(0, lines, down_amount):
        if data[i][char_index] == '#':
            trees += 1
        char_index = (char_index+right_amount) % line_length
    return trees


def part2(data):
    trees = 1
    for right_amount, down_amount in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees *= part1(data, right_amount, down_amount)
    return trees


print(f'Answer for part 1: {part1(data, 3, 1)}')  # 270
print(f'Answer for part 2: {part2(data)}')  # 2122848000