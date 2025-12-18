import backtrader as bt import pandas_ta as ta

class RSIFuturesStrategy(bt.Strategy): params = ( ('rsi_period', 14), ('overbought', 70), ('oversold', 30), )

def __init__(self):
    self.rsi = bt.indicators.RSI(self.data.close, period=self.p.rsi_period)
    self.order = None

def log(self, txt, dt=None):
    dt = dt or self.datas[0].datetime.date(0)
    print(f'{dt.isoformat()}, {txt}')

def notify_order(self, order):
    if order.status in [order.Submitted, order.Accepted]:
        return
    if order.status in [order.Completed]:
        if order.isbuy():
            self.log(f'BUY EXECUTED, Price: {order.executed.price:.2f}')
        else:
            self.log(f'SELL EXECUTED, Price: {order.executed.price:.2f}')
    self.order = None

def next(self):
    if self.order:
        return

    if not self.position:
        # Entry Logic: Oversold RSI
        if self.rsi < self.p.oversold:
            self.log(f'BUY CREATE, Price: {self.data.close[0]:.2f}')
            self.order = self.buy()
    else:
        # Exit Logic: Overbought RSI
        if self.rsi > self.p.overbought:
            self.log(f'SELL CREATE, Price: {self.data.close[0]:.2f}')
            self.order = self.sell()