import ccxt
import pandas as pd
from datetime import datetime, timedelta

# Initialize Binance exchange
def initialize_exchange():
    exchange = ccxt.binance({
        'rateLimit': 1200,
        'enableRateLimit': True
    })
    return exchange

# Fetch historical OHLCV data (Open, High, Low, Close, Volume)
def fetch_historical_data(exchange, symbol, timeframe, days):
    since = exchange.parse8601((datetime.now() - timedelta(days=days)).isoformat())
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since)
    data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
    return data

# Calculate daily price movement for 0.01 BTC
def calculate_daily_movement(data, btc_amount=0.01):
    data['daily_movement'] = data['close'].diff().abs() * btc_amount
    total_movement = data['daily_movement'].sum()
    return data, total_movement

def main():
    exchange = initialize_exchange()
    symbol = 'BTC/USDT'  # Symbol to analyze
    timeframe = '1d'  # Daily timeframe
    days = 30  # Last 30 days

    print("Fetching data from Binance...")
    data = fetch_historical_data(exchange, symbol, timeframe, days)

    print("Calculating daily price movements...")
    data, total_movement = calculate_daily_movement(data)

    print("\nDaily Price Movements for 0.01 BTC:\n")
    print(data[['timestamp', 'close', 'daily_movement']])

    print(f"\nTotal Price Movement for 0.01 BTC over {days} days: ${total_movement:.2f}")

if __name__ == "__main__":
    main()