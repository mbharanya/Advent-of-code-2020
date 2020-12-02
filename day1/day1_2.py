import itertools

filename = "input.txt"

with open(filename) as f:
    lines = f.readlines()
    lines = [int(x.strip()) for x in lines]
    for (a,b,c) in itertools.product(lines, lines.copy(), lines.copy()):
        if(a + b + c == 2020):
            print(a,b,c)
            print(a * b * c)