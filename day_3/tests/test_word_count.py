"""module for testing word count"""
import unittest
from day_3.word_count import words
class TestWordCounts(unittest.TestCase):

    """
        Counts the occurrences or characters in a word
    """

    def test_word_occurance1(self):
        """Tests for word occurence for 1 word"""
        self.assertDictEqual({'word': 1}, words('word'),
                             msg='should count one word')

    def test_word_occurance2(self):
        """Tests for 1 occurance in a sentence"""
        self.assertDictEqual({'one': 1, 'of': 1, 'each': 1}, words("one of each"),
                             msg='should count one of each')

    def test_word_occurance3(self):
        """Tests for multiple occurrence in a repetitive sentence"""
        self.assertDictEqual({'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
                             words("one fish two fish red fish blue fish"),
                             msg='should count multiple occurrences')

    def test_word_occurance4(self):
        """Tests for occurence of punctuation marks"""
        self.assertDictEqual({'car': 1, ":": 2, 'carpet': 1, 'as': 1,
                              'java': 1, 'javascript!!&@$%^&': 1},
                             words('car : carpet as java : javascript!!&@$%^&'),
                             msg='should include punctuation')
