import unittest
from task1 import remove_specials, contains_char, n_chars_long, begins_with_ab_ends_with_s

class TestTask1(unittest.TestCase):

    def test_remove_specials(self):
        self.assertEqual(remove_specials("Hello, World!"), "Hello World")
        self.assertEqual(remove_specials("Python@3.9"), "Python39")
        self.assertEqual(remove_specials("No_specials_here"), "Nospecialshere")
        self.assertEqual(remove_specials(""), "")

    def test_contains_char(self):
        self.assertTrue(contains_char("Hello", "H"))
        self.assertTrue(contains_char("Bye, world", "o"))
        self.assertFalse(contains_char("Hello", "Z"))
        self.assertFalse(contains_char("Bye, world", "a"))
        self.assertTrue(contains_char("12345", "3"))
        self.assertFalse(contains_char("", "a"))

    def test_n_chars_long(self):
        self.assertTrue(n_chars_long("Hello world", 5))
        self.assertFalse(n_chars_long("Hello world", 6))
        self.assertEqual(n_chars_long("Python programming", 6).group(), "Python")
        self.assertFalse(n_chars_long("Short", 10))

    def test_begins_with_ab_ends_with_s(self):
        self.assertTrue(begins_with_ab_ends_with_s("apples"))
        self.assertTrue(begins_with_ab_ends_with_s("bananas"))
        self.assertFalse(begins_with_ab_ends_with_s("grapes"))
        self.assertFalse(begins_with_ab_ends_with_s("oranges"))
        self.assertTrue(begins_with_ab_ends_with_s("abacus and oranges"))
        self.assertFalse(begins_with_ab_ends_with_s("abaci and grapes"))
        self.assertTrue(begins_with_ab_ends_with_s("abacus. And grapes?"))

if __name__ == '__main__':
    unittest.main()