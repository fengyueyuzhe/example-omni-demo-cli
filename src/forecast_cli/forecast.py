"""Load a forecast file and format each day for the terminal."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Day:
    date: str
    condition: str
    high_c: float
    low_c: float
    rain_chance: int


def load_forecast(path: Path) -> tuple[str, list[Day]]:
    data = json.loads(Path(path).read_text())
    return data["city"], [Day(**day) for day in data["days"]]


def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def format_day(day: Day, units: str = "c") -> str:
    if units == "f":
        high, low, unit = to_fahrenheit(day.high_c), to_fahrenheit(day.low_c), "°F"
    else:
        high, low, unit = day.high_c, day.low_c, "°C"
    return (
        f"{day.date}  {day.condition:<13}"
        f"{high:>5.1f}{unit} / {low:>5.1f}{unit}   rain {day.rain_chance:>3}%"
    )
