# decision_engine/decision_engine.py

def compute_utility(
    service_continuity,
    spectrum_efficiency,
    congestion,
    alpha=None,
    beta=None,
    gamma=None
):
    """
    Utility-based AI decision function.

    U = α·SC + β·SE + γ·(1 − Congestion)

    - SC  : Service Continuity (probability SINR ≥ threshold)
    - SE  : Spectrum Efficiency (normalized)
    - Congestion : normalized [0,1]

    If α, β, γ are not provided, defaults are used
    for backward compatibility.
    """

    # 🔹 Default weights (legacy-safe)
    if alpha is None or beta is None or gamma is None:
        alpha, beta, gamma = 0.4, 0.4, 0.2

    # 🔹 Safety normalization (just in case)
    total = alpha + beta + gamma
    if total != 1.0:
        alpha /= total
        beta /= total
        gamma /= total

    utility = (
        alpha * service_continuity +
        beta * spectrum_efficiency +
        gamma * (1 - congestion)
    )

    return utility


def decide_delivery_mode(
    unicast_kpis,
    atsc_kpis,
    weights=None
):
    """
    Decide delivery mode by maximizing utility.

    Parameters:
    - unicast_kpis : dict with keys
        ['service_continuity', 'spectrum_efficiency', 'congestion']
    - atsc_kpis : same structure as unicast_kpis
    - weights : optional dict {'alpha','beta','gamma'}
        → enables dynamic AI weights
    """

    # 🔹 Extract dynamic weights if provided
    if weights:
        alpha = weights.get("alpha")
        beta = weights.get("beta")
        gamma = weights.get("gamma")
    else:
        alpha = beta = gamma = None

    utility_unicast = compute_utility(
        service_continuity=unicast_kpis["service_continuity"],
        spectrum_efficiency=unicast_kpis["spectrum_efficiency"],
        congestion=unicast_kpis["congestion"],
        alpha=alpha,
        beta=beta,
        gamma=gamma
    )

    utility_atsc = compute_utility(
        service_continuity=atsc_kpis["service_continuity"],
        spectrum_efficiency=atsc_kpis["spectrum_efficiency"],
        congestion=atsc_kpis["congestion"],
        alpha=alpha,
        beta=beta,
        gamma=gamma
    )

    # 🔹 Decision rule
    # ATSC   → Offload (Unicast → Broadcast)
    # UNICAST → Onload (Broadcast → Unicast)
    return "ATSC" if utility_atsc > utility_unicast else "UNICAST"