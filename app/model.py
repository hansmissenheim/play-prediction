from pathlib import Path

from xgboost import XGBClassifier

MODEL_PATH = (
    Path(__file__).parents[1] / "models" / "xgboost_v1_2024-05-16_05-35-56_0.7185.json"
)


def load_model():
    model = XGBClassifier()
    model.load_model(MODEL_PATH)

    return model
