import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input

def get_disk_mask(line):
    disk_mask = []
    file_index = 0
    for i, c in enumerate(line):
        c = int(c)
        if i % 2 == 0: # even = file
            disk_mask += [file_index] * c
            file_index += 1
        else: # value is number of free slots
            disk_mask += ["."] * c
    return disk_mask

def get_insert_index(disk_map):
    for i in range(len(disk_map)):
        if disk_map[i] == ".":
            yield i
            
def get_from_index(disk_map):
    for i in range(len(disk_map)-1, 0, -1):
       if disk_map[i] != ".":
           yield i 
           
def get_compact_disk_map(disk_map): 
    try:
        from_index_gen = get_from_index(disk_map)
        to_index_gen = get_insert_index(disk_map)
        from_index = next(from_index_gen)
        to_index = next(to_index_gen)
        while from_index > to_index:
            # swap
            print("Swapping {} {} with {} {}".format(from_index,disk_map[from_index],to_index, disk_map[to_index]))
            disk_map[from_index], disk_map[to_index] = disk_map[to_index], disk_map[from_index]
            to_index = next(to_index_gen)
            from_index = next(from_index_gen)
    except StopIteration:
        print("Done iterating") 
    return disk_map

def compute_checksum(compacted_disk_map):
    checksum = 0
    for i, v in enumerate(compacted_disk_map):
        try:
            v = int(v)
            checksum += i * v
        except ValueError:
            break
    return checksum
        
def solve(data):
    """Solution method"""
    line = data[0]
    # line to diskmap
    disk_map = get_disk_mask(line) # diskmap is an array of char
    # compat file: move from right most to left most open spot
    compacted_disk_map = get_compact_disk_map(disk_map)
    # compute checksum 
    checksum = compute_checksum(compacted_disk_map)
    return checksum

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()