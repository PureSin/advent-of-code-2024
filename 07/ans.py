import sys
import itertools
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input

def parse_line(line):
    target, rest = line.split(":")
    target = int(target)
    values = [int(i) for i in rest.split()]
    return target, values 

def is_valid(target, values):
    # try different combos but do it from left to right
    operators = ["+", "*"]
    combos = [list(p) for p in itertools.product(operators, repeat=len(values) - 1)]
     
    # try them out 
    for c in combos:
        total = values[0]
        for i in range(1, len(values)) :
            total = eval("{} {} {}".format(total, c[i-1], values[i]))
        if total == target:
            print("Find valid combo {}, for {}, target: {}", c, values, target)
            return True
    return False 

def is_valid_2(target, values):
    # try different combos but do it from left to right
    operators = ["+", "*", "||"]
    combos = [list(p) for p in itertools.product(operators, repeat=len(values) - 1)]
     
    # try them out 
    for c in combos:
        i = 0
        total = values[i]
        i+=1
        while i < len(values):
            v = values[i]
            i+=1
            op = c.pop(0) 
            if op == "||":
                total = int("{}{}".format(total, v))
            else:
                total = eval("{} {} {}".format(total, op, v))
        if total == target:
            print("Find valid combo {}, for {}, target: {}", c, values, target)
            return True
    return False 


def solve(data):
    """Solution method"""
    valid_sum = 0
    for line in data:
        target, values = parse_line(line)
        print("Eval {}, with values: {}.".format(target, values))
        if is_valid_2(target, values):
            valid_sum += target
    return valid_sum

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()