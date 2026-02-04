# decision_engine/test_cases.py

from decision_engine import decide_delivery_mode


def test_high_congestion_prefers_atsc():
    unicast_kpis = {
        "service_continuity": 0.85,
        "spectrum_efficiency": 0.40,
        "congestion": 0.85
    }

    atsc_kpis = {
        "service_continuity": 0.80,
        "spectrum_efficiency": 0.75,
        "congestion": 0.30
    }

    decision = decide_delivery_mode(unicast_kpis, atsc_kpis)
    assert decision == "ATSC"


def test_low_load_prefers_unicast():
    unicast_kpis = {
        "service_continuity": 0.90,
        "spectrum_efficiency": 0.65,
        "congestion": 0.20
    }

    atsc_kpis = {
        "service_continuity": 0.75,
        "spectrum_efficiency": 0.50,
        "congestion": 0.40
    }

    decision = decide_delivery_mode(unicast_kpis, atsc_kpis)
    assert decision == "UNICAST"


def test_utility_tradeoff_prefers_atsc():
    """
    Even with lower SINR, ATSC can win due to better
    spectrum efficiency and lower congestion.
    """

    unicast_kpis = {
        "service_continuity": 0.60,
        "spectrum_efficiency": 0.55,
        "congestion": 0.30
    }

    atsc_kpis = {
        "service_continuity": 0.45,
        "spectrum_efficiency": 0.70,
        "congestion": 0.25
    }

    decision = decide_delivery_mode(unicast_kpis, atsc_kpis)
    assert decision == "ATSC"


def test_equal_conditions_defaults_to_unicast():
    unicast_kpis = {
        "service_continuity": 0.70,
        "spectrum_efficiency": 0.60,
        "congestion": 0.40
    }

    atsc_kpis = {
        "service_continuity": 0.70,
        "spectrum_efficiency": 0.60,
        "congestion": 0.40
    }

    decision = decide_delivery_mode(unicast_kpis, atsc_kpis)
    assert decision == "UNICAST"

# Utility-based AI decision model
# U = α·SC + β·SE + γ·(1 − Congestion)
#
# SC  : Service Continuity (probability SINR ≥ SINR_th)
# SE  : Spectrum Efficiency (data_rate / bandwidth)
# Congestion : fraction of occupied network resources
#
# α + β + γ = 1
# Decision emerges by maximizing utility, not by fixed rules.


# Multi-objective optimization: SINR influences decisions but does not dictate them.

if __name__ == "__main__":
    test_high_congestion_prefers_atsc()
    test_low_load_prefers_unicast()
    test_utility_tradeoff_prefers_atsc()
    test_equal_conditions_defaults_to_unicast()

    print("All decision engine test cases passed.")
