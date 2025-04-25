"""
Handles the data from different sources and formats.

Output:
- Standard data format
"""

import pandas as pd
from pathlib import Path
from knightrade.data.standard_data import TimeSeries, CrossSection
from typing import Literal


def read_csv(path: Path,
             date_col: str,
             output_type: Literal['TimeSeries', 'CrossSection'] = 'TimeSeries') -> TimeSeries | CrossSection:
    """
    Reads a CSV file and returns a TimeSeries or CrossSection object.

    :param path: Path to the CSV file.
    :param date_col: Name of the date column in the CSV file.
    :param output_type: Type of the output object. Can be 'TimeSeries' or 'CrossSection'.
    :return: TimeSeries or CrossSection object.
    """
    try:
        df = pd.read_csv(path, parse_dates=[date_col])
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"File is empty: {path}")
    except pd.errors.ParserError:
        raise ValueError(f"Error parsing file: {path}")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file: {path}. Error: {e}")

    # Check if the date column is in the correct format
    if output_type == 'TimeSeries':
        return TimeSeries(df)
    elif output_type == 'CrossSection':
        return CrossSection(df)
    else:
        raise ValueError("output_type must be 'TimeSeries' or 'CrossSection'")


def read_excel(path: Path,
                sheet_name: str,
                date_col: str,
                output_type: Literal['TimeSeries', 'CrossSection'] = 'TimeSeries') -> TimeSeries | CrossSection:
     """
     Reads an Excel file and returns a TimeSeries or CrossSection object.
    
     :param path: Path to the Excel file.
     :param sheet_name: Name of the sheet in the Excel file.
     :param date_col: Name of the date column in the Excel file.
     :param output_type: Type of the output object. Can be 'TimeSeries' or 'CrossSection'.
     :return: TimeSeries or CrossSection object.
     """
     try:
          df = pd.read_excel(path, sheet_name=sheet_name, parse_dates=[date_col])
     except FileNotFoundError:
          raise FileNotFoundError(f"File not found: {path}")
     except ValueError:
          raise ValueError(f"Sheet not found: {sheet_name} in {path}")
     except Exception as e:
          raise ValueError(f"An error occurred while reading the file: {path}. Error: {e}")
    
     # Check if the date column is in the correct format
     if output_type == 'TimeSeries':
          return TimeSeries(df)
     elif output_type == 'CrossSection':
          return CrossSection(df)
     else:
          raise ValueError("output_type must be 'TimeSeries' or 'CrossSection'")


def read_yfinance(tickers: str | list[str],
                  start: str,
                  end: str, column: str | None = None,
                  output_type: Literal['TimeSeries', 'CrossSection'] = 'TimeSeries') -> TimeSeries | CrossSection:
    """
    Reads data from Yahoo Finance and returns a TimeSeries or CrossSection object.

    :param ticker: Ticker symbol for the stock.
    :param start: Start date for the data.
    :param end: End date for the data.
    :param output_type: Type of the output object. Can be 'TimeSeries' or 'CrossSection'.
    :return: TimeSeries or CrossSection object.
    """
    import yfinance as yf

    try:
        df = yf.download(tickers, start=start, end=end)
    except Exception as e:
        raise ValueError(f"An error occurred while fetching data from Yahoo Finance. Error: {e}")

    if column:
        if column not in df.columns:  # type: ignore
            raise ValueError(f"Column {column} not found in the data.")
        df = df[[column]]  # type: ignore
        df = df.droplevel(0, axis=1)  # type: ignore


    # Check if the date column is in the correct format
    if output_type == 'TimeSeries':
        return TimeSeries(df)  # type: ignore
    elif output_type == 'CrossSection':
        time_series = TimeSeries(df)  # type: ignore
        return time_series.convert_to_cross_section()
    else:
        raise ValueError("output_type must be 'TimeSeries' or 'CrossSection'")


if __name__ == "__main__":
   data = read_yfinance(["AAPL", "NVDA"], "2020-01-01", "2021-01-01", column="Close", output_type='CrossSection')
   print(data)