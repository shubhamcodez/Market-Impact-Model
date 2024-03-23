import pandas as pd
import numpy as np
from scipy.optimize import minimize

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

# Define the function to compute temporary impact
def temp_impact(params, X, V, sigma):
    eta, beta = params
    temporary_impact = eta * sigma * (X / (6*V/6.5)) ** beta 
    return temporary_impact

# Extract the required data for computation
impact330 = vwap330 - arrivalPrice
permanent_impact = (terminalPrice - arrivalPrice)/2


Y = (impact330 - permanent_impact)  # temp_impact
X = imbalance
V = totalDailyValue

# Replace infinite and NaN values with zeros
X = X.replace([np.inf, -np.inf, np.nan], 0)
V = V.replace([np.inf, -np.inf, np.nan], 0)
Y = Y.replace([np.inf, -np.inf, np.nan], 0)

def mean_absolute_error(params, X, V, dailyVol, Y):
    Ypred = temp_impact(params, X, V, dailyVol)
    if Y.shape != Ypred.shape:
        raise ValueError("Shapes of Y and Ypred are not equal")

    mae = np.mean((Y - Ypred))
    return abs(mae)

# Initial guess for eta and beta
initial_guess = [0.1, 0.8] #expected 0.142, 0.6

# Minimize the mean absolute error
result = minimize(mean_absolute_error, initial_guess, args=(X, V, dailyVol, Y), method='Nelder-Mead')
# Get the estimated parameters
eta, beta = result.x

# Print the estimated parameters
print(f"Estimated eta: {eta}")
print(f"Estimated beta: {beta}")
