import unittest
import Check

class TestCheck(unittest.TestCase):

    def test_IsNumber_Returns_True_When_Valid_Number_Is_Passed_In(self):
       result = Check.IsNumber(5)
       self.assertEqual(result,True)

    def test_IsNumber_Returns_False_When_Invalid_Number_Is_Passed_In(self):
       result = Check.IsNumber('abc')
       self.assertEqual(result,False)