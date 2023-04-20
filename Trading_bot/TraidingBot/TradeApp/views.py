from django.shortcuts import render
import requests
import pandas as pd
from binance.client import Client
import talib
from talib import abstract
from tradingview_ta import TA_Handler, Interval, Exchange
import matplotlib.pyplot as plt
#[p9.]
api_key = '2OvN6ErpB20vzCbwgIbmt5OtwZUjId2vYMweJ2iOVgHJG6zMnMgN1yFeDZ2EGolf'
api_secret = 'AIOFy6ZjcFIwXmEZFDsTxZGmFeTcQNS0oW2TFh72Nwx8kHFYd1ntSfeoNKjAp8m1'

client = Client(api_key, api_secret)

def index_page(requests):
    tit = "FastTrade"
    return render(requests, 'TradeApp/main.html')

def auto(requests):
    return render(requests,'TradeApp/auto.html')

def rec_cur(requests):
    return render(requests,'TradeApp/rec_cur.html')

def get_cur(requests):
    all_tickers = pd.DataFrame(client.get_ticker())
    usdt = all_tickers[all_tickers.symbol.str.contains('USDT')]
    work = usdt[~((usdt.symbol.str.contains('UP')) | (usdt.symbol.str.contains('DOWN')))]
    top_coin = work[work.priceChangePercent == work.priceChangePercent.max()]
    top_coin = top_coin.symbol.values[0]
    print(top_coin)
    return render(requests ,'TradeApp/rec_cur.html',{'top_coin': top_coin})

def rec_buy(requests):
    return render(requests, 'TradeApp/rec_buy.html',)

def rec_sell(requests):
    return render(requests, 'TradeApp/rec_sell.html')

def last_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + 'min ago UTC'))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'open', 'high', 'low', 'close', 'volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

df = last_data("BTCUSDT", '1m', '120')
sma = abstract.SMA(df["close"])
rsa = abstract.RSI(df)

tesla = TA_Handler(
    symbol="BTCUSDT",
    screener="Crypto",
    exchange="Binance",
    interval=Interval.INTERVAL_1_MINUTE,
)


df.insert(5,"SMA",sma)
df.insert(5,"RSA",rsa)
df['stddev'] = df.close.rolling(window = 20).std
plt.figure(figsize=(20,10))
plt.plot(df[['open', 'high', 'low', 'close']])
plt.savefig('gr.png')

print(df)




































