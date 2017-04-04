import unittest
from primeSieve import primeSieve


class primeGenerator(unittest.TestCase):

    ''' Test if it returns an empty list when given input 1'''
    def test_empty_list_for_1(self):
        self.assertEqual(primeSieve(1) , [])
    '''Test if it returns an empty list with 0 as input'''
    def test_empty_list_for_0(self):
        self.assertEqual(primeSieve(0), [])
    '''Test for TypeError for string input'''
    def test_for_str_type_error(self):
        self.assertEqual(primeSieve('random str'), 'TypeError')
    '''Test for ValueError for negative number input'''
    def test_for_negative_value_error(self):
        self.assertEqual(primeSieve(-100), 'ValueError')
    ''' Test for correct values'''
    def test_correct_values(self):
        self.assertEqual(primeSieve(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


if __name__ == '__main__':
    unittest.main()
