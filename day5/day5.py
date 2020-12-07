filename = "/home/xmbomb/dev/aoc2020/day5/input.txt"


def get_lower_half(list):
    length = len(list)
    return list[0:int(length / 2)]


def get_upper_half(list):
    length = len(list)
    return list[int(length / 2):length]


def get_row_col(line):
    row_numbers = list(range(0, 127 + 1))
    col_numbers = list(range(0, 7 + 1))
    for char in line:
        if char == 'F':
            row_numbers = get_lower_half(row_numbers)
        elif char == 'B':
            row_numbers = get_upper_half(row_numbers)
        elif char == 'L':
            col_numbers = get_lower_half(col_numbers)
        elif char == 'R':
            col_numbers = get_upper_half(col_numbers)
        # print(f'Keeping row numbers {row_numbers[0]} .. {row_numbers[len(row_numbers) - 1]}')
        # print(f'Keeping col numbers {col_numbers[0]} .. {col_numbers[len(col_numbers) - 1]}')
    return (row_numbers[0], col_numbers[0])


def calc(row, col):
    return row * 8 + col


def test(line):
    (row, col) = get_row_col(line)
    print(calc(row, col))

def part2(l):
    l.sort()
    full_range = list(range(l[0], l[len(l)-1] + 1))
    return [x for x in full_range if x not in l]

test("FBFBBFFRLR")
test("BFFFBBFRRR")
test("BBFFBBFRLL")

with open(filename, 'r') as file:
    lines = file.read().strip().split('\n')
    results = [calc(*get_row_col(line)) for line in lines]
    print(f'max is {max(results)}')
    print(f'my seat is {part2(results)[0]}')
