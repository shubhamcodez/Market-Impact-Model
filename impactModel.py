import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

totalDailyValue = pd.read_csv("Input/totalDailyValueDf.csv")
imbalance = pd.read_csv("Input/imbalanceDf.csv")
vwap330 = pd.read_csv("Input/vwap330Df.csv")
arrivalPrice = pd.read_csv("Input/arrivalPriceDf.csv")
terminalPrice = pd.read_csv("Input/terminalPriceDf.csv")
dailyVol = pd.read_csv("Input/dailyVolDf.csv")

# Drop the "Stock" column if present
totalDailyValue.drop("Stock", axis=1, inplace=True)
imbalance.drop("Stock", axis=1, inplace=True)
vwap330.drop("Stock", axis=1, inplace=True)
arrivalPrice.drop("Stock", axis=1, inplace=True)
terminalPrice.drop("Stock", axis=1, inplace=True)
dailyVol.drop("Stock", axis=1, inplace=True)

#compute rolling 10 day average of daily value
avgDailyValue = totalDailyValue.copy()

queue = []
for c in totalDailyValue.columns:
    #add new day
    queue.append(totalDailyValue[c])


    if len(queue) == 10:
        avgDailyValue[c] = sum(queue) / 10

        #remove the earliest day in the queue
        queue.pop(0)
    else:
        avgDailyValue[c] = np.zeros_like(avgDailyValue.index)

#we use the data from day 11 and onwards because the daily vol and average value are not avaliable before then
totalDailyValue = totalDailyValue[totalDailyValue.columns[10:]]
imbalance = imbalance[imbalance.columns[10:]]
vwap330 = vwap330[vwap330.columns[10:]]
arrivalPrice = arrivalPrice[arrivalPrice.columns[10:]]
terminalPrice = terminalPrice[terminalPrice.columns[10:]]
dailyVol = dailyVol[dailyVol.columns[10:]]
avgDailyValue = avgDailyValue[avgDailyValue.columns[10:]]

# Extract the required data for computation
impact330 = vwap330 - arrivalPrice
permanent_impact = (terminalPrice - arrivalPrice)/2


Y = (impact330 - permanent_impact)  # temp_impact
X = imbalance
V = avgDailyValue

# Replace infinite and NaN values with stock specific means
Y = Y.apply(lambda row: row.fillna(row.mean()), axis=1)

#perform the non-linear regression to minimize the sum of squared error

#stack the data to one column
y = np.array(Y.stack())
x = np.array((X / (6*V/6.5)).stack())
sigma = np.array(dailyVol.stack())

def temp_impact(x,eta,beta):
    temporary_impact = eta * sigma * np.sign(x) * np.power(np.abs(x) , beta)
    return temporary_impact

# Perform the curve fitting
popt, pcov = curve_fit(temp_impact, x, y)

# popt contains the optimal values for eta and beta
eta_optimal = popt[0]
beta_optimal = popt[1]

#print the result
print('Optimal eta: %.5f, Optimal beta: %.5f'%(eta_optimal,beta_optimal))