class NetworkState:
    """
    Stores time-evolving network state and SINR history.
    """

    def __init__(self):
        self.popularity = 0.4
        self.sinr_linear = 10 ** (15 / 10)
        self.congestion = 0.0
        self.sinr_history = []

    def get_state(self):
        return self.popularity, self.sinr_linear, self.congestion

    def update_state(self, popularity, sinr_linear, congestion):
        self.popularity = popularity
        self.sinr_linear = sinr_linear
        self.congestion = congestion
        self.sinr_history.append(sinr_linear)

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