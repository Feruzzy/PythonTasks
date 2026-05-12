import unittest
from practice import (
    range_numbers
)

class TestPyBank(unittest.TestCase):

    def test_that_range_function_exist(self):
        practice.range_numbers("2, 5, 7, 9, 20")

    def test_that_largest_number_is_20(self):
        # Given
        number = 9
       
        # When
        actual = range_numbers(numbers)
       
        # Check
        expected = 18  # (20 - 2)
        self.assertEqual(actual, expected)







