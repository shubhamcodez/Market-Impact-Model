import os
import numpy as np
import math
from taq.TAQQuotesReader import TAQQuotesReader
from taq.TAQTradesReader import TAQTradesReader
from impactUtils.VWAP import VWAP
from impactUtils.TickTest import TickTest

def getImbalance(trades, startTS, endTS):
    tickTest = TickTest()
    classifications = tickTest.classifyAll(trades, startTS, endTS)
    imbalanced_volume = 0
    for i in range(0, len(classifications)):
        imbalanced_volume += classifications[i][2] * trades.getSize(i)

    imbalance = VWAP(trades, startTS, endTS).getVWAP()*imbalanced_volume
    return imbalance