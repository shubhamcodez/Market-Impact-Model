import unittest
from taq.MyDirectories import *
from taq.TAQTradesReader import TAQTradesReader
from impactUtils.ReturnBuckets import ReturnBuckets

# Test ReturnBuckets class used to compute
# returns of some length of time, e.g. 2 minutes
# or 15 minutes
class Test_ReturnBuckets(unittest.TestCase):

    def testName(self):
        startTS = 18 * 60 * 60 * 1000 / 2  # 930AM
        endTS = 16 * 60 * 60 * 1000  # 4PM
        numBuckets = 2
        fileName = MyDirectories.getTradesDir() + '/20070919/IBM_trades.binRT'
        data = TAQTradesReader( fileName )
        returnBuckets = ReturnBuckets(data, startTS, endTS, numBuckets)
        self.assertTrue(returnBuckets.getN() == 2)
        self.assertAlmostEqual(
            [-0.0035073024530167807, 0.001459211750603595],
            [returnBuckets.getReturn(0), returnBuckets.getReturn(1)]
        )


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
