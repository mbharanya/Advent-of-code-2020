import re

filename = "/home/xmbomb/dev/aoc2020/day4/input.txt"

def is_valid(record):
    is_valid = True
    try:
        for (field_name, fun) in fields.items():
            if not record[field_name]:
                is_valid = False
            elif not fun(record[field_name]):
                is_valid = False
    except:
        is_valid = False
    return is_valid

def is_valid_height(value):
    int_value = value[:-2]
    if value.endswith("cm"):
        return int(int_value) >= 150 and int(int_value) <= 193
    else:
        return int(int_value) >= 59 and int(int_value) <= 76
    
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

fields = {
    "byr": lambda x: (int(x) >= 1920 and int(x) <= 2002),
    "iyr": lambda x: (int(x) >= 2010 and int(x) <= 2020),
    "eyr": lambda x: (int(x) >= 2020 and int(x) <= 2030),
    "hgt": lambda x: is_valid_height(x),
    "hcl": lambda x: re.match("^#[0-9a-f]{6}", x),
    "ecl": lambda x: re.match("amb|blu|brn|gry|grn|hzl|oth", x),
    "pid": lambda x: re.match("^[0-9]{9}$", x)
}

with open(filename, 'r') as file:
    records = file.read().strip().split('\n\n')
    dicts = []
    for record in records:
        record = record.replace("\n", " ")

        record_dict = {}

        for kv in record.split(' '):
            (k,v) = tuple(kv.split(':'))
            record_dict[k] = v 
        dicts.append(record_dict)

    count = len(list(filter(lambda dict: is_valid(dict), dicts)))
    print(count)