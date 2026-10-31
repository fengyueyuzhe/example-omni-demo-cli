"""Command-line entry point: python -m forecast_cli [--file PATH]."""

from __future__ import annotations

import argparse
from pathlib import Path

from forecast_cli.forecast import format_day, load_forecast

DEFAULT_FILE = Path(__file__).resolve().parents[2] / "data" / "sample_forecast.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="forecast", description="Print a weekly forecast.")
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE, help="forecast JSON file")
    args = parser.parse_args(argv)

    city, days = load_forecast(args.file)
    print(f"{city}: {len(days)}-day forecast")
    for day in days:
        print(format_day(day))
    return 0
