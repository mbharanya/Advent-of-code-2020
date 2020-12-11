import re

filename = "/home/xmbomb/dev/aoc2020/day7/input.txt"


class Bag:
    def __init__(self, amount: int, color: str, sub_bags):
        self.amount = amount
        self.color = color
        self.sub_bags = sub_bags

    def __str__(self):
        return (f"{self.amount} x {self.color} {len(self.sub_bags)} sub_bags")
    
    def can_contain_bag(self, bag):
        return bag.color in map(lambda x: x.color, self.sub_bags) 
    

test_rules = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

parse_regex = "(.*) bags contain (.*)"
parse_contains = "([0-9]) (.*) bags?"

start_bag = "shiny gold"


def flatten(l):
    newlist = [item for items in l for item in items]
    return newlist


def parse_rule(rule):
    (base_bag_color, can_contain_str) = re.findall(parse_regex, rule)[0]
    contains = flatten(list([re.findall(parse_contains, s)
                             for s in can_contain_str.split(', ')]))

    sub_bags = []
    if len(contains) > 0:
        sub_bags = list(map(lambda element: Bag(
            element[0], element[1], []), list(contains)))

    bag_rules = Bag(1, base_bag_color, sub_bags)
    return bag_rules
def test():
    bag_map = []
    for rule in test_rules.strip().split("\n"):
        bag_rules = parse_rule(rule)
        bag_map.append(bag_rules)
    bag_to_find = Bag(1, start_bag, [])
    amount = recursively_get_bag(bag_map, bag_to_find, 0, [])
    print(amount)



def recursively_get_bag(bag_map, bag_to_find, i, found_bags):
    bags_that_can_contain_start_bag = list(filter(lambda v: v.can_contain_bag(bag_to_find), bag_map))
    print(f'finding bag for color {bag_to_find.color}')
    if(len(bags_that_can_contain_start_bag) > 0):
        for b in bags_that_can_contain_start_bag:
            if (b not in found_bags):
                found_bags.append(b)
                i = recursively_get_bag(bag_map, b, i + 1, found_bags)
    return i


with open(filename, 'r') as file:
    lines = file.read().strip().split("\n")
    bag_map = []
    for rule in lines:
        bag_rules = parse_rule(rule)
        bag_map.append(bag_rules)
    bag_to_find = Bag(1, start_bag, [])
    amount = recursively_get_bag(bag_map, bag_to_find, 0, [])
    print(amount)

