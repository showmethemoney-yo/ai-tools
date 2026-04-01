# src/data_loader.py

import yfinance as yf
import pandas as pd

def load_data(ticker="AAPL", start="2020-01-01"):
    """
    Download historical stock data from Yahoo Finance.
    Returns a DataFrame with 'Close' and 'Volume'.
    """
    df = yf.download(ticker, start=start)
    df = df[['Close', 'Volume']]
    return df

if __name__ == "__main__":
    # Load data for Apple
    df = load_data()
    print("First 5 rows of data:")
    print(df.head())