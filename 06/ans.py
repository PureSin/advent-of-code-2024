import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input
import copy

def move(x_pos, y_pos, cur_dir):
    if cur_dir == "<":
        return x_pos - 1, y_pos
    elif cur_dir == ">":
        return x_pos + 1, y_pos
    elif cur_dir == "^":
        return x_pos, y_pos - 1 
    elif cur_dir == "v":
        return x_pos, y_pos + 1 
    return (x_pos, y_pos)

def find_start_pos(data):
    # return x,y in data that is not "." or "#"
    print("{}x{}", len(data), len(data[0]))
    for y in range(len(data)):
        for x in range(len(data[0])):
            e = data[y][x]
            if e != "." and e != "#":
                return x,y,e
            
def is_on_grid(x_pos, y_pos, data):
   return x_pos >= 0 and x_pos < len(data) and y_pos >=0 and y_pos < len(data[0]) 

def solve(data):
    """Solution method"""
    # data is s 2x2 grid with # marking obstacles and one of <, ^, >, and down carrot for guard's start pos and direction
    # guard turns right when encountering an obstacle. mark, all visited spots with X and return the marked grid 
    data = [list(row) for row in data]
    res = copy.deepcopy(data)
    x_pos, y_pos, cur_dir = find_start_pos(data)
    print(f"x: {x_pos}, y: {y_pos}, direction: {cur_dir}")
    while is_on_grid(x_pos, y_pos, data):
        # mark the grid
        res[y_pos][x_pos] = 'X'
        # check for collisions
        next_x_pos, next_y_pos = move(x_pos, y_pos, cur_dir)
        if not is_on_grid(next_x_pos, next_y_pos, data):
            break
        if data[next_y_pos][next_x_pos] == "#":
            # turn
            if cur_dir == '>':
                cur_dir = "v"
            elif cur_dir == 'v':
                cur_dir = '<'
            elif cur_dir == "<":
                cur_dir = "^"
            else: #"^"
                cur_dir = ">"
            a, b = move(x_pos, y_pos, cur_dir)
            print("Turning at line {} x {}, new dir {}, new pos: {}x{}".format(x_pos, y_pos, cur_dir, a, b))
            x_pos = a
            y_pos = b
        else:
            y_pos = next_y_pos
            x_pos = next_x_pos
        if not is_on_grid(x_pos, y_pos, data):
            break
        data[y_pos][x_pos] = '.' # TODO need to handle hitting an obstracle here 
    for row in res:
        print(''.join(row))
    x_count = sum([1 for row in res for e in row if e == "X"])
    return x_count

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()