import unittest 
from ans import *

class TestAns(unittest.TestCase):
    def test_solve(self):
        """Test the solve function"""
        test_data = read_input(str(Path(__file__).parent / 'sample.txt'))
        expected_result = 11387
        self.assertEqual(solve(test_data), expected_result)
        
    def test_checksum(self):
        checksum = compute_checksum(list("0099811188827773336446555566.............."))
        self.assertEqual(checksum, 1928)

if __name__ == "__main__":
    unittest.main()