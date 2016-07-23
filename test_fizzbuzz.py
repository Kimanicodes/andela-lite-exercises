import unittest
from fizzbuzz import fizz_buzz


class FizzBuzzTest(unittest.TestCase):
    def test_multiples_of_15(self):
        self.assertEqual(fizz_buzz(30), 'FizzBuzz')

    def test_multiples_of_3(self):
        self.assertEqual(fizz_buzz(9), 'Fizz')

    def test_multiples_of_5(self):
        self.assertEqual(fizz_buzz(100), 'Buzz')

    def test_multiples_of_n(self):
        self.assertEqual(fizz_buzz(17), 17)


if __name__ == '__main__':
    unittest.main()
