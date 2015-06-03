import unittest
from fizzbuzz import *
from nose_parameterized import parameterized

class FizzBuzzTests(unittest.TestCase):
    def test_length_of_list_is_100(self):
        fizz_buzz_numbers = get_fizz_buzz_numbers()
        self.assertEqual(len(fizz_buzz_numbers), 100)

    def test_first_item_is_1(self):
        fizz_buzz_numbers = get_fizz_buzz_numbers()
        self.assertEqual(fizz_buzz_numbers[0], 1)

    @parameterized.expand([
    (1, 1),
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    ])
    def test_fizz_response_for_multiple_of_3(self, interger_in, expected_fizz_buzz_response):
        fizz_response = fizz_buzz_calc(interger_in)
        self.assertEqual(fizz_response, expected_fizz_buzz_response)

#    def test_2(self):
#        self.assertEqual(fizz_buzz_calc(4),4)
#        self.assertEqual(fizz_buzz_calc(6), "Fizz")
#        self.assertEqual(fizz_buzz_calc(10), "Buzz")
#        self.assertEqual(fizz_buzz_calc(15), "FizzBuzz")
