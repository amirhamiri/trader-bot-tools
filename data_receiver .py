import pandas as pd
from binance.client import Client

client = Client()


def get_data(coin, timeframe):
    df = pd.DataFrame(client.futures_historical_klines(coin, timeframe, "10 days ago UTC"))
    df = df.iloc[:, :6]
    df.columns = ["Time", "Open", "High", "Low", "Close", "Volume"]
    df = df.set_index("Time")
    df.index = pd.to_datetime(df.index, unit="ms")
    df = df.astype(float)
    return df


df = get_data("BTCUSDT", client.KLINE_INTERVAL_30MINUTE)
df.to_csv(path_or_buf="BTC-USDT")
