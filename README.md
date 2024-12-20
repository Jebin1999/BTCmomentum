# BTC Momentum Analysis

This repository contains a Python script (`BTCmomentum.py`) that analyzes the daily price movements of Bitcoin (BTC) against USDT. The script uses the `ccxt` library to fetch historical OHLCV (Open, High, Low, Close, Volume) data from the Binance exchange and calculates the daily price movement for a specified amount of BTC.

## Features

- Fetches historical OHLCV data from Binance using `ccxt`.
- Calculates daily price movements for a specified amount of BTC.
- Summarizes total price movements over a given time period.

## Requirements

To run this script, you need to have the following installed:

- Python 3.7 or higher
- Required Python libraries:
  - `ccxt`
  - `pandas`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BTC-momentum.git
   cd BTC-momentum
   ```

2. Install the required libraries:
   ```bash
   pip install ccxt pandas
   ```

## Usage

1. Run the script:
   ```bash
   python BTCmomentum.py
   ```

2. The script will:
   - Fetch the last 30 days of daily OHLCV data for BTC/USDT from Binance.
   - Calculate daily price movements for 0.01 BTC.
   - Display the daily price movements and the total price movement over the specified time period.

## Example Output

```
Fetching data from Binance...
Calculating daily price movements...

Daily Price Movements for 0.01 BTC:

   timestamp        close  daily_movement
0  2023-11-20  30000.00          0.00
1  2023-11-21  31000.00        100.00
...

Total Price Movement for 0.01 BTC over 30 days: $500.00
```

## Configuration

You can modify the following parameters in the `main` function:

- **symbol**: The cryptocurrency pair to analyze (default: `BTC/USDT`).
- **timeframe**: The timeframe for OHLCV data (default: `1d` for daily data).
- **days**: The number of days of historical data to fetch (default: `30`).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository, submit a pull request, or open an issue.

## Author

[Your Name](https://github.com/Jebin1999)

## Disclaimer

This script is for educational purposes only and should not be used for financial advice or trading decisions. Use it at your own risk.

