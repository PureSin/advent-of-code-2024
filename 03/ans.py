import re
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input

def solve(data):
    """Solution method"""
    print("data length {}".format(len(data)))
    
    # Find all matches of mul(x,y) pattern
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = []
    for line in data:
        found = re.finditer(pattern, line)
        for match in found:
            matches.append((match.start(), match.group()))
    print(f"Found {len(matches)} matches: {matches}")
    # Extract numbers from each match and multiply them
    total = 0
    for match in matches:
        # Extract numbers using regex, stripping 'mul(' and ')'
        nums = re.findall(r'\d+', match)
        x, y = int(nums[0]), int(nums[1])
        print(f"Multiplying {x} * {y}")
        total += x * y
        
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    # Find start indices for `do()`
    do_matches = [(match.start(), match.group()) for match in re.finditer(do_pattern, line)]

    # Find start indices for `don't()`
    dont_matches = [(match.start(), match.group()) for match in re.finditer(dont_pattern, line)]

    # Print results
    print("Matches for 'do()':", do_matches)
    print("Matches for 'don't()':", dont_matches)
    return total

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()