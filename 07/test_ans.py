import pytest
from ans import *

def test_solve():
    """Test the solve function"""
    test_data = read_input(str(Path(__file__).parent / 'sample.txt'))
    expected_result = 11387
    assert solve(test_data) == expected_result, f"Expected {expected_result}, but got {solve(test_data)}" 