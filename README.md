# 💳 Online Payment Fraud Detection using Machine Learning

## 🎓 Major Final Year Project

This project is a Machine Learning-based system designed to detect fraudulent online payment transactions.  
It analyzes transaction features and predicts whether a transaction is **Legitimate** or **Fraudulent** using advanced ML algorithms.

The system also includes a Flask-based web application for real-time predictions.

---

## 📌 Problem Statement

Online payment systems are highly vulnerable to fraudulent transactions.  
Detecting fraud accurately is challenging due to:

- Highly imbalanced datasets
- Large transaction volumes
- Real-time processing requirements

This project builds a reliable fraud detection model using Machine Learning techniques.

---

## 🚀 Features

- 🔍 Fraud detection using ML algorithms
- 📊 Handles imbalanced datasets
- 📈 Model performance evaluation (Precision, Recall, F1-score, ROC-AUC)
- 🌐 Web interface using Flask
- ⚡ Real-time transaction prediction
- 📂 Clean project structure
- 📉 Data visualization & analysis

---

## 🛠 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- HTML & CSS

---

## 📊 Machine Learning Models Used

- Logistic Regression
- Random Forest Classifier
- (Optional) XGBoost
- SMOTE (for handling class imbalance)

---

## 📂 Project Structure

fraud_detection_major_project/
│
├── app.py # Flask web application
├── train_model.py # Model training script
├── models/
│ └── fraud_model.pkl # Trained model
├── templates/
│ └── index.html # Web interface
├── static/
│ └── styles.css
├── data/
│ └── creditcard.csv
├── requirements.txt
└── README.md


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

python train_model.py


This will generate:

fraud_model.pkl


---

### 4️⃣ Run the Web Application

python app.py


Open browser:

http://127.0.0.1:5000


---

## 📈 Model Evaluation Metrics

Since fraud detection datasets are highly imbalanced, we use:

- Confusion Matrix
- Precision
- Recall
- F1-Score
- ROC-AUC Score

> Accuracy alone is not reliable for fraud detection problems.

---

## 🧠 How It Works

1. Dataset is preprocessed and cleaned.
2. Data is split into training and testing sets.
3. ML model is trained on transaction features.
4. Model is evaluated using advanced metrics.
5. Trained model is integrated into Flask app.
6. User enters transaction details.
7. System predicts fraud probability.

---

## 🔮 Future Improvements

- Deploy on AWS / Render / Heroku
- Integrate real-time API-based fraud detection
- Add Deep Learning models
- Build interactive dashboard
- Add user authentication system

---

## 📚 Applications

- Banking Systems
- E-commerce Platforms
- Online Payment Gateways
- Financial Institutions

---

## 👨‍💻 Author

**Neerukattu Jaswanth**  
Final Year B.Tech Student  
Machine Learning & AI Enthusiast  

---

## ⭐ Support

If you find this project useful, please give it a ⭐ on GitHub!
