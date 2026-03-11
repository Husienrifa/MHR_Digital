import requests
import yfinance as yf

# Fetch stock data from Alpha Vantage

def fetch_alpha_vantage(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Fetch stock data from Finnhub

def fetch_finnhub(symbol, api_key):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Fetch stock data from yfinance

def fetch_yfinance(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')
    return data.to_dict()

# Example usage:
# alpha_data = fetch_alpha_vantage('AAPL', 'YOUR_ALPHA_VANTAGE_API_KEY')
# finnhub_data = fetch_finnhub('AAPL', 'YOUR_FINNHUB_API_KEY')
# yfinance_data = fetch_yfinance('AAPL')