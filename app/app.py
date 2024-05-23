from flask import Flask, render_template, request
from model import load_model

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = [
        int(request.form.get("drive", 1)),
        int(request.form.get("qtr", 1)),
        int(request.form.get("quarter_seconds_remaining", 900)),
        int(request.form.get("down", 1)),
        int(request.form.get("ydstogo", 10)),
        int(request.form.get("yardline_100", 75)),
        int(request.form.get("shotgun", 0)),
        int(request.form.get("no_huddle", 0)),
        int(request.form.get("score_differential", 0)),
        float(request.form.get("spread_line", 0.0)),
        int(request.form.get("season", 2023)),
    ]
    xgb = load_model()
    play_type = xgb.predict([data])

    return "Pass" if play_type[0] == 0 else "Run"
