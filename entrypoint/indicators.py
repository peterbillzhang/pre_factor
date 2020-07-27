from factor_factory import indicators
from data_fetcher import yf_reader
import matplotlib.pyplot as plt
import talib

from factor_factory.indicators import MovingAverageMethod

df_ohlc = yf_reader.get_ohlc("MSFT", start="2020-01-01")

ema = indicators.moving_average(df_ohlc, 20, MovingAverageMethod.EMA)

ma = indicators.moving_average(ema, 20, MovingAverageMethod.SMA)

print(ma[["Close", "ema", "sma"]].tail(10))

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.plot(ma.index.values,
        ma["Close"],
        color='purple')

ax.plot(ma.index.values, ma["ema"])

ax.plot(ma.index.values, ma["sma"], color="orange")

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Precipitation (inches)",
       title="Daily Total Precipitation\nBoulder, Colorado in July 2018")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

plt.show()
