"""
Strategy module for KnightTrade.

This module contains the Strategy class, which is responsible for
defining and executing trading strategies.

output -> position
"""

import pandas as pd

from abc import ABC, abstractmethod
from dataclasses import dataclass
from knightrade.data import TimeSeries


@dataclass(slots=True)
class Strategy(ABC):
    """
    Abstract base class for trading strategies.
    This class defines the interface for all trading strategies.
    """

    price: TimeSeries

    @abstractmethod
    def generate_signals(self) -> TimeSeries:
        """
        abstractmethod: Generate buy/sell signals based on the strategy.
        """
        ... 


@dataclass(slots=True)
class SimpleMovingAverageStrategy(Strategy):
    """
    Simple Moving Average (SMA) strategy.
    This strategy generates buy/sell signals based on the crossing of two moving averages.
    """

    short_window: int
    long_window: int
    amount: float = 1.0
    

    def generate_signals(self) -> TimeSeries:
        """
        Generate buy/sell signals based on the crossing of two moving averages.
        """
        price = self.price.data.copy()
        signals = pd.DataFrame(index=price.index, columns=price.columns)
        # set signals type to float
        signals = signals.astype(float)

        # Calculate short and long moving averages
        short_mavg = price.rolling(window=self.short_window, min_periods=self.short_window).mean().shift(1)
        long_mavg = price.rolling(window=self.long_window, min_periods=self.long_window).mean().shift(1)

        # Generate signals
        signals[price > short_mavg] = self.amount
        signals[price < long_mavg] = -self.amount

        # set signals type to float
        signals = signals.astype(float)
        signals = signals.ffill().fillna(0)
        signals = TimeSeries(signals)
        return signals


@dataclass(slots=True)
class MomentumStrategy(Strategy):
    """
    Momentum strategy.
    This strategy generates buy/sell signals based on the momentum of the price.
    """

    window: int
    amount: float = 1.0

    def generate_signals(self) -> TimeSeries:
        """
        Generate buy/sell signals based on the momentum of the price.
        """
        price = self.price.data.copy()
        signals = pd.DataFrame(index=price.index, columns=price.columns)
        # set signals type to float
        signals = signals.astype(float)

        # Calculate momentum
        momentum = price.pct_change(periods=self.window).shift()

        # Generate signals
        signals[momentum > 0] = self.amount
        signals[momentum < 0] = -self.amount

        signals = signals.ffill().fillna(0)
        return TimeSeries(signals)

        
@dataclass(slots=True)
class MeanReversionStrategy(Strategy):
    """
    Mean Reversion strategy.
    This strategy generates buy/sell signals based on the mean reversion of the price.
    """

    window: int
    amount: float = 1.0

    def generate_signals(self) -> TimeSeries:
        """
        Generate buy/sell signals based on the mean reversion of the price.
        """
        price = self.price.data.copy()
        signals = pd.DataFrame(index=price.index, columns=price.columns)
        # set signals type to float
        signals = signals.astype(float)

        rolling_mean = price.rolling(window=self.window).mean().shift(1)
        rolling_std = price.rolling(window=self.window).std().shift(1)

        # Generate signals
        signals[price < (rolling_mean - rolling_std)] = self.amount
        signals[price > (rolling_mean + rolling_std)] = -self.amount

        signals = signals.ffill().fillna(0)
        return TimeSeries(signals)
    

@dataclass(slots=True)
class BollingerBandsStrategy(Strategy):
    """
    Bollinger Bands strategy.
    This strategy generates buy/sell signals based on the Bollinger Bands.
    """

    window: int
    num_std_dev: float
    amount: float = 1.0

    def generate_signals(self) -> TimeSeries:
        """
        Generate buy/sell signals based on the Bollinger Bands.
        """
        price = self.price.data.copy()
        signals = pd.DataFrame(index=price.index, columns=price.columns)
        # set signals type to float
        signals = signals.astype(float)
        rolling_mean = price.rolling(window=self.window).mean().shift(1)
        rolling_std = price.rolling(window=self.window).std().shift(1)

        # Calculate upper and lower bands
        upper_band = rolling_mean + (self.num_std_dev * rolling_std)
        lower_band = rolling_mean - (self.num_std_dev * rolling_std)

        # Generate signals
        signals[price < lower_band] = self.amount
        signals[price > upper_band] = -self.amount

        signals = signals.ffill().fillna(0)
        return TimeSeries(signals)


@dataclass(slots=True)
class RSIStrategy(Strategy):
    """
    Relative Strength Index (RSI) strategy.
    This strategy generates buy/sell signals based on the RSI.
    """

    window: int
    overbought: float = 70.0
    oversold: float = 30.0
    amount: float = 1.0

    def generate_signals(self) -> TimeSeries:
        """
        Generate buy/sell signals based on the RSI.
        """
        price = self.price.data.copy()
        signals = pd.DataFrame(index=price.index, columns=price.columns)
        # set signals type to float
        signals = signals.astype(float)

        # Calculate RSI
        delta = price.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=self.window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        # Generate signals
        signals[rsi < self.oversold] = self.amount
        signals[rsi > self.overbought] = -self.amount

        signals = signals.ffill().fillna(0)
        return TimeSeries(signals)
