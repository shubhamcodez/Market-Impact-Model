The folder contains 3 modules: taq, impactUtils, Prprocessing
1. taq contains 3 functions : TAQQuotesReader, TAQTradesReader, MyDirectories
2. preprocessing module contains 5 functions: ArrivalPrice, Imbalance, DailyValue, MidQuoteReturns, TerminalPrice
3. impactUtils contains 4 functions: LastPriceBuckets, ReturnBuckets, TickTest, VWAP

The folder contains 3 data folders: 
1. Input - containing csv files of regression inputs
2. trades - containing trades data from NASDAQ
3. quotes - containing quotes data from NASDAQ

   
Directory Structure of the project goes as following:
ATQSHW1/
├── _pycache_
├── Data
│   ├── arrivalPriceOf.csv
│   ├── imbalanceOf.csv
│   ├── midQuoteReturnsArrayOf.csv
│   ├── terminalPriceOf.csv
│   ├── totalDailyValueOf.csv
│   ├── vwap330Of.csv
│   └── vwapCloseOf.csv
├── impactUtils
│   ├── _pycache_
│   ├── FirstPriceBuckets
│   │   ├── _pycache_
│   │   ├── __init__.py
│   │   └── FirstPriceBuckets.py
│   ├── LastPriceBuckets
│   ├── ReturnBuckets
│   ├── TickTest
│   └── VWAP
├── Input
├── Preprocessing
│       ├── ArrivalPrice
│         ├── _pycache_
│         ├── __init__.py
│         └── getArrivalPrice.py
│       ├── DailyValue
│       ├── Imbalance
│       ├── MidQuoteReturns
│       ├── TerminalPrice
├── __init__.py
├── quotes
├── taq
├── tests
└── trades
├── impactModel.py
├── Inputs.py
├── Lee's section of ATQS2024.mxm
├── Preprocessing.py
└── runTests.py
