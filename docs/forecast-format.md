# Forecast file format

`forecast_cli` reads a JSON file with a city name and a list of days.

```json
{
  "city": "Seattle",
  "days": [
    {"date": "2026-11-02", "condition": "Light rain", "high_c": 11.5, "low_c": 6.0, "rain_chance": 80}
  ]
}
```

| Field | Type | Notes |
| ----- | ---- | ----- |
| `city` | string | Shown in the header line |
| `days[].date` | string | ISO date, printed as is |
| `days[].condition` | string | Short description, up to 13 characters fit the column |
| `days[].high_c`, `days[].low_c` | number | Temperatures in Celsius |
| `days[].rain_chance` | integer | Percent, 0 to 100 |

See `data/sample_forecast.json` for a full week.
