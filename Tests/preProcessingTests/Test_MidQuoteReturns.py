import unittest
import numpy as np
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Shubham/ATQSHW1/'))
sys.path.append(parent_dir)

from unittest.mock import MagicMock
from taq.TAQQuotesReader import TAQQuotesReader
from taq.MyDirectories import MyDirectories
from Preprocessing.MidQuoteReturns import getMidQuoteReturns
from impactUtils.ReturnBuckets import ReturnBuckets

class TestGetMidQuoteReturns(unittest.TestCase):
    def testConstructor(self):
        startTS = 18 * 60 * 60 * 1000 // 2
        endTS = startTS + (13 * 60 * 60 * 1000 // 2)
        numBuckets = 4
        fileName = MyDirectories.getQuotesDir() + "/20070919/IBM_quotes.binRQ"
        data = TAQQuotesReader(fileName)

        returns = np.round(getMidQuoteReturns(data, startTS, endTS, numBuckets),4)
        expected_returns = np.round(np.array([-0.005313,  0.003575,  0.001974,  0]),4)
        np.testing.assert_array_equal(returns, expected_returns)


if __name__ == '__main__':
    unittest.main() 


if __name__ == '__main__':
    unittest.main()