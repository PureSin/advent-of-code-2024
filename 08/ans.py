import sys
import itertools
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input

def parse_input(data):
    grid = []
    frequency = {}
    y = 0
    for line in data:
        l = list(line)
        grid.append(l)
        # find unique symbols
        symbols = set(l)
        for s in symbols:
            if s == ".":
                continue
            # all the indicies
            x_indicies = [i for i, x in enumerate(l) if x == s] 
            if s in frequency:
                frequency[s] += [(x,y) for x in x_indicies]
            else:
                frequency[s] = [(x,y) for x in x_indicies]
        y += 1
    return grid, frequency 

def is_valid_antinode(x, y, grid):
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] != "#":
        grid[y][x] = "#"
        return 1
    return 0

def is_valid(combo, grid):
    x1, y1 = combo[0]
    x2, y2 = combo[1]
    dx = x2 - x1
    dy = y2 - y1
    a1x = x1 + 2*dx
    a1y = y1 + 2*dy
    a2x = x1 - dx
    a2y = y1 - dy
    print("Antinodes: {} and {}".format((a1x, a1y), (a2x, a2y)))
    return is_valid_antinode(a1x, a1y, grid) + is_valid_antinode(a2x, a2y, grid) 

def find_antinodes(grid, frequency):
    # do it symbol by symbol
    count = 0 
    for symbol in frequency:
        print("Checking symbol: {}".format(symbol))
        positions = frequency[symbol]
        # generate all the combinations
        combos = itertools.combinations(positions, 2)
        for c in combos:
            print("Checking combo: {}".format(c))
            # find their distance and then the 2 positions that are candidates
            # check if valid and mark as needed
            count += is_valid(c, grid)
    return count, grid

def solve(data):
    """Solution method"""
    # read line by line and parse into array
    # frequency is a dict of symbol to a list of tuples for locations
    grid, frequency = parse_input(data)
    for s in frequency:
        print("Symbol: {}, positions: {}".format(s, frequency.get(s)))
    # for each symbol, try all combinations and find antinodes 
    cnt, antinodes = find_antinodes(grid, frequency)
    for l in antinodes:
        print(l)
    return cnt

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()