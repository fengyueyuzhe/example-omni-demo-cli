import unittest

from forecast_cli.cli import DEFAULT_FILE
from forecast_cli.forecast import load_forecast
from forecast_cli.summary import summarize


class SummaryTest(unittest.TestCase):
    def test_summarize_sample(self):
        _, days = load_forecast(DEFAULT_FILE)
        self.assertEqual(summarize(days), "High 14.0°C, low 3.5°C, 3 rainy days")


if __name__ == "__main__":
    unittest.main()
