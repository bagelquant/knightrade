# Data Handler

Provide a easy interface to convert data from different sources to a [standard data object](standard_data.md).

Data source:
- local file
    - `pandas.DataFrame`
    - `.csv` file
    - `.json` file
    - `.xlsx` file
- remote file
    - `yahoo finance`

This module is a function-based module, all functions are stateless and could be used independently.

## Usage

```python
from pathlib import Path
from knightrade.data import read_csv, read_yahoo

# local file
cross_section = read_csv(path=Path("data.csv"),  
                         date_col="trade_date",
                         output="CrossSection")   

# remote file

time_series = read_yahoo(ticker="AAPL",
                         start_date=start_date,
                         end_date=end_date,
                         output="TimeSeries")
```

## Functions

- `read_pd`
- `read_csv`
- `read_json`
- `read_excel`
- `read_yahoo`

