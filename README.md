# 🛡️ Online Payment Fraud Detection using Machine Learning

A professional Flask + Machine Learning demonstration that analyzes online payment transaction details and classifies them as **potentially fraudulent** or **apparently legitimate**.

> **Important:** The current model is trained on a reproducible **synthetic dataset** created for an academic/portfolio demonstration. The sample transactions below are realistic usage examples, but they are **not real customer transactions**. This project must not be used as the sole basis for real financial decisions.

## ✨ What the Project Does

The application takes three transaction values:

1. **Transaction Amount** — amount being transferred.
2. **Original Balance** — account balance before the transaction.
3. **New Balance** — account balance after the transaction.

A trained Random Forest classifier analyzes these values and returns:

- 🟢 **Transaction Appears Legitimate**, or
- 🔴 **Potentially Fraudulent Transaction**
- An estimated **fraud probability** when supported by the model.

## 🖥️ Browser Experience

The application opens as a modern dark dashboard with:

- Responsive layout for desktop and mobile
- Transaction input cards
- Currency-aware amount fields
- Model-ready status indicator
- Clear success/fraud result panels
- Fraud probability display
- Input validation and helpful error messages
- Sample transaction values for quick testing

## 🧠 Machine Learning Workflow

```text
Synthetic Transaction Data
          ↓
Data Preparation
          ↓
Train / Test Split
          ↓
Random Forest Classifier
          ↓
Model Evaluation
          ↓
model.pkl
          ↓
Flask Web Application
          ↓
User Transaction Input
          ↓
Prediction + Fraud Probability
```

## 📂 Professional Project Structure

```text
online-payment-fraud-detection-ml/
│
├── app/
│   ├── __init__.py
│   ├── app.py                 # Flask routes and web application
│   ├── templates/
│   │   └── index.html         # Browser interface
│   └── static/
│       └── style.css          # Responsive dashboard styling
│
├── model/
│   ├── __init__.py
│   └── model.py               # Model loading and prediction service
│
├── training/
│   ├── __init__.py
│   └── model_training.py      # Dataset generation and model training
│
├── requirements/
│   └── requirements.txt       # Python dependencies
│
├── model.pkl                  # Trained Random Forest model
├── run.py                     # Simple application entry point
├── .gitignore
└── README.md
```

## ⚙️ Run the Project on Windows

### 1. Clone the repository

```powershell
git clone https://github.com/Jaswanth-36/online-payment-fraud-detection-ml.git
cd online-payment-fraud-detection-ml
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements/requirements.txt
```

### 4. Train / regenerate the model

Run this whenever you want to regenerate `model.pkl` from the current training code:

```powershell
python -m training.model_training
```

Example terminal output:

```text
=== Online Payment Fraud Detection | Model Evaluation ===
              precision    recall  f1-score   support

           0      ...       ...       ...       ...
           1      ...       ...       ...       ...

Confusion matrix:
[[... ...]
 [... ...]]
ROC-AUC: ...

Model saved successfully: ...\model.pkl
```

The exact evaluation numbers can change if the training process or dataset is changed.

### 5. Start the web application

```powershell
python run.py
```

You should see:

```text
 * Running on http://127.0.0.1:5000
```

Open this address in Chrome or another browser:

**http://127.0.0.1:5000**

### 6. Stop the application

Return to the terminal and press:

```text
Ctrl + C
```

## 🧪 Sample Transactions and Expected Demonstration Outputs

These examples show how the application can be tested. They are **demonstration scenarios**, not real banking records.

### Example 1 — Normal-looking transaction

| Field | Value |
|---|---:|
| Transaction Amount | ₹5,000 |
| Original Balance | ₹10,000 |
| New Balance | ₹5,000 |

Typical result from the current trained demonstration model:

```text
Transaction Appears Legitimate
Estimated fraud probability: approximately 3%
```

### Example 2 — High-risk demonstration transaction

| Field | Value |
|---|---:|
| Transaction Amount | ₹9,000 |
| Original Balance | ₹10,000 |
| New Balance | ₹1,000 |

Typical result from the current trained demonstration model:

```text
Potentially Fraudulent Transaction
Estimated fraud probability: approximately 95%
```

### Example 3 — Small transaction

| Field | Value |
|---|---:|
| Transaction Amount | ₹200 |
| Original Balance | ₹5,000 |
| New Balance | ₹4,800 |

Typical result:

```text
Transaction Appears Legitimate
```

> The probability shown in the browser is model-dependent. If you retrain the model, the exact probability may change.

## 🌐 What Happens in the Browser

When you open the application, you will see:

```text
┌───────────────────────────────────────────────┐
│ 🛡️ FraudGuard ML                             │
│                                               │
│       Online Payment Fraud Detection          │
│ Analyze transaction details with ML           │
│                                               │
│  TRANSACTION ANALYSIS       ● Model Ready     │
│                                               │
│  Transaction Amount     Original Balance      │
│  ₹ [ 5000             ] ₹ [ 10000          ] │
│                                               │
│  New Balance                                │
│  ₹ [ 5000             ]                     │
│                                               │
│  [       Analyze Transaction            → ]  │
│                                               │
│  ✓ MODEL RESULT                               │
│  Transaction Appears Legitimate               │
│  Estimated fraud probability: 2.95%           │
└───────────────────────────────────────────────┘
```

For a fraud prediction, the result card changes to a warning style and displays:

```text
⚠  MODEL RESULT
   Potentially Fraudulent Transaction
   Estimated fraud probability: 95.13%
```

## 🔍 How the Code Is Organized

### `app/app.py`

Handles the Flask web application and `/predict` endpoint. It receives form values, validates them, calls the model service, and sends the result back to the browser.

### `model/model.py`

Contains the reusable model-loading and prediction logic. This keeps machine-learning logic separate from the Flask web layer.

### `training/model_training.py`

Creates the reproducible demonstration dataset, trains the Random Forest model, evaluates it, and saves `model.pkl`.

### `app/templates/index.html`

Contains the user-facing browser interface.

### `app/static/style.css`

Contains the responsive visual design, dashboard layout, result cards, buttons, forms, and mobile styling.

### `requirements/requirements.txt`

Lists the Python packages required to install and run the project.

## 📊 Model Evaluation

The training script reports:

- Precision
- Recall
- F1-score
- Confusion matrix
- ROC-AUC

These metrics provide more useful information than accuracy alone for fraud-detection problems.

## 🔐 Input Validation

The application rejects:

- Empty required fields
- Non-numeric transaction values
- Negative amounts
- Negative balances
- Missing model files

Instead of showing a Python traceback in the browser, the user receives a clear error message.

## ⚠️ Current Model Limitation

This project deliberately uses a synthetic dataset. The fraud labels are generated using an artificial demonstration risk rule rather than historical banking data.

Therefore:

- High probability does **not** mean a real transaction is actually fraudulent.
- The model is suitable for demonstrating an end-to-end ML application.
- It is not suitable for deployment in a real bank, payment gateway, or financial institution without substantial validation and redesign.

## 🚀 Future Improvements

- Replace synthetic data with a validated real-world fraud dataset.
- Add transaction type, location, device, time and account-history features.
- Handle severe class imbalance using validated techniques.
- Compare Logistic Regression, Random Forest, XGBoost and other models.
- Add automated unit and integration tests.
- Add authentication and audit logging.
- Add model versioning and monitoring.
- Deploy using a production WSGI server and secure HTTPS configuration.

## 👨‍💻 Author

**Neerukattu Jaswanth**  
Machine Learning & AI Enthusiast

## ⭐ Project Goal

This project demonstrates how a machine-learning model can be connected to a user-friendly Flask application to create an end-to-end prediction system—from **data generation and model training to browser-based prediction and result visualization**.
