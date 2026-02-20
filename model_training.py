
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Create synthetic dataset
np.random.seed(42)
data_size = 5000

data = pd.DataFrame({
    "amount": np.random.uniform(10, 10000, data_size),
    "oldbalanceOrg": np.random.uniform(0, 10000, data_size),
    "newbalanceOrig": np.random.uniform(0, 10000, data_size),
    "isFraud": np.random.randint(0, 2, data_size)
})

X = data[["amount", "oldbalanceOrg", "newbalanceOrig"]]
y = data["isFraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved as model.pkl")
