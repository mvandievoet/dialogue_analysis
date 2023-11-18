
import pandas as pd
import unittest
from hw3.dialog_by_non_pony import dialog_by_non_pony

class DialofTestCase(unittest.TestCase):

    def test_dialog(self):
        d = {'pony': ['Fluttershy','you','Everypony'], 'dialog': ["hi this is me", "but not me", "nor me"]}
        df = pd.DataFrame(data=d)
        d1 = {'pony': ['you'], 'dialog': ["but not me"]}
        df1 = pd.DataFrame(data=d1)
        values = dialog_by_non_pony(df)
        boo = True
        if (values.iloc[0,0] != df1.iloc[0,0] or values.iloc[0,1] != df1.iloc[0,1]):
            boo = False
        self.assertEqual(boo, True)
