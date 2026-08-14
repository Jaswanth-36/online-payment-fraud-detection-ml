from pathlib import Path
import pickle

import numpy as np
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"

app = Flask(__name__)

# Load the trained model once when the application starts.
try:
    with MODEL_PATH.open("rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError as exc:
    raise RuntimeError(
        "model.pkl was not found. Run 'python model_training.py' first."
    ) from exc


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        amount = float(request.form["amount"])
        old_balance = float(request.form["oldbalanceOrg"])
        new_balance = float(request.form["newbalanceOrig"])

        values = (amount, old_balance, new_balance)
        if any(value < 0 for value in values):
            raise ValueError("Transaction values cannot be negative.")

        features = np.array([[amount, old_balance, new_balance]], dtype=float)
        prediction = int(model.predict(features)[0])

        probability = None
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(features)[0][1]) * 100

        if prediction == 1:
            result = "Fraudulent Transaction Detected"
            result_type = "danger"
        else:
            result = "Transaction Appears Legitimate"
            result_type = "success"

        return render_template(
            "index.html",
            prediction_text=result,
            result_type=result_type,
            probability=probability,
            form_data={
                "amount": amount,
                "oldbalanceOrg": old_balance,
                "newbalanceOrig": new_balance,
            },
        )

    except (KeyError, TypeError, ValueError):
        return render_template(
            "index.html",
            error="Please enter valid non-negative numeric values for all fields.",
            form_data=request.form,
        ), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
