from pathlib import Path
import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42
DATA_SIZE = 5_000
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"


def build_demo_dataset(size=DATA_SIZE):
    """Create a reproducible synthetic dataset for educational demonstration."""
    rng = np.random.default_rng(RANDOM_STATE)

    amount = rng.uniform(10, 10_000, size)
    old_balance = rng.uniform(0, 15_000, size)
    balance_change = rng.uniform(0, np.minimum(amount, old_balance))
    new_balance = np.maximum(old_balance - balance_change, 0)

    # Synthetic risk rule used only to create labels for this demonstration.
    risk_score = (
        (amount > 7_500).astype(int)
        + (balance_change > 6_000).astype(int)
        + ((old_balance - new_balance) > amount * 0.95).astype(int)
    )
    is_fraud = (risk_score >= 2).astype(int)

    return pd.DataFrame(
        {
            "amount": amount,
            "oldbalanceOrg": old_balance,
            "newbalanceOrig": new_balance,
            "isFraud": is_fraud,
        }
    )


def train_model():
    data = build_demo_dataset()

    features = ["amount", "oldbalanceOrg", "newbalanceOrig"]
    X = data[features]
    y = data["isFraud"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=12,
        min_samples_leaf=2,
        class_weight="balanced",
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print("\nModel evaluation")
    print("----------------")
    print(classification_report(y_test, predictions, digits=3))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))
    print(f"ROC-AUC: {roc_auc_score(y_test, probabilities):.3f}")

    with MODEL_PATH.open("wb") as model_file:
        pickle.dump(model, model_file)

    print(f"\nModel saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
