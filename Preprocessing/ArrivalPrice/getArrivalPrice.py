import os
import numpy as np
import math
from impactUtils.FirstPriceBuckets import FirstPriceBuckets

def getArrivalPrice(trades, startTS, endTS, numBuckets) :
    arrivalPrice = 0
    for i in range(0, trades.getN()):
        if FirstPriceBuckets(trades, numBuckets, startTS, endTS).getPrice(i) is not None:
            arrivalPrice = FirstPriceBuckets(trades, numBuckets, startTS, endTS).getPrice(i)
            break
    return arrivalPrice 