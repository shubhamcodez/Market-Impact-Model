import os
import numpy as np
import math
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Shubham/ATQSHW1/'))
sys.path.append(parent_dir)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

#from taq.TAQQuotesReader import TAQQuotesReader
from impactUtils.ReturnBuckets import ReturnBuckets

def getMidQuoteReturns(quotes,startTS, endTS, numBuckets):
    quoteOneDayReturns = []
    #numBuckets = int(math.ceil((endTS - startTS) / (120000)))
    returnBuckets = ReturnBuckets(quotes, startTS, endTS, numBuckets)
    
    for i in range(0, numBuckets):
        return_val = returnBuckets.getReturn(i)
        if return_val is None:
            return_val = 0
        quoteOneDayReturns.append(return_val)

    return np.array(quoteOneDayReturns)