from hw3.create_wordlist import create_wordlist
from collections import Counter
import unittest
from hw3.get5words import get5words

class get5TestCase(unittest.TestCase):

    def test_get5(self):
        y = alpha
        x = ['not','nor', 'too','too','here','here','here','be','be','be','be','should','should','should','should','should','should','this','this','this','this','this']
        self.assertEqual(['should','this', 'be', 'here','too'], get5words(x, y))


