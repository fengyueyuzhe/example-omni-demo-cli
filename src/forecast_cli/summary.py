"""Summarize a forecast in one line: python -m forecast_cli.summary."""

from __future__ import annotations

from forecast_cli.forecast import Day, load_forecast


def summarize(days: list[Day], rain_threshold: int = 50) -> str:
    high = max(day.high_c for day in days)
    low = min(day.low_c for day in days)
    rainy = sum(1 for day in days if day.rain_chance >= rain_threshold)
    return f"High {high:.1f}°C, low {low:.1f}°C, {rainy} rainy days"


if __name__ == "__main__":
    from forecast_cli.cli import DEFAULT_FILE

    _, days = load_forecast(DEFAULT_FILE)
    print(summarize(days))
