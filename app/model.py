from pathlib import Path

from xgboost import XGBClassifier

MODEL_DIR = Path(__file__).parents[1] / "models"
LATEST_MODEL = sorted(MODEL_DIR.iterdir())[-1]


class PlayPredictionModel:
    _instance = None
    model: XGBClassifier

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.model = cls.load_model()
        return cls._instance

    @classmethod
    def load_model(cls, model_path: Path | None = None):
        if model_path is None:
            model_path = LATEST_MODEL

        model = XGBClassifier()
        model.load_model(model_path)
        return model
