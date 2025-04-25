"""
Main module

Author: Yanzhong(Eric) Huang
"""
from time import perf_counter
from src.knightrade import read_yfinance
from src.knightrade import SimpleMovingAverageStrategy, MeanReversionStrategy
from src.knightrade import Backtest


def main() -> None:
    """
    Main function to demonstrate the usage of the trading strategies.
    """
    data_time_series = read_yfinance(tickers=["AAPL", "NVDA"], start="2020-01-01", end="2023-01-01", column="Close")
    sma = SimpleMovingAverageStrategy(_price=data_time_series,
                                      short_window=10,
                                      long_window=10,
                                      amount=100)
    mean_reversion = MeanReversionStrategy(_price=data_time_series,
                                           window=10,
                                           amount=100)


    # Run backtest
    backtest_sma = Backtest(strategy=sma, price=data_time_series)
    backtest_sma.run()
    backtest_mean_reversion = Backtest(strategy=mean_reversion, price=data_time_series)
    backtest_mean_reversion.run()
    # Print results
    print(f"Portfolio Value (SMA):\n{backtest_sma.portfolio}")
    print(f"Cash (SMA):\n{backtest_sma.cash}")

    print(f"Portfolio Value (Mean Reversion):\n{backtest_mean_reversion.portfolio}")
    print(f"Cash (Mean Reversion):\n{backtest_mean_reversion.cash}")



    

if __name__ == "__main__":
    start_time = perf_counter()
    main()

    end_time = perf_counter()
    print(f"Execution time: {end_time - start_time:.2f} seconds \n or {end_time - start_time:.2f} minutes")