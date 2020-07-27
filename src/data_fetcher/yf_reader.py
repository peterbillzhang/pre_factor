import pandas as pd
from pandas_datareader import data as pdr
import os


def get_nasdaq_100_components(csv_file_name: str):
    df_nasdaq100 = pd.read_csv(csv_file_name)

    return df_nasdaq100


def save_nasdaq_100_quotes(df_nasdaq_100_list: pd.DataFrame, output_path: str):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for index, row in df_nasdaq_100_list.iterrows():
        symbol = row['Symbol']
        print(symbol)
        data = pdr.DataReader(symbol,
                              start='2010-1-1',
                              end='2020-12-31',
                              data_source='yahoo')[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
        file_name = os.path.join(output_path, "{}.csv".format(symbol))
        data.to_csv(file_name, index=True, encoding='utf-8')


def get_nasdaqlisted(csv_file_name: str) -> pd.DataFrame:
    df_nasdaqlisted = pd.read_csv(csv_file_name, sep="|")

    return df_nasdaqlisted


def get_ohlc(symbol: str, start="2010-01-01", end="2020-12-31") -> pd.DataFrame:
    data = pdr.DataReader(symbol,
                          start=start,
                          end=end,
                          data_source='yahoo')[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    return data
