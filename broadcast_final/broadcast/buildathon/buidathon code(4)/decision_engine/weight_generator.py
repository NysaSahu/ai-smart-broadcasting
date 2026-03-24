"""
Context-aware MBOS dynamic weighting for stability and proactive offloading.
Implements dynamic AI weights (alpha, beta, gamma) based on real-time network context.
"""

def generate_dynamic_weights(hour, redundancy_factor, user_count):
    """
    Generate dynamic weights for MBOS decision engine based on network context.
    Args:
        hour (int): Current hour (0-23).
        redundancy_factor (float): Network redundancy factor (0.0-1.0).
        user_count (int): Number of active users.
    Returns:
        dict: Weights for alpha, beta, gamma. Keys: {'alpha', 'beta', 'gamma'}; values sum to 1.0.
    """
    # Default balanced weights
    weights = {'alpha': 0.33, 'beta': 0.33, 'gamma': 0.34}

    if 19 <= hour <= 23 and user_count > 50:
        # Prioritize congestion relief
        weights = {'alpha': 0.2, 'beta': 0.2, 'gamma': 0.6}
    elif redundancy_factor > 0.9:
        # Prioritize service continuity
        weights = {'alpha': 0.7, 'beta': 0.2, 'gamma': 0.1}
    elif 8 <= hour <= 17:
        # Prioritize spectrum efficiency
        weights = {'alpha': 0.25, 'beta': 0.5, 'gamma': 0.25}

    # Ensure weights sum to 1.0 (floating point correction)
    total = sum(weights.values())
    for k in weights:
        weights[k] = round(weights[k] / total, 2)
    # Final correction for floating point rounding
    diff = 1.0 - sum(weights.values())
    if diff != 0:
        # Adjust gamma to ensure sum is exactly 1.0
        weights['gamma'] = round(weights['gamma'] + diff, 2)
    return weights
