import os
import time
import pandas as pd
from binance.client import Client
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_triangular_arbitrage_opportunity(client, symbol_list):
    """
    Identifies a triangular arbitrage opportunity.
    """
    for symbol1 in symbol_list:
        for symbol2 in symbol_list:
            for symbol3 in symbol_list:
                if symbol1[3:] == symbol2[:3] and symbol2[3:] == symbol3[:3] and symbol3[3:] == symbol1[:3]:
                    # Check for arbitrage opportunity
                    ticker1 = client.get_ticker(symbol=symbol1)
                    ticker2 = client.get_ticker(symbol=symbol2)
                    ticker3 = client.get_ticker(symbol=symbol3)

                    price1 = float(ticker1['lastPrice'])
                    price2 = float(ticker2['lastPrice'])
                    price3 = float(ticker3['lastPrice'])

                    if price1 * price2 * price3 > 1:
                        return (symbol1, symbol2, symbol3)
    return None

def main():
    """
    Main function to run the bot.
    """
    # Load configuration
    with open('config.json') as f:
        config = json.load(f)

    # Initialize Binance client
    client = Client(config['api_key'], config['api_secret'])

    # Get all symbols
    exchange_info = client.get_exchange_info()
    symbol_list = [s['symbol'] for s in exchange_info['symbols']]

    logging.info("Starting triangular trading bot...")

    while True:
        try:
            opportunity = get_triangular_arbitrage_opportunity(client, symbol_list)
            if opportunity:
                logging.info(f"Arbitrage opportunity found: {opportunity}")
                # Execute trades
                try:
                    # Place orders
                    order1 = client.order_market_buy(symbol=opportunity[0], quantity=1)
                    order2 = client.order_market_sell(symbol=opportunity[1], quantity=1)
                    order3 = client.order_market_sell(symbol=opportunity[2], quantity=1)

                    logging.info("Trades executed successfully!")
                except Exception as e:
                    logging.error(f"An error occurred during trade execution: {e}")
            time.sleep(1)
        except Exception as e:
            logging.error(f"An error occurred in the main loop: {e}")

if __name__ == "__main__":
    main()
