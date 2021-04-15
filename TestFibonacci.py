import unittest
import Fibonacci

class TestFibonacci(unittest.TestCase):

    def test_Print_Returns_The_5th_Term_Value(self):
       result = Fibonacci.Print(5)
       self.assertEqual(result,3)

    def test_Print_Returns_The_8th_Term_Value(self):
       result = Fibonacci.Print(8)
       self.assertEqual(result,13)