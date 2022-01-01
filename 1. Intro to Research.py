import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


# Sample 100 points with a mean of 0 and an std of 1. This is a standard normal distribution

def randomplot():
    X = np.random.normal(0, 1, 100)
    X2 = np.random.normal(0, 1, 100)

    plt.plot(X)
    plt.plot(X2)
    plt.xlabel('Time')
    plt.ylabel('Returns')
    plt.legend(['X', 'X2'])


data = yf.download(['GME'], '2015-01-01', '2020-01-01')
data['return'] = data['Adj Close'].pct_change()[1:]
plt.hist(data['return'], bins=20)
plt.xlabel('Return')
plt.ylabel('Freq')


MAVG = data.rolling(60).mean()
plt.plot(data.index, data.values)
plt.plot(MAVG.index, MAVG.values)
plt.ylabel('Price')
plt.legend(['GME', '60-day MAVG'])
plt.show()

