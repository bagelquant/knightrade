
# Backtest Module Documentation

The `backtest.py` module provides functionality for simulating trading strategies on historical price data. It calculates portfolio performance, including cash and position values, over time.

## Key Components

### `Backtest` Class

The `Backtest` class is the core of this module. It simulates the execution of a trading strategy and tracks portfolio performance.

#### Attributes

- **strategy** (`Strategy`): The trading strategy to be backtested. It generates buy/sell signals.
- **price** (`TimeSeries`): Historical price data for the assets being traded.
- **initial_cash** (`float`): The starting cash balance for the backtest. Default is 1,000,000.
- **portfolio** (`TimeSeries`): The total portfolio value (cash + positions) over time.
- **position** (`TimeSeries`): The position sizes for each asset over time.
- **cash** (`TimeSeries`): The cash balance over time.

#### Methods

- **`__post_init__()`**: Initializes the position attribute by generating signals from the strategy.
- **`run()`**: Executes the backtest by calculating portfolio value and cash balance over time.

### Example Usage

Below is an example of how to use the `Backtest` class:

```python
from knightrade.data.standard_data import TimeSeries
from knightrade.strategy import SimpleMovingAverageStrategy
from knightrade.backtest import Backtest
import pandas as pd

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
```

### Testing

The `_test()` function in `backtest.py` provides a quick way to test the module. It uses sample price data and a simple moving average strategy to demonstrate the backtest process.

### Performance

The module is designed to handle large datasets efficiently. The `TimeSeries` class is used to manage time-indexed data for prices, positions, and cash.

### Future Improvements

- Add support for transaction costs and slippage.
- Include performance metrics such as Sharpe ratio and maximum drawdown.
- Allow for multiple strategies to be tested simultaneously.

## Conclusion

The `backtest.py` module is a powerful tool for evaluating trading strategies. By simulating trades on historical data, it helps traders and developers assess the viability of their strategies before deploying them in live markets.
