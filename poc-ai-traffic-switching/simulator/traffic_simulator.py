from simulator.users import generate_users
from simulator.network_state import NetworkState


class TrafficSimulator:
    def __init__(self, start_users):
        self.current_users = start_users

    def step(self, change):
        self.current_users += change
        if self.current_users < 0:
            self.current_users = 0

        users = generate_users(self.current_users)
        load = min(1.0, self.current_users / 50)

        return NetworkState(len(users), load)
