"""Module for prime number generator tests"""
import unittest
from day_1.primesieve import primesieve


class PrimeGenerator(unittest.TestCase):
    """Contains tests for the sieve of eratosthenes for generating prime numbers"""

    def test_empty_list_for_1(self):
        """Test if it returns an empty list when given input 1"""
        self.assertEqual(primesieve(1), [])
    def test_empty_list_for_0(self):
        """Test if it returns an empty list with 0 as input"""
        self.assertEqual(primesieve(0), [])
    def test_for_str_type_error(self):
        """Test for TypeError for string input"""
        self.assertEqual(primesieve('random str'), 'TypeError')
    def test_for_negative_value_error(self):
        """Test for ValueError for negative number input"""
        self.assertEqual(primesieve(-100), 'ValueError')
    def test_correct_values(self):
        """Test for correct values"""
        self.assertEqual(primesieve(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


if __name__ == '__main__':
    unittest.main()
