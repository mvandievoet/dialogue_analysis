import unittest
from hw3.len_nested import len_nested

class len_nestedTestCase(unittest.TestCase):

    def test_lenNested(self):

        x = [[1,2,3],[1,2]]
        self.assertEqual(5, len_nested(x))

