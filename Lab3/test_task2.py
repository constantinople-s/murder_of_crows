import unittest
from task2 import retrieve_monetary_values

class TestRetrieveMonetaryValues(unittest.TestCase):

    def test_single_value(self):
        self.assertEqual(retrieve_monetary_values("$10"), 10.0)

    def test_multiple_values(self):
        self.assertEqual(retrieve_monetary_values("$10 $20 $30"), 60.0)

    def test_values_with_cents(self):
        self.assertEqual(retrieve_monetary_values("$10.50 $20.75"), 31.25)

    def test_no_values(self):
        self.assertEqual(retrieve_monetary_values("No money here!"), 0.0)

    def test_mixed_text(self):
        self.assertEqual(retrieve_monetary_values("I have $5 and $10.50 in my wallet."), 15.5)

    def test_invalid_values(self):
        self.assertEqual(retrieve_monetary_values("$10.123 $20.1a $30"), 60.0)

if __name__ == '__main__':
    unittest.main()