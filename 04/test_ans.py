import unittest
from ans import *

class TestIsXMas(unittest.TestCase):
    def test_valid_original_pattern(self):
        # M.S
        # .A.
        # M.S
        pattern = [
            ['M', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'S']
        ]
        self.assertTrue(is_x_mas(pattern))

    def test_valid_horizontal_flip(self):
        # S.M
        # .A.
        # S.M
        pattern = [
            ['S', '.', 'M'],
            ['.', 'A', '.'],
            ['S', '.', 'M']
        ]
        self.assertTrue(is_x_mas(pattern))

    def test_valid_vertical_flip(self):
        # M.S
        # .A.
        # M.S
        pattern = [
            ['M', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'S']
        ]
        self.assertTrue(is_x_mas(pattern))

    def test_valid_both_flips(self):
        # S.S
        # .A.
        # M.M
        pattern = [
            ['S', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'M']
        ]
        self.assertTrue(is_x_mas(pattern))

    def test_invalid_wrong_middle(self):
        # M.S
        # .B.
        # M.S
        pattern = [
            ['M', '.', 'S'],
            ['.', 'B', '.'],
            ['M', '.', 'S']
        ]
        self.assertFalse(is_x_mas(pattern))

    def test_invalid_wrong_corners(self):
        # X.S
        # .A.
        # M.Y
        pattern = [
            ['X', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'Y']
        ]
        self.assertFalse(is_x_mas(pattern))

    def test_case_insensitive(self):
        # m.s
        # .a.
        # m.s
        pattern = [
            ['m', '.', 's'],
            ['.', 'a', '.'],
            ['m', '.', 's']
        ]
        self.assertTrue(is_x_mas(pattern))

    def test_solve(self):
        # Arrange
        input_data = read_input(str(Path(__file__).parent / 'input.txt'))
        
        # Act
        result = solve(input_data)
        
        # Assert
        assert result == (2554, 1916), f"Expected (2554, 1916) but got {result}"
        
if __name__ == '__main__':
    unittest.main() 