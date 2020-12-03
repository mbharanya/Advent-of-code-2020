filename = "/home/xmbomb/dev/aoc2020/day3/input.txt"

with open(filename) as f:
    lines = f.readlines()
    fields = [[]]
    trees = 0
    step_down = 1
    step_side = 2

    line_no = 0

    for line in lines[::step_down]:
        print(line_no)
        line_no += 1
        if (len(line) >= step_side):
            step_side = 2
        if line[step_side] == "#":
            trees += 1
        step_side += 3
    print(trees)

    # for x in range(len(lines)):
    #     for y in range(len(lines[x])):
            
    # for line in lines:
    #     index = lines.index(line)
    #     line = line.strip()
    #     fields.append([index, [char for char in line]])

