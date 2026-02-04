import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

MODEL_PATH = "decision_engine/congestion_model.pkl"

FEATURES = ["users", "hour", "is_night", "redundancy", "sinr_linear"]

def train_congestion_model(csv_path="simulation_dataset.csv"):
    if not os.path.exists(csv_path):
        raise FileNotFoundError("Dataset not found")

    data = pd.read_csv(csv_path)

    # Backward compatibility
    if "redundancy" not in data:
        data["redundancy"] = 0.5
    if "sinr_linear" not in data:
        data["sinr_linear"] = 1.0

    data["is_night"] = data["hour"].apply(
        lambda h: 1 if h >= 20 or h <= 6 else 0
    )

    X = data[FEATURES]
    y = data["congestion"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("✅ Congestion AI model trained")


def predict_congestion(users, hour, redundancy=0.5, sinr_linear=1.0):
    is_night = 1 if hour >= 20 or hour <= 6 else 0

    X = pd.DataFrame([{
        "users": users,
        "hour": hour,
        "is_night": is_night,
        "redundancy": redundancy,
        "sinr_linear": sinr_linear
    }])

    model = joblib.load(MODEL_PATH)
    pred = model.predict(X)[0]

    return max(0.0, min(1.0, pred))


if __name__ == "__main__":
    train_congestion_model("simulation_dataset.csv")
    print("Test prediction:",
          predict_congestion(users=120, hour=21, redundancy=0.9, sinr_linear=0.8))