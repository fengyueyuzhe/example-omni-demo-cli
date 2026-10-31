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


def format_day(day: Day) -> str:
    return (
        f"{day.date}  {day.condition:<13}"
        f"{day.high_c:>5.1f}°C / {day.low_c:>5.1f}°C   rain {day.rain_chance:>3}%"
    )
