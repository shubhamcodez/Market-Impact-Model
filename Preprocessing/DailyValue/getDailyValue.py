import os
import numpy as np
import math

from taq.TAQTradesReader import TAQTradesReader
def getDailyValue(trades):
    total_daily_value = 0
    for i in range(0, trades.getN()):
        total_daily_value += trades.getSize(i)*trades.getPrice(i)
    
    return total_daily_value