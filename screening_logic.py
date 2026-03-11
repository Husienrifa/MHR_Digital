# Screening Logic for Swing Trade and Scalping

## Technical Indicators Used
- Moving Average (MA)
- Relative Strength Index (RSI)
- Bollinger Bands

## Swing Trade Screening Logic
1. **Moving Average**: If the current price is above the 50-day moving average, it's a potential buy signal.
2. **RSI**: If the RSI is below 30, it's an indication that the asset is oversold.
3. **Bollinger Bands**: If the price hits the lower band, it’s a potential buy signal.

## Scalping Screening Logic
1. **Moving Average**: Use the 5-minute moving average crossover as a buy/sell indicator.
2. **RSI**: Look for RSI to exceed 70 (overbought) for selling.
3. **Volume**: High trading volume indicates a stronger price movement.

# Example Function Definitions

def swing_trade_logic(price, moving_average, rsi, bollinger_band):
    if price > moving_average and rsi < 30 and price <= bollinger_band['lower']:
        return "Buy"
    return "Hold"


def scalping_logic(price, sma_short, sma_long, rsi, volume):
    if sma_short > sma_long and rsi < 70 and volume > threshold:
        return "Buy"
    return "Sell"