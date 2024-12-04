import re
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input

def solve(data):
    """Solution method"""
    print("data length {}".format(len(data)))
    
    # Find all matches of mul(x,y) pattern
    combined_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    # Find matches and their start indices
    part1_total = 0
    part2_total = 0 
    can_mut = True
    # flatten into 1 line
    data = ''.join(data)
    matches = [(match.start(), match.group()) for match in re.finditer(combined_pattern, data)]

    print(f"Found {len(matches)} matches: {matches}")
    # Extract numbers from each match and multiply them
    for match in matches:
        match_str = match[1]  # Get the matched string
        if match_str.startswith('mul'):
            # Extract numbers using regex, stripping 'mul(' and ')'
            nums = re.findall(r'\d+', match_str)
            x, y = int(nums[0]), int(nums[1])
            print(f"Multiplying {x} * {y}")
            part1_total += x * y
            if can_mut == True:
                part2_total += x * y
        elif match_str.startswith("don't"):
            print("disable mut")
            can_mut = False
        elif match_str.startswith('do'):
            print("enable mut")
            can_mut = True
    
    return part1_total, part2_total 

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
