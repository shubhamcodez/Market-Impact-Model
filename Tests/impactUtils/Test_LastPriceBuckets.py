import unittest
from taq.TAQTradesReader import TAQTradesReader
from impactUtils.LastPriceBuckets import LastPriceBuckets

# Classes used to test LastPriceBuckets class
# used to determine the last price in buckets
# of a specified length
class StubTAQTradesReader(TAQTradesReader):
    def __init__(self, filePathName):
        # super( filePathName )
        self._data = [
            [10 * 60 * 60 * 1000, 59.30],
            [15 * 60 * 60 * 1000, 63.00],
            [1 + 15 * 60 * 60 * 1000, 63.52]
        ]

    def getN(self):
        return len(self._data)

    def getTimestamp(self, iRec):
        return self._data[iRec][0]

    def getPrice(self, iRec):
        return self._data[iRec][1]

class Test_LastPriceBuckets(unittest.TestCase):

    def testConstructor(self):
        startTS = None
        endTS = None
        numBuckets = 2
        dataReader = StubTAQTradesReader(None)
        fpb = LastPriceBuckets(dataReader, numBuckets, startTS, endTS)
        self.assertTrue(fpb.getN() == 2)
        self.assertTrue(
            fpb.getTimestamp(0) == (10 * 60 * 60 * 1000) and fpb.getTimestamp(1) == (1 + 15 * 60 * 60 * 1000))
        self.assertAlmostEqual(fpb.getPrice(0), 59.30, delta=0.0001)
        self.assertAlmostEqual(fpb.getPrice(1), 63.52, delta=0.0001)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
