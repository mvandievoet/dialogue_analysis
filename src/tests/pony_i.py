import unittest
from hw3.pony_i import pony_i

class pony_iTestCase(unittest.TestCase):

    def test_PonyI(self):

        x = "Twilight Sparkle"
        self.assertEqual(x, pony_i(0))

