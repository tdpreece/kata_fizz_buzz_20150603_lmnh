import unittest
from fizzbuzz import *
from nose_parameterized import parameterized

class FizzBuzzTests(unittest.TestCase):
    def test_length_of_list_is_100(self):
        fizz_buzz_numbers = get_fizz_buzz_numbers()
        self.assertEqual(len(fizz_buzz_numbers), 100)

    @parameterized.expand([
    (0, 1),
    (2, "Fizz"),
    ])
    def test_output_list_values(self, list_index, expected_value):
        fizz_buzz_numbers = get_fizz_buzz_numbers()
        self.assertEqual(fizz_buzz_numbers[list_index], expected_value)

    @parameterized.expand([
    (1, 1),
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
    ])
    def test_fizz_buzz_calculator(self, interger_in, expected_fizz_buzz_response):
        fizz_response = fizz_buzz_calc(interger_in)
        self.assertEqual(fizz_response, expected_fizz_buzz_response)

#    def test_2(self):
#        self.assertEqual(fizz_buzz_calc(4),4)
#        self.assertEqual(fizz_buzz_calc(6), "Fizz")
#        self.assertEqual(fizz_buzz_calc(10), "Buzz")
#        self.assertEqual(fizz_buzz_calc(15), "FizzBuzz")
