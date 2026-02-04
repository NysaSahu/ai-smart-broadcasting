def compute_sinr(users):
    """
    SINR = Signal / (Interference + Noise)
    """
    SIGNAL_POWER = 1.0
    NOISE = 0.1
    INTERFERENCE_PER_USER = 0.02

    interference = INTERFERENCE_PER_USER * users
    sinr = SIGNAL_POWER / (interference + NOISE)

    return sinr