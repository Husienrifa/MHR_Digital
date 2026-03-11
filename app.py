# app.py

# Main application that integrates all modules

from data_fetcher import DataFetcher
from technical_indicators import TechnicalIndicators
from screening_logic import ScreeningLogic
from telegram_bot import TelegramBot


def main():
    # Initialize all components
    data_fetcher = DataFetcher()
    technical_indicators = TechnicalIndicators()
    screening_logic = ScreeningLogic()
    telegram_bot = TelegramBot()

    # Fetch data
    data = data_fetcher.fetch_data()
    
    # Calculate technical indicators
    indicators = technical_indicators.calculate(data)
    
    # Apply screening logic
    screened_data = screening_logic.apply(indicators)
    
    # Send results to Telegram
    telegram_bot.send_message(screened_data)


if __name__ == '__main__':
    main()