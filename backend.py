import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL NESN.SW BMW.DE TSLA NIO", start="2019-01-01", end="2022-12-01")['Close']

print(data.head())

data.plot()
plt.show()