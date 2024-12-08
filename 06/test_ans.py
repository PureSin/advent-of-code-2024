# test_ans.py
import unittest
from ans import move, find_start_pos, is_on_grid, solve

class TestAns(unittest.TestCase):

    def test_move(self):
        self.assertEqual(move(0, 0, ">"), (1, 0))
        self.assertEqual(move(1, 1, "<"), (0, 1))
        self.assertEqual(move(1, 1, "^"), (1, 0))
        self.assertEqual(move(1, 1, "v"), (1, 2))

    def test_find_start_pos(self):
        data = [
            [".", ".", "#"],
            [".", "^", "."],
            ["#", ".", "#"]
        ]
        self.assertEqual(find_start_pos(data), (1, 1, "^"))

    def test_is_on_grid(self):
        data = [
            [".", ".", "#"],
            [".", "<", "."],
            ["#", ".", "#"]
        ]
        self.assertTrue(is_on_grid(1, 1, data))
        self.assertFalse(is_on_grid(3, 1, data))
        self.assertFalse(is_on_grid(1, -1, data))

    def test_solve(self):
        data = [
            [".", ".", "#"],
            [".", "<", "."],
            ["#", ".", "#"]
        ]
        self.assertEqual(solve(data), 2)

if __name__ == "__main__":
    unittest.main()