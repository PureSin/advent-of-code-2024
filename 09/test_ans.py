import unittest 
from ans import *

class TestAns(unittest.TestCase):
    def test_solve(self):
        """Test the solve function"""
        test_data = read_input(str(Path(__file__).parent / 'sample.txt'))
        expected_result = 1928
        self.assertEqual(solve(test_data), expected_result)
        
    def test_checksum(self):
        checksum = compute_checksum(list("0099811188827773336446555566.............."))
        self.assertEqual(checksum, 1928)
    
    def test_get_disk_mask(self):
        line = "12345"
        self.assertEqual(get_disk_mask(line), [0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2])
        
    def test_compact_disk_map(self):
        res = get_compact_disk_map([0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]) 
        self.assertEqual(res, [0, 2, 2, 1, 1, 1, 2, 2, 2, '.', '.', '.', '.', '.', '.'])

if __name__ == "__main__":
    unittest.main()