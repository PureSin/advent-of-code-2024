import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input

def is_valid(levels: list[int]) -> bool:
    # check levels is monotonic
    # check if list is monotonically increasing
    increasing = all(levels[i] >= levels[i-1] for i in range(1, len(levels)))
    # check if list is monotonically decreasing 
    decreasing = all(levels[i] <= levels[i-1] for i in range(1, len(levels)))
    # return True if either increasing or decreasing
    # print("is increasing {0}, or decreasing {1}".format(increasing, decreasing))
    is_monotonic = increasing or decreasing
    if not is_monotonic:
        return False
    
    # get min and max diff between consecutive numbers
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_valid_2(levels: list[int]) -> bool:
    if is_valid(levels):
        return True
    # try removing every position
    return any(is_valid(levels[:i] + levels[i+1:]) for i in range(len(levels)))

def solve(data):
    """Solution method"""
    # check each report one by one and return how many are safe
    safe_reports = sum(1 for l in data if is_valid(list(map(int, l.split()))))
    safe_reports_2 = sum(1 for l in data if is_valid_2(list(map(int, l.split()))))
    return safe_reports, safe_reports_2

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()