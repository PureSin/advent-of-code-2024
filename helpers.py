def read_input(file_path):
    """Read input from file and return data"""
    with open(file_path, 'r') as file:
        return file.read().splitlines() 