import json
from pathlib import Path

DATA_DIR = Path(__file__).parents[1] / "data"

encodings = None
if (DATA_DIR / "encodings.json").exists():
    with open(DATA_DIR / "encodings.json", "r") as f:
        encodings = json.load(f)


def betting_odds(probability: float) -> int:
    if probability > 0.5:
        return round(-100 * (probability / (1 - probability)))
    else:
        return round(100 * ((1 - probability) / probability))
