# Strategy Documentation

## Overview

This document provides an overview of the trading strategies implemented in the `strategy.py` module. Each strategy is designed to generate buy/sell signals based on specific market conditions and indicators.

## Strategies

### Abstract Base Class: `Strategy`

The `Strategy` class is an abstract base class that defines the interface for all trading strategies. It includes the following attributes and methods:

- **Attributes**:
  - `price`: A `TimeSeries` object representing the price data.

- **Methods**:
  - `generate_signals()`: An abstract method that must be implemented by all subclasses to generate buy/sell signals.

### Simple Moving Average Strategy: `SimpleMovingAverageStrategy`

This strategy generates buy/sell signals based on the crossing of two moving averages.

- **Attributes**:
  - `short_window`: The window size for the short moving average.
  - `long_window`: The window size for the long moving average.
  - `amount`: The amount to buy/sell (default is 1.0).

- **Logic**:
  - Buy signals are generated when the price is above the short moving average.
  - Sell signals are generated when the price is below the long moving average.

### Momentum Strategy: `MomentumStrategy`

This strategy generates buy/sell signals based on the momentum of the price.

- **Attributes**:
  - `window`: The window size for calculating momentum.
  - `amount`: The amount to buy/sell (default is 1.0).

- **Logic**:
  - Buy signals are generated when momentum is positive.
  - Sell signals are generated when momentum is negative.

### Mean Reversion Strategy: `MeanReversionStrategy`

This strategy generates buy/sell signals based on the mean reversion of the price.

- **Attributes**:
  - `window`: The window size for calculating the rolling mean and standard deviation.
  - `amount`: The amount to buy/sell (default is 1.0).

- **Logic**:
  - Buy signals are generated when the price is below the rolling mean minus one standard deviation.
  - Sell signals are generated when the price is above the rolling mean plus one standard deviation.

### Bollinger Bands Strategy: `BollingerBandsStrategy`

This strategy generates buy/sell signals based on the Bollinger Bands.

- **Attributes**:
  - `window`: The window size for calculating the rolling mean and standard deviation.
  - `num_std_dev`: The number of standard deviations for the bands.
  - `amount`: The amount to buy/sell (default is 1.0).

- **Logic**:
  - Buy signals are generated when the price is below the lower Bollinger Band.
  - Sell signals are generated when the price is above the upper Bollinger Band.

### Relative Strength Index (RSI) Strategy: `RSI_Strategy`

This strategy generates buy/sell signals based on the Relative Strength Index (RSI).

- **Attributes**:
  - `window`: The window size for calculating RSI.
  - `overbought`: The RSI threshold for overbought conditions (default is 70.0).
  - `oversold`: The RSI threshold for oversold conditions (default is 30.0).
  - `amount`: The amount to buy/sell (default is 1.0).

- **Logic**:
  - Buy signals are generated when the RSI is below the oversold threshold.
  - Sell signals are generated when the RSI is above the overbought threshold.