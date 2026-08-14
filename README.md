# Online Payment Fraud Detection using Machine Learning

A Flask-based machine-learning demonstration that classifies an online transaction as **potentially fraudulent** or **apparently legitimate** from three transaction features.

> **Important:** This repository uses a reproducible **synthetic dataset** for educational purposes. It is not a production fraud-detection system and its predictions must not be used as the sole basis for real financial decisions.

## Features

- Random Forest classification model
- Reproducible synthetic training data
- Train/test split with stratification
- Precision, recall, F1-score, confusion matrix, and ROC-AUC evaluation
- Flask web interface for interactive predictions
- Input validation and user-friendly error handling
- Fraud-probability display when supported by the trained model

## Tech Stack

- Python 3.10+
- Flask
- NumPy
- Pandas
- Scikit-learn
- HTML/CSS

## Project Structure

```text
online-payment-fraud-detection-ml/
├── app.py                 # Flask application and prediction endpoint
├── model_training.py      # Dataset generation, training, and evaluation
├── model.pkl              # Trained Random Forest model
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Web interface
├── .gitignore             # Local/environment exclusions
└── README.md              # Project documentation
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Jaswanth-36/online-payment-fraud-detection-ml.git
cd online-payment-fraud-detection-ml
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Train the model (optional if `model.pkl` is already present)

```bash
python model_training.py
```

The script creates the synthetic training data, evaluates the model, and saves the trained model as `model.pkl`.

### 5. Start the application

```bash
python app.py
```

Open **http://127.0.0.1:5000** in a browser.

## How It Works

1. The training script creates a reproducible synthetic transaction dataset.
2. Transaction amount and balance features are used as model inputs.
3. The data is split into training and test sets using stratification.
4. A Random Forest classifier is trained and evaluated.
5. The trained model is saved to `model.pkl`.
6. Flask loads the model when the application starts.
7. The web form validates user input and sends the transaction features to the model.
8. The application displays the predicted class and, when available, the model's fraud probability.

## Model Evaluation

The training script reports:

- Precision
- Recall
- F1-score
- Confusion matrix
- ROC-AUC

Accuracy alone is not sufficient for evaluating fraud-detection systems, particularly when fraud classes are imbalanced.

## Limitations

This is a **portfolio/academic demonstration**, not a real banking fraud engine. The labels are generated from an artificial risk rule rather than historical financial transactions. A production system would require a validated real-world dataset, stronger feature engineering, careful class-imbalance treatment, model monitoring, security controls, and domain validation.

## Future Improvements

- Train on a validated real-world fraud dataset
- Add additional transaction and account features
- Compare multiple models and tune hyperparameters
- Add automated tests and CI
- Add authentication and audit logging for a deployed system
- Deploy behind a production WSGI server

## Author

**Neerukattu Jaswanth**  
Machine Learning & AI Enthusiast
