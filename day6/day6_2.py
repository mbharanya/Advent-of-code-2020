from collections import Counter

filename = "/home/xmbomb/dev/aoc2020/day6/input.txt"

def num_intersections(group):
    people = group.split("\n")
    intersections = set.intersection(*[set(person) for person in people])
    return len(intersections)

# print(num_unique("a\nb\nc"))
print(num_intersections("ab\nac"))
print(num_intersections("abc"))

with open(filename, 'r') as file:
    lines = file.read().strip().split('\n\n')
    print(sum([num_intersections(line) for line in lines]))
    
