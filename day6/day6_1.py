from collections import Counter

filename = "/home/xmbomb/dev/aoc2020/day6/input.txt"

def num_unique(group):
    group = group.replace("\n", "")
    return len(Counter(group))

print(num_unique("aabc"))

with open(filename, 'r') as file:
    lines = file.read().strip().split('\n\n')
    print(sum([num_unique(line) for line in lines]))
    
