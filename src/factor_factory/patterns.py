"""
This library is made for generate candlestick patterns.
"""

import pandas as pd

def bearish(df_ohlc: pd.DataFrame, pos: int) -> pd.Series:
    row = df_ohlc.iloc[pos, :]
    if row["close"] < row["open"]:
        return 1
    elif row["close"] < row["open"]:
        return 0
