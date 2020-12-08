
filename = "/home/xmbomb/dev/aoc2020/day8/input.txt"

example_instructions = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def part1(lines):
    def run(i, acc, already_ran):
        line = lines[i]

        if i in already_ran:
            print(f'Infinite loop, acc is {acc}')
            exit(0)
        else:
            already_ran.append(i)

        (instruction, value) = tuple(line.split(" "))
        value = int(value)
        if(instruction == "acc"):
            run(i + 1, acc + value, already_ran)
        elif(instruction == "jmp"):
            run(i + value, acc, already_ran)
        elif(instruction == "nop"):
            run(i + 1, acc, already_ran)
        
        print(f'Code is done, acc is {acc}')
    run(0,0,[])

# part1(lines=example_instructions.strip().split('\n'))

with open(filename, 'r') as file:
    lines = file.read().strip().split('\n')
    part1(lines)

    # lines = example_instructions.strip().split('\n')
