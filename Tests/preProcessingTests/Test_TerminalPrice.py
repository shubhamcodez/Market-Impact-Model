import unittest
import numpy as np
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Shubham/ATQSHW1/'))
sys.path.append(parent_dir)

from taq.TAQTradesReader import TAQTradesReader
from taq.MyDirectories import MyDirectories
from Preprocessing.TerminalPrice import getTerminalPrice
from impactUtils.ReturnBuckets import ReturnBuckets

class TestTerminalPrice(unittest.TestCase):
    def testConstructor(self):
        startTS = 18 * 60 * 60 * 1000 // 2
        endTS = startTS + (13 * 60 * 60 * 1000 // 2)
        numBuckets = 4
        fileName = MyDirectories.getTradesDir() + "/20070919/IBM_trades.binRT"
        data = TAQTradesReader(fileName)

        returns = round(getTerminalPrice(data, startTS, endTS, numBuckets),2)
        expected_returns = round(116.73,2)
        np.testing.assert_array_equal(returns, expected_returns)


if __name__ == '__main__':
    unittest.main() 
