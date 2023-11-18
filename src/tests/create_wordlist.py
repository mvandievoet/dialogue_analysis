import unittest
from hw3.create_wordlist import create_wordlist

class wordlistTestCase(unittest.TestCase):

    def test_wordlist(self):

        x = "this, is a Sentence! of words1"
        y = ['this','is','a','sentence','of','words']
        self.assertEqual(y, create_wordlist(x))

