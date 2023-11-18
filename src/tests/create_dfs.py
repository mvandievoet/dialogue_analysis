
import pandas as pd
import unittest
from hw3.create_dfs import create_dfs

class CreateDfsTestCase(unittest.TestCase):

    def test_create2(self):
        
        d = {'pony': ['me','you','me'], 'dialog': ["hi this is me", "but not me", "nor me"]}
        df = pd.DataFrame(data=d)
        arr1 = ['me', 'not', 'nor']
        arr2 = [1,2,3]
        values = create_dfs(arr1, arr2, df)
        results = []
        a = pd.DataFrame({'pony': ['me','you','me'], 'dialog': ["hi this is me", "but not me", "nor me"]})
        b = pd.DataFrame({'pony': ['you'], 'dialog': ["but not me"]})
        c = pd.DataFrame({'pony': ['me'], 'dialog': ["nor me"]})
        results.append(a)
        results.append(b)
        results.append(c)
        bo = True
        for i in [0,1,2]:
            for x in range(len(values[i])):
                for y in range(len(values[i].columns)):
                    if not values[i].iloc[x,y]==results[i].iloc[x,y]:
                        bo = False
   
        self.assertEqual(bo, True)
