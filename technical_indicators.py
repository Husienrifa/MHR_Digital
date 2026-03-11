import pandas as pd
import numpy as np

class TechnicalIndicators:
    def __init__(self, data):
        self.data = data

    def calculate_rsi(self, period=14):
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_macd(self, short_window=12, long_window=26, signal_window=9):
        exp1 = self.data['Close'].ewm(span=short_window, adjust=False).mean()
        exp2 = self.data['Close'].ewm(span=long_window, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=signal_window, adjust=False).mean()
        return macd, signal

    def calculate_bollinger_bands(self, window=20):
        sma = self.data['Close'].rolling(window=window).mean()
        rstd = self.data['Close'].rolling(window=window).std()
        upper_band = sma + (rstd * 2)
        lower_band = sma - (rstd * 2)
        return upper_band, lower_band

    def calculate_ema(self, span):
        return self.data['Close'].ewm(span=span, adjust=False).mean()

    # Add additional indicators as needed
