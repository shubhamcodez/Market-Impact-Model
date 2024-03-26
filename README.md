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

1. Data preprocessing loop for each stock and day.
2. Filtering high volatility days to exclude from the final regression.
3. Testing code through unit tests and parametric bootstrap process.
4. Summary statistics analysis including residuals, parameter significance, fit quality, and differences between liquid and illiquid stocks.
5. Analysis of optimal lookbacks on volatility and average daily value imbalance.

## Team Members

- [Name 1](https://github.com/username1) - NetID: netid1
- [Name 2](https://github.com/username2) - NetID: netid2
- [Name 3](https://github.com/username3) - NetID: netid3

## GitHub Repository

[Project Repository](https://github.com/yourusername/project-repository)

## Additional Notes

- Ensure all scripts are well-documented and follow best coding practices.
- Perform rigorous testing to validate the correctness of the implemented algorithms.
- Provide clear explanations and interpretations for the obtained results in the summary statistics and analysis section.
- Regularly update the README with any project developments or changes.
