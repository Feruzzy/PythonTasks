import unittest
from back_to_sender import daily_wage  # Assuming your function is in back_to_sender.py

class TestBackToSender(unittest.TestCase):

    def test_that_daily_wage_is_calculated_correctly_for_less_than_50(self):
        # Given
        number = 25
       
        # When
        actual = daily_wage(number)
       
        # Check
        expected = 9000  # (25 * 160) + 5000
        self.assertEqual(actual, expected)

    def test_that_daily_wage_is_calculated_correctly_for_50_to_59(self):
        # Given
        number = 55
       
        # When
        actual = daily_wage(number)
       
        # Check
        expected = 16000  # (55 * 200) + 5000
        self.assertEqual(actual, expected)

    def test_that_daily_wage_is_calculated_correctly_for_60_to_69(self):
        # Given
        number = 65
       
        # When
        actual = daily_wage(number)
       
        # Check
        expected = 21250  # (65 * 250) + 5000
        self.assertEqual(actual, expected)

    def test_that_daily_wage_is_calculated_correctly_for_70_and_above(self):
        # Given
        number = 80
       
        # When
        actual = daily_wage(number)
       
        # Check
        expected = 45000  # (80 * 500) + 5000
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
