import io
import unittest
from contextlib import redirect_stdout

from forecast_cli.cli import DEFAULT_FILE, main
from forecast_cli.forecast import format_day, load_forecast


class ForecastTest(unittest.TestCase):
    def test_load_sample(self):
        city, days = load_forecast(DEFAULT_FILE)
        self.assertEqual(city, "Seattle")
        self.assertEqual(len(days), 7)

    def test_format_day(self):
        _, days = load_forecast(DEFAULT_FILE)
        line = format_day(days[0])
        self.assertIn("2026-11-02", line)
        self.assertIn("11.5°C", line)
        self.assertIn("rain  80%", line)

    def test_cli_prints_header_and_days(self):
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(main([]), 0)
        lines = out.getvalue().splitlines()
        self.assertEqual(lines[0], "Seattle: 7-day forecast")
        self.assertEqual(len(lines), 8)


if __name__ == "__main__":
    unittest.main()
