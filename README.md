# example-omni-demo-cli

Print a weekly weather forecast from a JSON file in the terminal.

## Run

```bash
PYTHONPATH=src python -m forecast_cli
PYTHONPATH=src python -m forecast_cli --file path/to/forecast.json
```

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests
```
