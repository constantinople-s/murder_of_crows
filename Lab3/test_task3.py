import unittest
from task3 import main

class TestMainFunction(unittest.TestCase):
    
    def test_main_with_comments_and_blank_lines(self):
        test_input = 'test_input.py'
        with open(test_input, 'w') as file:
            file.write('''# This is a short comment
print("Hello, World!")  # Another comment

"""
This is a long comment
"""

print("Another line")  # Comment at the end of line

''')
        expected_output = 'print("Hello, World!")\nprint("Another line")'
        self.assertEqual(main(test_input), expected_output)

    def test_main_with_no_comments_or_blank_lines(self):
        test_input = 'test_input_no_comments.py'
        with open(test_input, 'w') as file:
            file.write('print("Hello, World!")\nprint("Another line")\n')
        expected_output = 'print("Hello, World!")\nprint("Another line")'
        self.assertEqual(main(test_input), expected_output)

    def test_main_with_only_comments_and_blank_lines(self):
        test_input = 'test_input_only_comments.py'
        with open(test_input, 'w') as file:
            file.write('''# This is a short comment

"""
This is a long comment
"""

# Another comment

''')
        expected_output = ''
        self.assertEqual(main(test_input), expected_output)

if __name__ == '__main__':
    unittest.main()