import unittest
import numpy as np
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Shubham/ATQSHW1/'))
sys.path.append(parent_dir)

from unittest.mock import MagicMock
from taq.TAQTradesReader import TAQTradesReader
from taq.MyDirectories import MyDirectories
from Preprocessing.DailyValue import getDailyValue
from impactUtils.ReturnBuckets import ReturnBuckets

class TestgetDailyValue(unittest.TestCase):
    def testConstructor(self):
        fileName = MyDirectories.getTradesDir() + "/20070919/IBM_trades.binRT"
        data = TAQTradesReader(fileName)

        tdv = np.round(getDailyValue(data)/(10**9),4)
        expected_tdv = np.round(1.043658,4)
        np.testing.assert_array_equal(tdv, expected_tdv)


if __name__ == '__main__':
    unittest.main() 
