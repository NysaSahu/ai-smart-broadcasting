import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

MODEL_PATH = "decision_engine/congestion_model.pkl"


def train_congestion_model(csv_path="congestion_dataset.csv"):
    if not os.path.exists(csv_path):
        raise FileNotFoundError("congestion_dataset.csv not found")

    data = pd.read_csv(csv_path)

    X = data[["users", "hour", "is_night"]]
    y = data["congestion"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("✅ Congestion AI model trained")


def predict_congestion(users, hour):
    is_night = 1 if hour >= 20 or hour <= 6 else 0

    model = joblib.load(MODEL_PATH)
    pred = model.predict([[users, hour, is_night]])[0]

    return max(0.0, min(1.0, pred))  # clamp to [0,1]


# 🔹 OPTIONAL TEST (keep this)
if __name__ == "__main__":
    # run after training
    print("Predicted congestion:",
          predict_congestion(users=120, hour=21))