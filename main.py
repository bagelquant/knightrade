"""
Main module

Author: Yanzhong(Eric) Huang
"""
import matplotlib.pyplot as plt
import pandas as pd
from time import perf_counter
from src.knightrade import read_yfinance, TimeSeries
from src.knightrade import SimpleMovingAverageStrategy, MeanReversionStrategy, Strategy
from src.knightrade import Backtest, plot_time_series, plot_drawdown
from dataclasses import dataclass



def main() -> None:
    """
    Main function to demonstrate the usage of the trading strategies.
    """

    # 1. Read data from Yahoo Finance using DataHandler module
    data_time_series = read_yfinance(tickers=["AAPL", "NVDA"], start="2020-01-01", end="2023-01-01", column="Close")

    # 2. Initialize the strategies
    sma = SimpleMovingAverageStrategy(_price=data_time_series,
                                      short_window=10,
                                      long_window=10,
                                      amount=100)
    mean_reversion = MeanReversionStrategy(_price=data_time_series,
                                           window=10,
                                           amount=100)
    # 2.1 Customize a strategy
    @dataclass(slots=True)
    class CustomStrategy(Strategy):
        """
        A simple custom strategy that inherits from Strategy.

        Long only when the price is above the moving average.
        """
        long_window: int        # Moving average window
        amount: float = 100.0   # Amount to buy

        def generate_signals(self) -> TimeSeries:
            """
            Generate buy/sell signals based on the moving average.

            ** This function is required to be implemented in the derived class. **
            ** abstractmethod. **
            """
            price = self._price.data.copy()
            signals = pd.DataFrame(index=price.index, columns=price.columns)
            # set signals type to float
            signals = signals.astype(float)

            # Calculate moving average
            mavg = price.rolling(window=self.long_window, min_periods=self.long_window).mean().shift(1)

            # Generate signals
            signals[price > mavg] = self.amount

            # set signals type to float
            signals = signals.astype(float)
            signals = signals.ffill().fillna(0)
            signals = TimeSeries(signals)
            return signals

    # 2.2 Initialize the custom strategy
    custom_strategy = CustomStrategy(_price=data_time_series,
                                      long_window=10,
                                      amount=100)

    # 3. Run the backtest

    sma_bt = Backtest(strategy=sma, price=data_time_series)
    mean_reversion_bt = Backtest(strategy=mean_reversion, price=data_time_series)
    custom_strategy_bt = Backtest(strategy=custom_strategy, price=data_time_series)

    # 4. Run the backtest
    sma_bt.run()
    mean_reversion_bt.run()
    custom_strategy_bt.run()

    # 4.1 Obtain the portfolio value
    portfolio_value_sma = sma_bt.portfolio.data
    portfolio_value_mean_reversion = mean_reversion_bt.portfolio.data
    portfolio_value_custom_strategy = custom_strategy_bt.portfolio.data
    result = TimeSeries(pd.concat([portfolio_value_sma,
                                   portfolio_value_mean_reversion,
                                   portfolio_value_custom_strategy], axis=1).sort_index())
    result.data.columns = ["SMA", "Mean Reversion", "Custom Strategy"]

    # 5. visualize the results
    fig_portfolio = plot_time_series(result, title="Different Strategies Backtest")
    fig_drawdown = plot_drawdown(result, title="Drawdown Backtest")
    fig_portfolio.savefig("docs/attachments/portfolio.png", dpi=300)
    fig_drawdown.savefig("docs/attachments/drawdown.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    start_time = perf_counter()
    main()

    end_time = perf_counter()
    print(f"Execution time: {end_time - start_time:.2f} seconds \n or {end_time - start_time:.2f} minutes")