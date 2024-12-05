import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from helpers import read_input

def candidate_generator(data):
    """Generate all possible 4-character subarrays from 2D input array"""
    # Check each row
    for row in data:
        for i in range(len(row)-3):
            yield row[i:i+4].lower()
    
    # Check each column
    for col in range(len(data[0])):
        for row in range(len(data)-3):
            yield ''.join(data[row+j][col] for j in range(4)).lower()
            
    # Check diagonals down-right
    for row in range(len(data)-3):
        for col in range(len(data[0])-3):
            yield ''.join(data[row+j][col+j] for j in range(4)).lower()
            
    # Check diagonals down-left
    for row in range(len(data)-3):
        for col in range(3, len(data[0])):
            yield ''.join(data[row+j][col-j] for j in range(4)).lower()
            
def candidate_generator_2(data):
    """Generate all possible 3x3 subarrays from 2D input array"""
    for row in range(len(data)-2):
        for col in range(len(data[0])-2):
            # Extract 3x3 slice
            slice_3x3 = [
                data[row+i][col:col+3] for i in range(3)
            ]
            yield slice_3x3, row, col
            
def is_x_mas(canditate):
    """
    M.S
    .A.
    M.S
    """
    # Check if candidate matches X-MAS pattern
    # Get the characters at key positions
    top_left = canditate[0][0].lower()
    top_right = canditate[0][2].lower()
    middle = canditate[1][1].lower()
    bottom_left = canditate[2][0].lower()
    bottom_right = canditate[2][2].lower()

    # Check if middle is 'a'
    if middle != 'a':
        return False

    # Check all 4 possible orientations:
    # Original: M.S/.A./M.S
    if ((top_left == 'm' and top_right == 's' and 
         bottom_left == 'm' and bottom_right == 's')):
        return True
    
    # Flipped horizontally: S.M/.A./S.M
    if ((top_right == 'm' and top_left == 's' and
         bottom_right == 'm' and bottom_left == 's')):
        return True
        
    # Flipped vertically: M.M/.A./S.S
    if ((bottom_left == 's' and bottom_right == 's' and
         top_left == 'm' and top_right == 'm')):
        return True
        
    # Flipped both: S.S/.A./M.M  
    if ((bottom_right == 'm' and bottom_left == 'm' and
         top_right == 's' and top_left == 's')):
        return True

    return False
    
def solve(data):
    """Solution method"""
    # given input 2D array, create a generator that returns every possible subarray of 4 chars since we're looking for XMAS
    count = 0
    for c in candidate_generator(data):
        if c == "xmas" or c == "samx":
            count += 1
    
    p2_count = 0     
    # Create a 2D array of dots with same dimensions as data
    mask = [["." for _ in range(len(data[0]))] for _ in range(len(data))]
    for c in candidate_generator_2(data):
        candidate, row, col = c
        for l in candidate:
            print(l)
        if is_x_mas(candidate):
            # Fill mask with candidate pattern at row,col
            for i in range(3):
                for j in range(3):
                    if candidate[i][j] in ['M', 'A', 'S']:
                        mask[row+i][col+j] = candidate[i][j]
            print("Yes")
            p2_count += 1
        print("No")
    # Print mask line by line
    print("\nFinal mask:")
    for line in mask:
        print(''.join(line))
    return count, p2_count

def main():
    # Read input
    input_data = read_input(str(Path(__file__).parent / 'input.txt'))
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()