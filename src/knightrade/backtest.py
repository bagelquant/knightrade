"""
Backtest code module for KnightTrade

Author: Yanzhong(Eric) Huang
"""

import pandas as pd
from knightrade.strategy import Strategy
from knightrade.data.standard_data import TimeSeries

from dataclasses import dataclass, field


@dataclass(slots=True)
class Backtest:
    """
    Backtest class for simulating trading strategies.
    """

    strategy: Strategy
    price: TimeSeries

    # Optional parameters
    initial_cash: float = 1_000_000.0

    # Automatically set
    portfolio: TimeSeries = field(init=False)
    position: TimeSeries = field(init=False)
    cash: TimeSeries = field(init=False)

    def __post_init__(self):
        self.position = self.strategy.generate_signals()

    def run(self) -> None:
        """
        Update self.portfolio_value
        :return: None
        """
        # Portfolio Value
        portfolio = self.price.data * self.position.data
        portfolio = portfolio.sum(axis=1)

        # Calculate Cash
        trade_amount = self.position.data.diff()
        trade_value = trade_amount * self.price.data
        trade_value.iloc[0] = self.position.data.iloc[0]  # first trade
        trade_cost = trade_value.cumsum()

        cash: pd.Series = self.initial_cash - trade_cost.sum(axis=1)
        cash.name = "Cash"
        portfolio.name = "Portfolio"

        # Assign to TimeSeries
        self.cash = TimeSeries(cash.to_frame())
        self.portfolio = TimeSeries(portfolio + cash)


def _test() -> None:
    """Quick test for this module"""
    from knightrade.data.standard_data import TimeSeries
    from knightrade.strategy import SimpleMovingAverageStrategy

    # Example price data
    data = pd.DataFrame(
        {
            "AAPL": [150, 152, 154, 153, 155, 157, 156],
            "MSFT": [300, 305, 310, 308, 312, 315, 314],
        },
        index=pd.date_range("2023-01-01", periods=7),
    )
    price = TimeSeries(data)

    # Example strategy
    strategy = SimpleMovingAverageStrategy(_price=price, short_window=2, long_window=3, amount=100)

    # Run backtest
    backtest = Backtest(strategy=strategy, price=price)
    backtest.run()

    # Print results
    print(f"Portfolio Value:\n{backtest.portfolio}")
    print(f"Cash:\n{backtest.cash}")


if __name__ == "__main__":
    from time import perf_counter

    start = perf_counter()
    _test()
    end = perf_counter()
    print(f"Time cost: {end - start:.2f} s \n or {(end - start) / 60:.2f} min")
