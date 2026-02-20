# 💳 Online Payment Fraud Detection using Machine Learning

## 📌 Project Overview

This project is a Machine Learning-based web application that detects fraudulent online payment transactions.  
It uses a Random Forest Classifier to classify transactions as **Fraudulent** or **Legitimate** based on transaction details.

The system is built using:
- Python
- Scikit-learn
- Flask
- Pandas
- NumPy

---

## 🚀 Features

- 🔍 Fraud detection using ML model
- 🌐 Simple Flask web interface
- 🧠 Random Forest Classifier
- 📊 Synthetic dataset generation
- ⚡ Real-time prediction

---

## 🛠 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML

---

## 📂 Project Structure

online_payment_fraud_detection/
│
├── app.py # Flask web app
├── model_training.py # Model training script
├── model.pkl # Trained ML model (generated after training)
├── requirements.txt # Required libraries
├── .gitignore
└── templates/
└── index.html # Web UI


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/online-payment-fraud-detection-ml.git
cd online-payment-fraud-detection-ml


---

### 2️⃣ Install Dependencies

pip install -r requirements.txt


---

### 3️⃣ Train the Model

python model_training.py


This will create:

model.pkl


---

### 4️⃣ Run the Flask App

python app.py


Open your browser:

http://127.0.0.1:5000


---

## 📊 Machine Learning Model

- Algorithm: **Random Forest Classifier**
- Train-Test Split: 80-20
- Input Features:
  - Transaction Amount
  - Old Balance
  - New Balance
- Output:
  - 0 → Legitimate
  - 1 → Fraudulent

---

## 🧠 How It Works

1. User enters transaction details.
2. Data is sent to Flask backend.
3. Model predicts fraud probability.
4. Result is displayed on the webpage.

---

## 🔮 Future Improvements

- Use real-world dataset (Kaggle Fraud Detection Dataset)
- Add model accuracy metrics
- Add confusion matrix visualization
- Deploy on Render / Heroku / AWS
- Add user authentication system

---

## 👨‍💻 Author

NEERUKATTU JASWANTH  
Machine Learning & AI Enthusiast  

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
