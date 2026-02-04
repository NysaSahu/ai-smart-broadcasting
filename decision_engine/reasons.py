# decision_engine/reasons.py

def explain_decision(unicast_kpis, atsc_kpis, utility_unicast, utility_atsc):
    """
    Explainable AI output for decision transparency.
    """
    return {
        "utility_unicast": round(utility_unicast, 3),
        "utility_atsc": round(utility_atsc, 3),
        "selected": "ATSC" if utility_atsc > utility_unicast else "UNICAST",
        "metrics": {
            "unicast": unicast_kpis,
            "atsc": atsc_kpis
        }
    }
