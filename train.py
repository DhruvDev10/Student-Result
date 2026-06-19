import pandas as pd
import joblib
import os

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

data = (r"H:\Dhruv_intern\Others\Student-Result\students.csv")
df = pd.read_csv(data)

X = df[
    [
        "weekly_study_hours",
        "attendance",
        "participation"
    ]
]
y = df["result"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

model = LogisticRegression(max_iter=1000)
model.fit(X, y_encoded)

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/logistic_model.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")

print("Model trained successfully.")