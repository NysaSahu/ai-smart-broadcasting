# ai_engine/graph_generator.py

import matplotlib.pyplot as plt

from ai_engine.mock_data import generate_user_range
from ai_engine.metrics import (
    spectrum_efficiency,
    service_continuity,
    available_cellular_bandwidth,
    congestion_efficiency_unicast,
    congestion_efficiency_broadcast,
    throughput_per_user_unicast,
    throughput_per_user_broadcast
)


def plot_all_graphs():
    users = generate_user_range()

    # ---------- Graph 1: Spectrum Efficiency ----------
    plt.figure()
    plt.plot(users, [spectrum_efficiency(u) for u in users])
    plt.xlabel("Number of Users")
    plt.ylabel("Spectrum Efficiency (bits/s/Hz)")
    plt.title("Users vs Spectrum Efficiency")
    plt.grid(True)
    plt.show()

    # ---------- Graph 2: Service Continuity ----------
    plt.figure()
    plt.plot(users, [service_continuity(u) for u in users])
    plt.xlabel("Number of Users")
    plt.ylabel("Service Continuity")
    plt.title("Users vs Service Continuity")
    plt.grid(True)
    plt.show()

    # ---------- Graph 3: Available Cellular Bandwidth ----------
    plt.figure()
    plt.plot(users, [available_cellular_bandwidth(u) for u in users])
    plt.xlabel("Number of Users")
    plt.ylabel("Available Cellular Bandwidth (MHz)")
    plt.title("Users vs Available Cellular Bandwidth")
    plt.grid(True)
    plt.show()

    # ---------- Graph 4: Broadcast vs Unicast Congestion Handling ----------
    plt.figure()
    plt.plot(users, [congestion_efficiency_unicast(u) for u in users], label="Unicast")
    plt.plot(users, [congestion_efficiency_broadcast(u) for u in users], label="Broadcast")
    plt.xlabel("Number of Users")
    plt.ylabel("Congestion Handling Efficiency")
    plt.title("Broadcast vs Unicast under Congestion")
    plt.legend()
    plt.grid(True)
    plt.show()

    # ---------- Graph 5: Throughput per User ----------
    plt.figure()
    plt.plot(users, [throughput_per_user_unicast(u) for u in users], label="Unicast")
    plt.plot(users, [throughput_per_user_broadcast(u) for u in users], label="Broadcast")
    plt.xlabel("Number of Users")
    plt.ylabel("Average Throughput per User (Mbps)")
    plt.title("Users vs Throughput per User")
    plt.legend()
    plt.grid(True)
    plt.show()