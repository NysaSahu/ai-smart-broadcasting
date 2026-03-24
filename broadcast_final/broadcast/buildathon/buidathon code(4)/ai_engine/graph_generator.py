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


def plot_all_graphs(return_figs=False):
    users = generate_user_range()

    figs = []

    # ---------- Graph 1: Spectrum Efficiency ----------
    se_vals = [spectrum_efficiency(u) for u in users]

    plt.figure()
    plt.plot(users, se_vals)
    plt.xlabel("Number of Users")
    plt.ylabel("Spectrum Efficiency (bits/s/Hz)")
    plt.title("Users vs Spectrum Efficiency")
    plt.grid(True)

    if return_figs:
        figs.append(plt.gcf())
    else:
        plt.show()

    # ---------- Graph 2: Service Continuity ----------
    sc_vals = [service_continuity(u) for u in users]

    plt.figure()
    plt.plot(users, sc_vals)
    plt.xlabel("Number of Users")
    plt.ylabel("Service Continuity")
    plt.title("Users vs Service Continuity")
    plt.grid(True)

    if return_figs:
        figs.append(plt.gcf())
    else:
        plt.show()

    # ---------- Graph 3: Available Cellular Bandwidth ----------
    bw_vals = [available_cellular_bandwidth(u) for u in users]

    plt.figure()
    plt.plot(users, bw_vals)
    plt.xlabel("Number of Users")
    plt.ylabel("Available Cellular Bandwidth (MHz)")
    plt.title("Users vs Available Cellular Bandwidth")
    plt.grid(True)

    if return_figs:
        figs.append(plt.gcf())
    else:
        plt.show()

    # ---------- Graph 4: Congestion Handling ----------
    cu_vals = [congestion_efficiency_unicast(u) for u in users]
    cb_vals = [congestion_efficiency_broadcast(u) for u in users]

    plt.figure()
    plt.plot(users, cu_vals, label="Unicast")
    plt.plot(users, cb_vals, label="Broadcast")
    plt.xlabel("Number of Users")
    plt.ylabel("Congestion Handling Efficiency")
    plt.title("Broadcast vs Unicast under Congestion")
    plt.legend()
    plt.grid(True)

    if return_figs:
        figs.append(plt.gcf())
    else:
        plt.show()

    # ---------- Graph 5: Throughput ----------
    tu_vals = [throughput_per_user_unicast(u) for u in users]
    tb_vals = [throughput_per_user_broadcast(u) for u in users]

    plt.figure()
    plt.plot(users, tu_vals, label="Unicast")
    plt.plot(users, tb_vals, label="Broadcast")
    plt.xlabel("Number of Users")
    plt.ylabel("Average Throughput per User (Mbps)")
    plt.title("Users vs Throughput per User")
    plt.legend()
    plt.grid(True)

    if return_figs:
        figs.append(plt.gcf())
    else:
        plt.show()

    if return_figs:
        return figs