import re

filename = "/home/xmbomb/dev/aoc2020/day4/input.txt"

def is_valid(record):
    is_valid = True
    try:
        for field in fields:
            if not record[field]:
                is_valid = False
    except:
        is_valid = False
    return is_valid

fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"]
optional_fields = ["cid"]

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