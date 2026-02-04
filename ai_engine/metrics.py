# ai_engine/metrics.py

# ---------- Existing KPIs ----------

def spectrum_efficiency(users):
    return max(0.5, 5 - 0.015 * users)


def service_continuity(users):
    return max(0.3, 1 - 0.004 * users)


def available_cellular_bandwidth(users):
    TOTAL_BW = 100
    used = users * 0.3
    return max(0, TOTAL_BW - used)


def congestion_efficiency_unicast(users):
    return max(0.2, 1 - 0.006 * users)


def congestion_efficiency_broadcast(users):
    return max(0.5, 1 - 0.002 * users)


# ---------- NEW KPI: Throughput per User ----------

def throughput_per_user_unicast(users):
    TOTAL_CAPACITY = 50  # Mbps
    return max(0.5, TOTAL_CAPACITY / users)


def throughput_per_user_broadcast(users):
    EFFECTIVE_CAPACITY = 20  # Mbps
    return max(2.0, EFFECTIVE_CAPACITY / (users ** 0.5))