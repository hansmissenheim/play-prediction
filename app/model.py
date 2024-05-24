from pathlib import Path

from xgboost import XGBClassifier

MODEL_PATH = (
    Path(__file__).parents[1] / "models" / "xgboost_v1_2024-05-16_05-35-56_0.7185.json"
)


class PlayPredictionModel:
    _instance = None
    model: XGBClassifier

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.model = cls.load_model()
        return cls._instance

    @classmethod
    def load_model(cls):
        model = XGBClassifier()
        model.load_model(MODEL_PATH)
        return model
