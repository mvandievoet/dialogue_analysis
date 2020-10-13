import unittest
from hw3.ponies_without import ponies_without

class ponies_withoutTestCase(unittest.TestCase):

    def test_poniesWithout(self): 
        self.assertEqual( "Applejack|Rarity|Pinkie|Pie|Rainbow|Dash|Fluttershy", ponies_without("Twilight Sparkle"))

