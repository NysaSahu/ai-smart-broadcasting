# decision_engine/ml_decision_engine.py

import numpy as np
import joblib

model = joblib.load("offload_model.pkl")

def decide_delivery_mode_ml(unicast_kpis, atsc_kpis):
    """
    ML-based inference that imitates utility-based AI.
    """

    features = np.array([[
        atsc_kpis["service_continuity"] - unicast_kpis["service_continuity"],
        atsc_kpis["spectrum_efficiency"] - unicast_kpis["spectrum_efficiency"],
        unicast_kpis["congestion"] - atsc_kpis["congestion"]
    ]])

    prediction = model.predict(features)[0]
    return "ATSC" if prediction == 1 else "UNICAST"