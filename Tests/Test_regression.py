import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
import unittest

#read the data
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

#caculate the parameters needed
X = imbalance
V = avgDailyValue


x = np.array((X / (6*V/6.5)).stack())
sigma = np.array(dailyVol.stack())

#parametric bootstrapping to see if our regression routine would recover the coeff
m,std = np.mean(x),np.std(x)


def temp_impact(x,eta,beta):
    temporary_impact = eta * sigma * np.sign(x) * np.power(np.abs(x) , beta)
    return temporary_impact


class Test_Curvefit(unittest.TestCase):

    def testRegression(self):
        #we preset some number for eta and beta
        eta = 0.3
        beta = 1.2
        
        #we check if the recovered parameters are consistent
        eta_test_list = []
        beta_test_list = []
        for i in range(1000):
            #simulate a dataset
            x_test = np.random.normal(m,std,size = len(sigma))

            #add some noise
            noise_level = std/3

            #simulate y-values according to the preset eta and beta
            y_test = eta * sigma * np.sign(x_test) * np.power(np.abs(x_test) , beta) + np.random.normal(0,noise_level,size = len(x_test))

            #fit the generated dataset
            popt, pcov = curve_fit(temp_impact, x_test, y_test)
            eta_test_list.append(popt[0])
            beta_test_list.append(popt[1])
        
        eta_test = np.mean(eta_test_list)
        beta_test = np.mean(beta_test_list)

        self.assertAlmostEqual(eta,eta_test, delta=0.01)
        self.assertAlmostEqual(beta,beta_test, delta=0.01)

        print('true eta: %s, recovered eta: %s'%(eta,eta_test))
        print('true beta: %s, recovered beta: %s'%(beta,beta_test))

if __name__ == '__main__':
    unittest.main() 