
import pandas as pd
import unittest
from hw3.equals_either import equals_either

class equals_eitherTestCase(unittest.TestCase):

    def test_equalsEither(self):
        d = {'pony': ['Twilight Sparkle','you','Everypony'], 'dialog': ["hi this is me", "but not me", "nor me"]}
        df = pd.DataFrame(data=d)
        d1 = {'pony': ['Twilight Sparkle', 'Everypony'], 'dialog': ['hi this is me', 'nor me']}
        df1 = pd.DataFrame(data=d1)
        values = equals_either(df, "Twilight Sparkle", "Everypony")
        boo = True
        if (values.iloc[0,0] != df1.iloc[0,0] or values.iloc[0,1] != df1.iloc[0,1]):
            boo = False
        self.assertEqual(boo, True)
