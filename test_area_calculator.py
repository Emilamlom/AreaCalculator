import unittest
from formulas import *

class MyTestCase(unittest.TestCase):
    def test_circle(self):
        self.assertEqual(Formulas.circle(10), 314.1592653589793)

        # I spent several hours trying to get these tests to work, but I couldn't. Tried assertRaises in multiple forms as well.
        self.assertEqual(Formulas.circle(-10), 'Values for area cannot be negative')
        self.assertEqual(Formulas.circle('str'), "could not convert string to float: 'str'")
    def text_rectangle(self):
        self.assertEqual(Formulas.rectangle(5, 2), 10)

    def text_square(self):
        self.assertEqual(Formulas.square(5), 25)

    def text_triangle(self):
        self.assertEqual(Formulas.triangle(5, 2), 5)

if __name__ == '__main__':
    unittest.main()
