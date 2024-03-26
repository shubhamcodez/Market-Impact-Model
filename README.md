# Market Impact Model

## Description

This project aims to develop an impact model for algorithmic trading and quantitative strategies, inspired by Almgren et al.'s "Direct Estimation of Equity Market Impact." The model focuses on predicting the impact of trading activities on stock prices, utilizing data from the TAQ dataset and employing techniques to filter high volatility days.

Reference: [Direct Estimation of Equity Market Impact](https://www.cis.upenn.edu/~mkearns/finread/costestim.pdf)

## Objective

The main objective is to build an impact model that can accurately estimate the market impact of trading activities, particularly focusing on the relationship between trading volume, price movements, and stock liquidity.

## Data

- Utilizes the TAQ dataset, focusing on a subset of S&P 500 stocks for liquidity.
- Uses average daily value traded instead of average daily volume traded to account for stock splits.
- Data processing involves computing various metrics such as mid-quote returns, total daily value, arrival price, value imbalance, volume-weighted average price, and terminal price.

## Methodology
1. Preprocess data to obtain daily value traded, volatility, imbalance, terminal, and arrival price.
2. Use these variables as input for a non-linear regression to get eta and beta parameters in the temporary impact equation.

## Running the Code
To run the code, follow these steps: <br>

Install the required dependencies: `pip install -r requirements.txt` <br>
Run the tests: `python runTests.py` <br>
To preprocess and prepare data: `python Preprocessing.py` and `python Inputs.py` <br>
Execute the main script: `python impactModel.py` <br>

## Team Members

- [Shubham Singh](https://github.com/ssnyu)
- [Tianqi Wang](https://github.com/foggyleo)
