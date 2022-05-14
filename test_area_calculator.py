import unittest
from formulas import *

class MyTestCase(unittest.TestCase):
    def test_circle(self):
        self.assertEqual(Formulas.circle(10), 314.1592653589793)

        self.assertEqual(Formulas.circle(-10), 'Values for area cannot be negative')
        self.assertEqual(Formulas.circle('str'), "could not convert string to float: 'str'")

    def text_rectangle(self):
        self.assertEqual(Formulas.rectangle(5, 2), 10)

        self.assertEqual(Formulas.rectangle(-10, 2), 'Values for area cannot be negative')
        self.assertEqual(Formulas.rectangle(10,-2), 'Values for area cannot be negative')
        self.assertEqual(Formulas.rectangle(-10, -2), 'Values for area cannot be negative')
        self.assertEqual(Formulas.rectangle('str', 2), "could not convert string to float: 'str'")

    def text_square(self):
        self.assertEqual(Formulas.square(5), 25)

        self.assertEqual(Formulas.square(-10), 'Values for area cannot be negative')
        self.assertEqual(Formulas.square('str'), "could not convert string to float: 'str'")

    def text_triangle(self):
        self.assertEqual(Formulas.triangle(5, 2), 5)

        self.assertEqual(Formulas.triangle(-10, 2), 'Values for area cannot be negative')
        self.assertEqual(Formulas.triangle(10, -2), 'Values for area cannot be negative')
        self.assertEqual(Formulas.triangle(-10, -2), 'Values for area cannot be negative')
        self.assertEqual(Formulas.triangle('str', 2), "could not convert string to float: 'str'")

if __name__ == '__main__':
    unittest.main()
