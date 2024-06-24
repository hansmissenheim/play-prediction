import json
from pathlib import Path

DATA_DIR = Path(__file__).parents[1] / "data"

encodings = None
if (DATA_DIR / "encodings.json").exists():
    with open(DATA_DIR / "encodings.json", "r") as f:
        encodings = json.load(f)
