import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from config import USE_TEST_MODE

def get_live_price(ticker="AAPL"):
    data = yf.Ticker(ticker).history(period="1m")
    price = float(data["Close"].iloc[-1])
    return price

def get_historical_replay(ticker="AAPL"):
    """
    Simulates real-time playback using yesterday's 1-minute candles.
    """
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    data = yf.download(ticker, start=yesterday, end=today, interval="1m")
    for idx, row in data.iterrows():
        yield float(row["Close"])

def get_price(ticker):
    if USE_TEST_MODE:
        return get_historical_replay(ticker)
    else:
        return get_live_price(ticker)
