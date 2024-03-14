import os
from flask import Flask, render_template, request
from src.pipelines.model_predictor import ModelPredictoripeline

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET"])
def train():
    os.system("python main.py")
    return "Training Succesful"


@app.route("/", methods=["POST", "GET"])
def predict():
    result = None
    if request.method == "POST":
        model_predictor_pipeline = ModelPredictoripeline()
        data = request.form["review"]
        result = (
            "Positive" if model_predictor_pipeline.run(data=data) == 1 else "Negative"
        )
    return render_template("index.html", data=data, result=result)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(host="0.0.0.0", port=8080)
