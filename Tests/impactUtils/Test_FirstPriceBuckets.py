import unittest
from taq.MyDirectories import MyDirectories
from taq.TAQTradesReader import TAQTradesReader
from taq.TAQQuotesReader import TAQQuotesReader
from impactUtils.FirstPriceBuckets import FirstPriceBuckets


class Test_FirstPriceBuckets(unittest.TestCase):

    def testConstructor(self):
        startTS = None
        endTS = None
        numBuckets = 2
        fileName = MyDirectories.getTradesDir() + "/20070919/IBM_trades.binRT"
        data = TAQTradesReader(fileName)

        fpb = FirstPriceBuckets(data, numBuckets, startTS, endTS)
        self.assertTrue(fpb.getN() == 2)
        self.assertTrue(fpb.getTimestamp(0) == 34216000 and fpb.getTimestamp(1) == 45900000)
        tolerance = 0.0001
        self.assertAlmostEqual(116.9000015258789,fpb.getPrice(0),tolerance)
        self.assertAlmostEqual(116.43000030517578,fpb.getPrice(1))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
