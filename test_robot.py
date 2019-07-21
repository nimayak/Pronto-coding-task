import unittest
from robot import move_robot
from robot import calculate_distance

class MyTest(unittest.TestCase):
    def test_move_robot(self):
        self.assertEqual(move_robot(['F1', 'R1', 'B2', 'L1', 'B3']), (0,0,0,-4))
    def test_calculate_distance(self):
        self.assertEqual(calculate_distance(0,0,0,-4), "4.0")

if __name__ == "__main__":
    unittest.main()