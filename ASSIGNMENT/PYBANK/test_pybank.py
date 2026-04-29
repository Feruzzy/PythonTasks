import unittest
from pybank import (
    validate_email, calculate_balance, is_strong_password,
    apply_interest, get_transaction_summary
)

class TestPyBank(unittest.TestCase):

    def test_email_validation(self):
        self.assertTrue(validate_email("test@bank.com"))
        self.assertFalse(validate_email("a@b.com")) 
        self.assertFalse(validate_email("@email.com")) 

    def test_calculate_balance(self):
        self.assertEqual(calculate_balance([100, -50, 20]), 70)
        self.assertEqual(calculate_balance([]), 0)

    def test_password_strength(self):
        self.assertTrue(is_strong_password("password123"))
        self.assertFalse(is_strong_password("1234567"))

    def test_apply_interest(self):
        self.assertEqual(apply_interest(1000, 0.05, 2), 1102.50)
        with self.assertRaises(ValueError):
            apply_interest(1000, -0.1, 5)

    def test_transaction_summary(self):
        sample_input = [["credit", 2000], ["debit", 500], ["credit", 300]]
        expected = [
            ["total_credits", 2300],
            ["total_debits", 500],
            ["net_balance", 1800],
            ["transaction_count", 3]
        ]
        self.assertEqual(get_transaction_summary(sample_input), expected)

if __name__ == "__main__":
    unittest.main()
