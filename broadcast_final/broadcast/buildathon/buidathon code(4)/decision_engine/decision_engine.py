# decision_engine/decision_engine.py

def compute_utility(
    service_continuity,
    spectrum_efficiency,
    congestion,
    alpha,
    beta,
    gamma
):
    """
    Utility-based AI decision function for MBOS.
    Implements context-aware dynamic weighting for stability and proactive offloading.

    U = α·SC + β·SE + γ·(1 − Congestion)

    Args:
        service_continuity (float): Probability SINR ≥ threshold
        spectrum_efficiency (float): Normalized spectrum efficiency
        congestion (float): Normalized congestion [0,1]
        alpha (float): Service continuity weight
        beta (float): Spectrum efficiency weight
        gamma (float): Congestion relief weight

    Returns:
        float: Utility value
    """
    utility = (
        alpha * service_continuity +
        beta * spectrum_efficiency +
        gamma * (1 - congestion)
    )
    return utility


def decide_delivery_mode(
    unicast_kpis,
    atsc_kpis,
    weights
):
    """
    Decide delivery mode by maximizing utility.
    Implements context-aware MBOS dynamic weighting for stability and proactive offloading.

    Args:
        unicast_kpis (dict): {'service_continuity', 'spectrum_efficiency', 'congestion'}
        atsc_kpis (dict): Same structure as unicast_kpis
        weights (dict): Mandatory. {'alpha','beta','gamma'}; values must sum to 1.0

    Returns:
        str: 'unicast' or 'atsc' based on utility maximization
    """
    alpha = weights['alpha']
    beta = weights['beta']
    gamma = weights['gamma']

    unicast_utility = compute_utility(
        unicast_kpis['service_continuity'],
        unicast_kpis['spectrum_efficiency'],
        unicast_kpis['congestion'],
        alpha,
        beta,
        gamma
    )
    atsc_utility = compute_utility(
        atsc_kpis['service_continuity'],
        atsc_kpis['spectrum_efficiency'],
        atsc_kpis['congestion'],
        alpha,
        beta,
        gamma
    )
    return 'unicast' if unicast_utility >= atsc_utility else 'atsc'
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