import backtrader as bt import yfinance as yf from strategy import RSIFuturesStrategy from config import SYMBOL, INITIAL_CASH, COMMISSION, RSI_PERIOD, RSI_OVERBOUGHT, RSI_OVERSOLD

def run_backtest(): cerebro = bt.Cerebro()

# Load Data (MNQ/NQ proxy via yfinance)
data_df = yf.download(SYMBOL, period="2y", interval="1h")
data = bt.feeds.PandasData(dataname=data_df)

cerebro.adddata(data)
cerebro.addstrategy(RSIFuturesStrategy, 
                     rsi_period=RSI_PERIOD, 
                     overbought=RSI_OVERBOUGHT, 
                     oversold=RSI_OVERSOLD)

cerebro.broker.setcash(INITIAL_CASH)
cerebro.broker.setcommission(commission=COMMISSION)

print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')
cerebro.run()
print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')

cerebro.plot()


if name == "main": run_backtest()