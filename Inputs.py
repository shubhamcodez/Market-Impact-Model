import os
import pandas as pd
import numpy as np
from taq.TAQQuotesReader import TAQQuotesReader
from taq.TAQTradesReader import TAQTradesReader
from impactUtils.TickTest import TickTest
from datetime import time

import numpy as np

def filter_high_volatility_days(volatility_df, percentile_threshold=95):
    # Initialize a list to store filtered days
    filtered_days = []
    daily_vol = []
    
    # Iterate over each 195-row range
    for i in range(0, len(volatility_df), 195):
        # Extract volatility values within the current range
        range_volatility = volatility_df.iloc[i:i+195]
        # Calculate the average volatility for each day (row) in the range
        daily_volatility = range_volatility.mean()
        # Calculate the mean volatility for the entire range
        mean_volatility = daily_volatility.mean()
        daily_vol.append(mean_volatility)
    
    # Calculate the percentile threshold based on the given percentile
    volatility_threshold = np.percentile(daily_vol, percentile_threshold)
    #print(volatility_threshold)
    # Filter out the days with volatility below the threshold
    for i, volatility in enumerate(daily_vol):
        #print(volatility <= volatility_threshold)
        if volatility <= volatility_threshold:
            # Append the day index to the filtered_days list
            filtered_days.append(i)
    return filtered_days

def daily_volatility(volatility_df):
    daily_vol = []
    for i in range(0, len(volatility_df), 195):
        # Extract volatility values within the current range
        range_volatility = volatility_df.iloc[i:i+195]
        # Calculate the average volatility for each day (row) in the range
        daily_volatility = range_volatility.mean()
        # Calculate the mean volatility for the entire range
        mean_volatility = daily_volatility
        daily_vol.append(mean_volatility)

    return np.array(daily_vol).T

def compute_volatility(midQuoteReturnsArrayDf):
    window_size = int(10 * 6.5 * 30)  # 10 days
    stds = []
    
    # Fill missing values in the DataFrame
    midQuoteReturnsArrayDf.fillna(0, inplace=True)
    
    for index, row in midQuoteReturnsArrayDf.iterrows():
        # Calculate rolling standard deviation with the specified window size
        rolling_std = row.rolling(window=window_size).std()
        # Scale the standard deviation to daily values
        scaled_std = rolling_std * np.sqrt(195)
        stds.append(scaled_std)
    
    # Concatenate the list of scaled standard deviations into a DataFrame
    volatility_df = pd.concat(stds, axis=1)
    volatility_df.columns = midQuoteReturnsArrayDf.index  # Assign column names as stock symbols
    volatility_df.fillna(0, inplace=True)
    
    return volatility_df




midQuoteReturnsArrayDf = pd.read_csv("Data/midQuoteReturnsArrayDf.csv", index_col=0)
totalDailyValueDf = pd.read_csv("Data/totalDailyValueDf.csv",index_col=0)
imbalanceDf = pd.read_csv("Data/imbalanceDf.csv",index_col=0)
vwap330Df = pd.read_csv("Data/vwap330Df.csv",index_col=0)
vwapCloseDf = pd.read_csv("Data/vwapCloseDf.csv",index_col=0)
arrivalPriceDf = pd.read_csv("Data/arrivalPriceDf.csv",index_col=0)
terminalPriceDf = pd.read_csv("Data/terminalPriceDf.csv",index_col=0)
volatility_df = compute_volatility(midQuoteReturnsArrayDf)
filtered_indices = filter_high_volatility_days(volatility_df)
daily_vol = pd.DataFrame(daily_volatility(volatility_df))

'''print(daily_vol.shape)
print(terminalPriceDf.shape)'''

midQuoteReturnsArrayDf = midQuoteReturnsArrayDf.iloc[:, filtered_indices]
totalDailyValueDf = totalDailyValueDf.iloc[:, filtered_indices]
imbalanceDf = imbalanceDf.iloc[:, filtered_indices]
vwap330Df = vwap330Df.iloc[:, filtered_indices]
vwapCloseDf = vwapCloseDf.iloc[:, filtered_indices]
arrivalPriceDf = arrivalPriceDf.iloc[:, filtered_indices]
terminalPriceDf = terminalPriceDf.iloc[:, filtered_indices]
daily_vol =  daily_vol.iloc[:, filtered_indices]

midQuoteReturnsArrayDf.to_csv("Input/midQuoteReturnsArrayDf.csv", index_label="Stock")
totalDailyValueDf.to_csv("Input/totalDailyValueDf.csv", index_label="Stock")
imbalanceDf.to_csv("Input/imbalanceDf.csv", index_label="Stock")
vwap330Df.to_csv("Input/vwap330Df.csv", index_label="Stock")
vwapCloseDf.to_csv("Input/vwapCloseDf.csv", index_label="Stock")
arrivalPriceDf.to_csv("Input/arrivalPriceDf.csv", index_label="Stock")
terminalPriceDf.to_csv("Input/terminalPriceDf.csv", index_label="Stock")
daily_vol.to_csv("Input/dailyVolDf.csv", index_label="Stock")
