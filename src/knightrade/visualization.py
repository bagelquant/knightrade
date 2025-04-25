"""
Visualization module for KnightTrade

Author: Yanzhong(Eric) Huang
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from knightrade.data import TimeSeries


def plot_time_series(time_series: TimeSeries,
                     pct_y: bool = False,
                     *args,
                     **kwargs) -> Figure:
    """
    Plot a time series.

    :param time_series: TimeSeries object to plot.
    :param pct_y: If True, plot percentage change.
    :param args: Additional arguments for plt.plot.
    """
    fig, ax = plt.subplots()
    data = time_series.data
    ax.plot(data, *args, **kwargs)
    ax.legend(data.columns)

    # set y-axis to percentage
    if pct_y:
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0%}"))

    return fig


def plot_drawdown(time_series: TimeSeries,
                    pct_y: bool = False,
                  *args,
                  **kwargs) -> Figure:
    """
    Plot the drawdown of a time series.

    :param time_series: TimeSeries object to plot.
    :param pct_y: If True, plot percentage change.
    :param args: Additional arguments for plt.plot.
    """
    fig, ax = plt.subplots()

    # Calculate drawdown
    data = time_series.data
    drawdown = data / data.cummax() - 1
    ax.plot(drawdown, *args, **kwargs)
    ax.legend(drawdown.columns)

    if pct_y:
        # set y-axis to percentage
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0%}"))
    return fig


def _test() -> None:
    import pandas as pd
    """Quick test for this module"""
    test_time_series = TimeSeries(
        pd.DataFrame(data={
            "AAPL": [1, 2, 3, 4, 5],
            "MSFT": [5, 4, 3, 2, 1]
        },
            index=pd.date_range(start="2020-01-01", periods=5)
        ))
    # fig = plot_time_series(test_time_series, pct_y=True)
    # fig = plot_drawdown(test_time_series, pct_y=True)
    # plt.show()



if __name__ == "__main__":
    from time import perf_counter

    start = perf_counter()
    _test()
    end = perf_counter()
    print(f"Time cost: {end - start:.2f} s \n or {(end - start) / 60:.2f} min")
