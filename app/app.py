from flask import Flask, render_template, request

from model.model import predict_transaction

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/predict")
def predict():
    form_data = request.form.to_dict()

    try:
        amount = float(form_data["amount"])
        old_balance = float(form_data["oldbalanceOrg"])
        new_balance = float(form_data["newbalanceOrig"])

        if any(value < 0 for value in (amount, old_balance, new_balance)):
            raise ValueError("Negative values are not allowed.")

        prediction, probability = predict_transaction(
            amount, old_balance, new_balance
        )

        if prediction == 1:
            result = "Potentially Fraudulent Transaction"
            result_class = "danger"
        else:
            result = "Transaction Appears Legitimate"
            result_class = "success"

        return render_template(
            "output.html",
            prediction_text=result,
            result_class=result_class,
            probability=probability,
            amount=amount,
            old_balance=old_balance,
            new_balance=new_balance,
        )

    except (KeyError, TypeError, ValueError, FileNotFoundError) as exc:
        if isinstance(exc, FileNotFoundError):
            message = str(exc)
        else:
            message = "Please enter valid non-negative numbers in all fields."

        return render_template(
            "index.html", error=message, form_data=form_data
        ), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
