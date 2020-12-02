import re

filename = "input.txt"

def split(word): 
    return [char for char in word]  

with open(filename) as f:
    lines = f.readlines()
    regex = "([0-9]+)-([0-9]+)\s([a-zA-Z]): (.*)"

    valid_pws = 0

    for line in lines:
        (from_no, to_no, letter, string) = re.findall(regex, line)[0]
        letter_count = split(string).count(letter)
        if letter_count >= int(from_no) and letter_count <= int(to_no):
            valid_pws += 1
    print(valid_pws)
