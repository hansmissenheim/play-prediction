from flask import Flask, render_template, request
from model import MODEL_DIR, PlayPredictionModel
from utils import encodings

app = Flask(__name__)


@app.route("/")
def index():
    if encodings:
        teams = encodings["posteam"]
        coaches = encodings["poscoach"]
    models = [model for model in MODEL_DIR.iterdir() if model.suffix != ".md"]
    models_mapping = {model.stem: model.name for model in sorted(models, reverse=True)}
    return render_template(
        "index.html",
        teams=teams,
        coaches=coaches,
        models=models_mapping,
    )


@app.route("/predict", methods=["POST"])
def predict():
    data = [
        int(request.form.get("drive", 1)),
        int(request.form.get("qtr", 1)),
        int(request.form.get("minutes", 0)) * 60 + int(request.form.get("seconds", 0)),
        int(request.form.get("down", 1)),
        int(request.form.get("ydstogo", 10)),
        int(request.form.get("yardline_100", 75)),
        int(request.form.get("shotgun", 0)),
        int(request.form.get("no_huddle", 0)),
        int(request.form.get("score_differential", 0)),
        float(request.form.get("spread_line", 0.0)),
        int(request.form.get("season", 2023)),
    ]
    xgb = PlayPredictionModel().model
    play_type = xgb.predict([data])
    return "Pass" if play_type[0] == 0 else "Run"


@app.route("/model", methods=["POST"])
def load_model():
    if model_name := request.form.get("model"):
        PlayPredictionModel().load_model(MODEL_DIR / model_name)
    else:
        PlayPredictionModel().load_model()

    return "", 200
