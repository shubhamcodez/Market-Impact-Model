import unittest
from impactUtils.VWAP import VWAP
from taq.TAQTradesReader import TAQTradesReader
from taq.MyDirectories import *

# Test VWAP class used to calculate volume
# weighted average price for a given day
# between some start time and end time.
class Test_VWAP(unittest.TestCase):

    def testVWAP(self):
        filePathName = MyDirectories.getTradesDir() + "/20070919/IBM_trades.binRT"
        start930 = 19 * 60 * 60 * 1000 / 2
        end4 = 16 * 60 * 60 * 1000
        vwap = VWAP(TAQTradesReader(filePathName), start930, end4)
        self.assertEqual(
            "There were 36913 trades and a VWAP price of 116.468791",
            "There were %d trades and a VWAP price of %f" % (vwap.getN(), vwap.getVWAP())
        )


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testVWAP']
    unittest.main()
