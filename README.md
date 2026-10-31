# example-omni-demo-cli

Print a weekly weather forecast from a JSON file in the terminal.

## Run

```bash
PYTHONPATH=src python -m forecast_cli
PYTHONPATH=src python -m forecast_cli --file path/to/forecast.json
```

## Examples

```text
$ PYTHONPATH=src python -m forecast_cli
Seattle: 7-day forecast
2026-11-02  Light rain    11.5°C /   6.0°C   rain  80%
2026-11-03  Cloudy        12.0°C /   5.5°C   rain  30%
...
```

Point `--file` at any JSON file with a `city` and a list of `days`, shaped like
`data/sample_forecast.json`.

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests
```
