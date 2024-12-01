def read_input(file_path):
    """Read input from file and return data"""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def return_lists(data):
    list1 = []
    list2 = []
    for l in data:
        nums = list(map(int, l.split()))
        list1.append(nums[0])
        list2.append(nums[1]) 
    return list1, list2
def solve(data):
    """Solution method"""
    # data is a list of 2 numbers per line
    list1, list2 = return_lists(data)
    # sort them for pairing
    list1.sort()
    list2.sort()
    # calculate the diff after pairing
    sum = 0
    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])
    # return the sum
    return sum

def main():
    # Read input
    input_data = read_input('01/input.txt')
    
    # Solve the problem
    answer = solve(input_data)
    
    # Print result
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
