from pathlib import Path
import pickle

import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model.pkl"
FEATURE_NAMES = ("amount", "oldbalanceOrg", "newbalanceOrig")


def load_model():
    """Load the trained classifier from the repository root."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "model.pkl was not found. Run 'python -m training.model_training' first."
        )

    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)


def predict_transaction(amount, old_balance, new_balance):
    """Return the predicted class and fraud probability for one transaction."""
    values = (float(amount), float(old_balance), float(new_balance))
    if any(value < 0 for value in values):
        raise ValueError("Transaction values cannot be negative.")

    features = np.array([values], dtype=float)
    model = load_model()
    prediction = int(model.predict(features)[0])

    probability = None
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(features)[0][1]) * 100

    return prediction, probability
