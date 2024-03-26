# Market Impact Model

## Description

This project aims to develop an impact model for algorithmic trading and quantitative strategies, inspired by Almgren et al.'s "Direct Estimation of Equity Market Impact."
Reference: [Direct Estimation of Equity Market Impact](https://www.cis.upenn.edu/~mkearns/finread/costestim.pdf)

## Objective

The main objective is to build an impact model that can accurately estimate the market impact of trading activities using trading volume, price movements, and stock liquidity.

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

Note: You need to have the raw TAQ dataset in your directory in order to run the preprocessing tests. 
Only the parametric bootstrapping test for regression ([Test_regression.py](https://github.com/ssnyu/Market-Impact-Model/blob/main/Tests/Test_regression.py)) can be run without the raw dataset.

## Results
According to the non-linear regression equations:

$$h = \eta * \sigma * (\frac{X}{VT})^\beta$$

$h$: temporary impact
$\sigma$: stock specific volatility
$X$: Daily imbalance (value)
$V$:Average daily value 
$T$: time

We discovered $\eta = 0.33244$, $\beta = 0.36127$.

The analysis of the fit of the model are in [descriptiveStats.ipynb](https://github.com/ssnyu/Market-Impact-Model/blob/main/descriptiveStats.ipynb)



## Supplementary 

### Directory structure - [Directory.ReadME](https://github.com/ssnyu/Market-Impact-Model/blob/main/Directory.md)

## Team Members

- [Shubham Singh](https://github.com/ssnyu) NetID: sks9437
- [Tianqi Wang](https://github.com/foggyleo) NetID: tw2250
