import os
import numpy as np
import math
from taq.TAQQuotesReader import TAQQuotesReader
from taq.TAQTradesReader import TAQTradesReader
from impactUtils.VWAP import VWAP
from Preprocessing.ArrivalPrice import getArrivalPrice
from Preprocessing.DailyValue import getDailyValue
from Preprocessing.Imbalance import getImbalance
from Preprocessing.MidQuoteReturns import getMidQuoteReturns
from Preprocessing.TerminalPrice import getTerminalPrice


startTS = 18 * 60 * 60 * 1000 / 2
impactTS = startTS + (6 * 60 * 60 * 1000) #3:30PM
endTS = startTS + (13 * 60 * 60 * 1000 / 2) #4PM
numBuckets = int(math.ceil((endTS - startTS) / (120000)))

# Define file paths for trades data
trade_directory = 'C:/Shubham/ATQSHW1/trades/'
quote_directory = 'C:/Shubham/ATQSHW1/quotes/'

# Read the list of S&P 500 stock symbols from the file
sp500_file_path = 'SP500.txt'
sp500_stocks = []
with open(sp500_file_path, 'r') as file:
    for line in file:
        symbol = line.strip()  # Remove any leading/trailing whitespace
        sp500_stocks.append(symbol)

# Initialize matrices to store computed values
num_stocks = len(sp500_stocks)
# the number of days based on the number of subfolders in the quotes directory
num_days = len(os.listdir(quote_directory))

#sp500_stocks = sp500_stocks[0:2]
# Expected shape: [500, 12800]
midQuoteReturnsArray = []
totalDailyValue = []
imbalance = []
vwap330 = []
vwapClose = []
arrivalPrice = []
terminalPrice = []

# Iterate over each subfolder within the quote directory
for quote_day in os.listdir(quote_directory):
    quote_day_path = os.path.join(quote_directory, quote_day)
    # Iterate over each stock symbol within the S&P 500 list
    mqr_stock = []
    tdv_stock = []
    imb_stock = []
    vwap330_stock = []
    vwapClose_stock = []
    arrival_stock = []
    terminal_stock = []
    
    for stock_symbol in sp500_stocks:
        quote_path = os.path.join(quote_day_path, f"{stock_symbol}_quotes.binRQ")
        trade_path = os.path.join(trade_directory, quote_day, f"{stock_symbol}_trades.binRT")
        if os.path.exists(quote_path) and os.path.exists(trade_path):
            trades = TAQTradesReader(trade_path)
            quotes = TAQQuotesReader(quote_path)
        
        mqr_stock.append(getMidQuoteReturns(quotes,startTS, endTS, numBuckets)) 
        tdv_stock.append(getDailyValue(trades)) # (500,daily)
        imb_stock.append(getImbalance(trades, startTS, impactTS))
        vwap330_stock.append(VWAP(trades, startTS, impactTS).getVWAP())
        vwapClose_stock.append(VWAP(trades, startTS, endTS).getVWAP())
        arrival_stock.append(getArrivalPrice(trades, startTS, endTS, numBuckets)) 
        terminal_stock.append(getTerminalPrice(trades, startTS, endTS, numBuckets))

    midQuoteReturnsArray.append(mqr_stock) # [65, 500, daily]
    totalDailyValue.append(tdv_stock)
    imbalance.append(imb_stock)
    vwap330.append(vwap330_stock)
    vwapClose.append(vwapClose_stock)
    arrivalPrice.append(arrival_stock)
    terminalPrice.append(terminal_stock)

concatenated_array = np.concatenate(midQuoteReturnsArray, axis=1)
midQuoteReturnsArray = np.reshape(concatenated_array, (concatenated_array.shape[1], -1)).T
totalDailyValue = np.array(totalDailyValue).T
imbalance = np.array(imbalance).T
vwap330 = np.array(vwap330).T
vwapClose = np.array(vwapClose).T
arrivalPrice = np.array(arrivalPrice).T
terminalPrice = np.array(terminalPrice).T

print("midQuoteReturnsArray:", midQuoteReturnsArray.shape)
print("Total Daily Value:",totalDailyValue.shape)
print("Imbalance:", imbalance.shape)
print("VWAP Impact:", vwap330.shape)
print("VWAP Close:", vwapClose.shape)
print("Arrival Price:",arrivalPrice.shape)
print("Terminal Price:", terminalPrice.shape)

import pandas as pd
import numpy as np

midQuoteReturnsArrayDf = pd.DataFrame(midQuoteReturnsArray, index=sp500_stocks)
totalDailyValueDf = pd.DataFrame(totalDailyValue, index=sp500_stocks)
imbalanceDf = pd.DataFrame(imbalance, index=sp500_stocks)
vwap330Df = pd.DataFrame(vwap330, index=sp500_stocks)
vwapCloseDf = pd.DataFrame(vwapClose, index=sp500_stocks)
arrivalPriceDf = pd.DataFrame(arrivalPrice, index=sp500_stocks)
terminalPriceDf = pd.DataFrame(terminalPrice, index=sp500_stocks)

midQuoteReturnsArrayDf.to_csv("Data/midQuoteReturnsArrayDf.csv", index_label="Stock")
totalDailyValueDf.to_csv("Data/totalDailyValueDf.csv", index_label="Stock")
imbalanceDf.to_csv("Data/imbalanceDf.csv", index_label="Stock")
vwap330Df.to_csv("Data/vwap330Df.csv", index_label="Stock")
vwapCloseDf.to_csv("Data/vwapCloseDf.csv", index_label="Stock")
arrivalPriceDf.to_csv("Data/arrivalPriceDf.csv", index_label="Stock")
terminalPriceDf.to_csv("Data/terminalPriceDf.csv", index_label="Stock")


#df.to_csv("data.csv")
