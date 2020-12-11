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
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

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
            int(element[0]), element[1], []), list(contains)))

    bag_rules = Bag(1, base_bag_color, sub_bags)
    return bag_rules
def test():
    bag_map = []
    for rule in test_rules.strip().split("\n"):
        bag_rules = parse_rule(rule)
        bag_map.append(bag_rules)
    bag_to_start = Bag(1, start_bag, [])
    # amount = recursively_get_bag(bag_map, bag_to_start, 1, [])
    amount = get_amount_of_bags(bag_map, bag_to_start)
    print(amount) 


def get_amount_of_bags(bag_map, bag_to_find):
    bag_found = list(filter(lambda v: v.color == bag_to_find.color, bag_map))[0]
    amount = 0
    for sub_bag in bag_found.sub_bags:
        amount = amount + sub_bag.amount + (sub_bag.amount * get_amount_of_bags(bag_map, sub_bag))
    return amount

# test()

with open(filename, 'r') as file:
    lines = file.read().strip().split("\n")
    bag_map = []
    for rule in lines:
        bag_rules = parse_rule(rule)
        bag_map.append(bag_rules)
    bag_to_find = Bag(1, start_bag, [])
    amount = get_amount_of_bags(bag_map, bag_to_find)
    print(amount)
