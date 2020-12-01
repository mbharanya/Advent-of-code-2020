import itertools

filename = "input.txt"

with open(filename) as f:
    lines = f.readlines()
    lines = [int(x.strip()) for x in lines]
    lines.sort()
    for (a,b) in itertools.product(lines, lines.copy()):
        if(a + b == 2020):
            print(a,b)
            print(a * b)