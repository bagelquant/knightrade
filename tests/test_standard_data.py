"""
Tests for the standard_data module.
"""

import unittest

import pandas as pd

from src.knightrade.standard_data import TimeSeries, CrossSection


class TestStandardData(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=pd.date_range("2020-01-01", periods=3))

    def test_time_series(self):
        ts = TimeSeries(self.data)

        # test convert_to_cross_section method
        cs = ts.convert_to_cross_section()
        self.assertIsInstance(cs, CrossSection)

    def test_cross_section(self):
        cs = CrossSection(self.data.T)

        # test convert_to_time_series method
        ts = cs.convert_to_time_series()
        self.assertIsInstance(ts, TimeSeries)


if __name__ == "__main__":
    unittest.main(verbosity=2)

