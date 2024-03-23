import os
import numpy as np
import math
from impactUtils.LastPriceBuckets import LastPriceBuckets

def getTerminalPrice(trades, startTS, endTS, numBuckets):
    return LastPriceBuckets(trades, numBuckets, startTS, endTS).getPrice(-1)