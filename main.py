from time import perf_counter
from src.knightrade import read_yfinance
from src.knightrade import SimpleMovingAverageStrategy, MeanReversionStrategy


def main() -> None:
    """
    Main function to demonstrate the usage of the trading strategies.
    """
    data_time_series = read_yfinance(tickers=["AAPL", "NVDA"], start="2020-01-01", end="2023-01-01", column="Close")
    sma = SimpleMovingAverageStrategy(price=data_time_series,
                                      short_window=10,
                                      long_window=10,
                                      amount=100)
    mean_reversion = MeanReversionStrategy(price=data_time_series,
                                           window=10,
                                           amount=100)

    sma_signals = sma.generate_signals()
    mean_reversion = mean_reversion.generate_signals()
    print(f"SMA signals: {sma_signals}")
    print(f"Mean Reversion signals: {mean_reversion}")
    
    

if __name__ == "__main__":
    start_time = perf_counter()
    main()

    import pandas as pd
    end_time = perf_counter()
    print(f"Execution time: {end_time - start_time:.2f} seconds \n or {end_time - start_time:.2f} minutes")