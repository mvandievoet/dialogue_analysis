import unittest
from hw3.to2decimal import to2decimal

class to2decimalTestCase(unittest.TestCase):

    def test_to2decimal(self):

        x = 1.23456
        self.assertEqual('1.23', to2decimal(x))

