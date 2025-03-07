"""
Standard data class

Standard Data Object is a class that provides a standard data structure for the project. It is a simple wrapper around `pandas.DataFrame` with some additional methods. It is used to ensure the data is in a consistent format. Especially for type hinting and data manipulation.

"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from pandas import DataFrame, DatetimeIndex


@dataclass(slots=True)
class StandardData(ABC):

    data: DataFrame

    def __post_init__(self):
        self._check_data()

    @abstractmethod
    def _check_data(self):
        """Check if the data is in the correct format, otherwise raise an error."""
        pass


@dataclass(slots=True)
class TimeSeries(StandardData):

    def _check_data(self):
        if not isinstance(self.data.index, DatetimeIndex):
            raise ValueError("Index must be a timestamp.")

    def convert_to_cross_section(self) -> "CrossSection":
        return CrossSection(self.data.T)


@dataclass(slots=True)
class CrossSection(StandardData):

    def _check_data(self):
        if not isinstance(self.data.columns, DatetimeIndex):
            raise ValueError("Columns must be a timestamp.")

    def convert_to_time_series(self) -> "TimeSeries":
        return TimeSeries(self.data.T)

