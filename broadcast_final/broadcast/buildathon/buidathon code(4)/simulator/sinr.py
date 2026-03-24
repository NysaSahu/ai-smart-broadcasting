import numpy as np

def compute_sinr(users, distance_km):
    """
    Compute SINR using Cost-231 Hata Path Loss model (urban macrocell).
    SINR degrades due to both user interference and distance-based path loss.

    Args:
        users (int): Number of active users (interferers)
        distance_km (float): Distance from transmitter to receiver (km)

    Returns:
        float: SINR (linear scale)
    """
    TX_POWER_DBM = 46.0
    NOISE_FLOOR_DBM = -104.0
    INTERFERENCE_COEFF = 0.02

    # Path loss (urban, Cost-231 Hata)
    PL = 128.1 + 37.6 * np.log10(distance_km)
    P_rx = TX_POWER_DBM - PL
    signal_linear = 10 ** (P_rx / 10)

    # Interference and noise (linear)
    interference_linear = INTERFERENCE_COEFF * users
    noise_linear = 10 ** (NOISE_FLOOR_DBM / 10)

    sinr = signal_linear / (interference_linear + noise_linear)
    return sinr