Automated Nasdaq Futures RSI Strategy

This project implements a fully automated backtesting engine for a Nasdaq (NQ/MNQ) futures strategy based on the Relative Strength Index (RSI).

Strategy Overview

Instrument: Nasdaq 100 Futures (NQ=F).

Indicator: RSI (14-period).

Entry: Buy when RSI crosses below 30 (Oversold).

Exit: Sell when RSI crosses above 70 (Overbought).

Features

Backtrader Integration: Industry-standard engine for strategy execution.

Dynamic Config: Easily tune RSI thresholds and commissions in config.py.

Live Data Proxy: Uses yfinance to fetch historical futures data.

Visualization: Generates performance charts automatically.

Setup Instructions

Install requirements:

Bash
pip install -r requirements.txt


Run the backtest:

Bash
python main.py

Next Steps for Live Deployment

To move to live trading, replace the yfinance data feed with an Interactive Brokers (IBKR) or NinjaTrader API bridge.