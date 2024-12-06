import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input

def parse_input(data):
    # rules are until there is an empty line
    rules = []
    while data:
        line = data.pop(0) 
        if line.strip() == "":
            break
        if "|" in line:
            left, right = line.strip().split("|")
            rules.append((int(left), int(right)))
    # parse the rest of the updates, they're commen seperated values of int
    updates = []
    for line in data:
        if line.strip() == "":
            continue
        if line.strip():
            update = [int(x) for x in line.strip().split(",")]
            updates.append(update)
    return rules, updates

def is_correct(update, rules):
    print("checking update: ", update)
    correct = True
    for rule in rules:
        left, right = rule
        if left not in update or right not in update:
            continue
        left_idx = update.index(left)
        right_idx = update.index(right)
        if left_idx >= right_idx:
            correct = False
            # flip the 2 values
            # Swap the values at left_idx and right_idx
            update[left_idx], update[right_idx] = update[right_idx], update[left_idx]
            # try again with this
            _, update = is_correct(update, rules)
    return correct, update 

def solve(data):
    """Solution method"""
    # parse the rules
    # parse the updates 
    rules, updates = parse_input(data)
    # filter the correct updates
    correct_updates = []
    fixed_updates = []
    for update in updates:
        correct, fixed = is_correct(update, rules)
        if correct:
            correct_updates.append(update)
        else:
            fixed_updates.append(fixed)
    # sum up the middle numbers
    p1_result = sum(update[len(update)//2] for update in correct_updates)
    print("Fixed updates:")
    for update in fixed_updates:
        print(update)
    p2_result = sum(update[len(update)//2] for update in fixed_updates)
    return p1_result, p2_result

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()