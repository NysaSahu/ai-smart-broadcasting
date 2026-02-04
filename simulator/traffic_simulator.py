from simulator.users import generate_users
from simulator.perturbations import apply_perturbations
from simulator.network_state import NetworkState
from simulator.content import generate_content_request
from simulator.sinr import compute_sinr
from datetime import datetime

USER_RATE_Mbps = 0.5
TOTAL_CAPACITY_Mbps = 50
SINR_THRESHOLD = 10 ** (5 / 10)

def simulate(time_steps=20):
    results = []
    state = NetworkState()

    for t in range(1, time_steps + 1):
        users = generate_users(t)
        content, redundancy = generate_content_request()

        sinr_linear = compute_sinr(users)
        popularity, _, _ = state.get_state()

        users, popularity, sinr_linear, events = apply_perturbations(
            users, popularity, sinr_linear
        )

        used_capacity = users * USER_RATE_Mbps * (1 + redundancy)
        congestion = min(1.0, used_capacity / TOTAL_CAPACITY_Mbps)

        state.update_state(popularity, sinr_linear, congestion)

        service_continuity = state.compute_service_continuity(
            SINR_THRESHOLD
        )

        results.append({
            "time": t,
            "hour": datetime.now().hour,
            "users": users,
            "content": content,
            "redundancy": redundancy,
            "sinr_linear": sinr_linear,
            "congestion": congestion,
            "service_continuity": service_continuity,
            "events": events
        })

    return results