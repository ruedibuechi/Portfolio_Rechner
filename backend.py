import yfinance as yf

data = yf.download("AAPL NESN.SW BMW.DE TSLA NIO", start="2019-01-01", end="2022-12-01")

data.to_csv('shareprices.csv')
