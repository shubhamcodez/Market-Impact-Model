import os
import sys
import unittest

from taq import MyDirectories
from taq.TAQQuotesReader import TAQQuotesReader
from taq.TAQTradesReader import TAQTradesReader

print("Success")
class Test_TAQQuotesReader(unittest.TestCase):

    def test1(self):

        reader = TAQQuotesReader( MyDirectories.getQuotesDir() + '/20070822/AAI_quotes.binRQ' )
        #reader = TAQQuotesReader("C:/Shubham/ATQSHW1/quotes/20070822/AAI_quotes.binRQ")
        zz = list([
            reader.getN(),
            reader.getSecsFromEpocToMidn(),
            reader.getMillisFromMidn( 0 ),
            reader.getAskSize( 0 ),
            reader.getAskPrice( 0 ),
            reader.getBidSize( 0 ),
            reader.getBidPrice( 0 )
        ])
        self.assertEqual( '[10476, 1187755200, 34252000, 54, 10.380000114440918, 20, 10.300000190734863]', str( zz ) )


if __name__ == "__main__":
    unittest.main()