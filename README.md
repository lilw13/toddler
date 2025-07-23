# Binance Triangular Trading Bot

This is a Python bot that performs triangular arbitrage on the Binance cryptocurrency exchange.

## How it works

The bot identifies triangular arbitrage opportunities by checking for price discrepancies between three currency pairs. When an opportunity is found, the bot executes a series of trades to profit from the price difference.

## Getting started

### Prerequisites

* Python 3.6 or higher
* A Binance account

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/toddler.git
   ```
2. Install the required dependencies:
   ```
   pip install -r bot/requirements.txt
   ```
3. Create a `config.json` file in the root directory and add your Binance API key and secret:
   ```json
   {
       "api_key": "YOUR_API_KEY",
       "api_secret": "YOUR_API_SECRET"
   }
   ```

### Usage

To run the bot, execute the following command:
```
python bot/main.py
```

## Disclaimer

This bot is for educational purposes only. Use it at your own risk. The author is not responsible for any financial losses.
