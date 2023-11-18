
import unittest
from hw3.set_data import set_data

class set_dataTestCase(unittest.TestCase):

    def test_setData(self):
        list1 = ['hi','hello']
        data = [1,2]
        dic1 = {}
        dic2 = {}
        dic2 = set_data(list1, data, dic2)
        dic1['hi']=1
        dic1['hello']=2

        boo = True
        if not (dic2['hi']==1 or dic2['hello']==2):
            boo = False
        self.assertEqual(boo, True)

