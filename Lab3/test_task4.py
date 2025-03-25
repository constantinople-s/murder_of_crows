import unittest
from task4 import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(change_date_format("2023-10-05"), "05-10-2023")
        self.assertEqual(change_date_format("1999-12-31"), "31-12-1999")
    
    def test_invalid_date(self):
        with self.assertRaises(AttributeError):
            change_date_format("05-10-2023")
        with self.assertRaises(AttributeError):
            change_date_format("2023/10/05")
        with self.assertRaises(AttributeError):
            change_date_format("20231005")

if __name__ == '__main__':
    unittest.main()