import unittest
from app.controller import my_calc

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(my_calc([1, 2, 3]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
