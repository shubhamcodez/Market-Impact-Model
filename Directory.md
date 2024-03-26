The folder contains 3 modules: taq, impactUtils, Prprocessing
1. taq contains 3 functions : TAQQuotesReader, TAQTradesReader, MyDirectories
2. preprocessing module contains 5 functions: ArrivalPrice, Imbalance, DailyValue, MidQuoteReturns, TerminalPrice
3. impactUtils contains 4 functions: LastPriceBuckets, ReturnBuckets, TickTest, VWAP

The folder contains 3 data folders: 
1. Input - containing csv files of regression inputs
2. trades - containing trades data from NASDAQ
3. quotes - containing quotes data from NASDAQ

   
Directory Structure of the project goes as following:
ATQSHW1/ <br>
├── _pycache_ <br>
├── Data<br>
│   ├── arrivalPriceDf.csv<br>
│   ├── imbalanceDf.csv<br>
│   ├── midQuoteReturnsArrayDf.csv<br>
│   ├── terminalPriceDf.csv<br>
│   ├── totalDailyValueDf.csv<br>
│   ├── vwap330Df.csv<br>
│   └── vwapCloseDf.csv<br>
├── impactUtils<br>
│   ├── _pycache_<br>
│   ├── FirstPriceBuckets<br>
│   │   ├── _pycache_<br>
│   │   ├── __init__.py<br>
│   │   └── FirstPriceBuckets.py<br>
│   ├── LastPriceBuckets<br>
│   ├── ReturnBuckets<br>
│   ├── TickTest<br>
│   └── VWAP<br>
├── Input<br>
├── Preprocessing<br>
│       ├── ArrivalPrice<br>
│         ├── _pycache_<br>
│         ├── __init__.py<br>
│         └── getArrivalPrice.py<br>
│       ├── DailyValue<br>
│       ├── Imbalance<br>
│       ├── MidQuoteReturns<br>
│       ├── TerminalPrice<br>
├── __init__.py<br>
├── quotes<br>
├── taq<br>
├── tests<br>
└── trades<br>
├── impactModel.py<br>
├── Inputs.py<br>
├── Lee's section of ATQS2024.mxm<br>
├── Preprocessing.py<br>
└── runTests.py<br>

Lee's section of ATQS2024.mxm
Preprocessing.py
runTests.py

