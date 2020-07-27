"""
This library is made to create most commonly used
indicators according to given ohlc data.
"""
from enum import Enum
import talib as ta
import pandas as pd


class MovingAverageMethod(Enum):
    """
    Moving average method Enum
    """
    SMA = 1
    EMA = 2


def moving_average(df_ohlc: pd.DataFrame, period: int,
                   method: MovingAverageMethod = MovingAverageMethod.EMA) -> pd.DataFrame:
    if method == MovingAverageMethod.EMA:
        # df_ohlc["ema"] = df_ohlc["Close"].ewm(span=period, adjust=False).mean()
        df_ohlc["ema"] = ta.EMA(df_ohlc["Close"], timeperiod=period)
    else:
        df_ohlc["sma"] = ta.SMA(df_ohlc["Close"], timeperiod=period)

    return df_ohlc

