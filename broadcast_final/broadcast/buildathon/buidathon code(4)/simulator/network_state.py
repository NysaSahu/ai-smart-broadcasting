class NetworkState:
    """
    Stores time-evolving network state, SINR history, and user distance.
    Now supports distance-aware SINR for physics-based modeling.
    """

    def __init__(self):
        self.popularity = 0.4
        self.sinr_linear = 10 ** (15 / 10)
        self.congestion = 0.0
        self.distance_km = 1.0
        self.sinr_history = []
        self.distance_history = []

    def get_state(self):
        return self.popularity, self.sinr_linear, self.congestion, self.distance_km

    def update_state(self, popularity, sinr_linear, congestion, distance_km):
        self.popularity = popularity
        self.sinr_linear = sinr_linear
        self.congestion = congestion
        self.distance_km = distance_km
        self.sinr_history.append(sinr_linear)
        self.distance_history.append(distance_km)

    def compute_service_continuity(self, sinr_threshold):
        """
        SC = Pr(SINR >= SINR_th)
        """
        if not self.sinr_history:
            return 0.0
        success = sum(
            1 for s in self.sinr_history if s >= sinr_threshold
        )
        return success / len(self.sinr_history)