from ai_engine.graph_generator import plot_all_graphs

# ----------------------------------------------------------
# RUN EXISTING GRAPHS (UNCHANGED)
# ----------------------------------------------------------
plot_all_graphs()


# ==========================================================
# IMPORTS
# ==========================================================
import math
import matplotlib.pyplot as plt


# ==========================================================
# COMMON DATA
# ==========================================================
users_cmp = list(range(10, 201, 10))

TOTAL_UNICAST_CAPACITY = 50   # Mbps
BROADCAST_BASE = 20           # Mbps


def unicast_tp(n):
    return max(0.5, TOTAL_UNICAST_CAPACITY / n)


def broadcast_tp(n):
    return max(2.0, BROADCAST_BASE / math.sqrt(n))


# ==========================================================
# BASE DELIVERY MODES
# ==========================================================
unicast_only = [unicast_tp(n) for n in users_cmp]
broadcast_only = [broadcast_tp(n) for n in users_cmp]


# ==========================================================
# TR-6026 THRESHOLD-BASED SWITCHING (NON-AI)
# ==========================================================
NUSER_TH = 60

tr6026_curve = [
    broadcast_tp(n) if n > NUSER_TH else unicast_tp(n)
    for n in users_cmp
]


# ==========================================================
# AI-ASSISTED SWITCHING
# ==========================================================
AI_SWITCH = 40

ai_curve = [
    broadcast_tp(n) if n > AI_SWITCH else unicast_tp(n)
    for n in users_cmp
]


# ==========================================================
# GRAPH 1: DELIVERY MODE COMPARISON (ALL STRATEGIES)
# ==========================================================
plt.figure()

plt.plot(users_cmp, unicast_only, label="Unicast only")
plt.plot(users_cmp, broadcast_only, label="Broadcast only")
plt.plot(users_cmp, tr6026_curve, label="TR-6026 Hybrid")
plt.plot(users_cmp, ai_curve, label="AI-assisted Hybrid")

plt.xlabel("Number of Users")
plt.ylabel("Average Throughput per User (Mbps)")
plt.title("Delivery Strategy Performance under Increasing Load")

plt.legend()
plt.grid(True)
plt.show()


# ==========================================================
# GRAPH 2: AI vs TR-6026 ONLY (Decision Logic Comparison)
# ==========================================================
plt.figure()

plt.plot(users_cmp, tr6026_curve, label="TR-6026 (Non-AI)")
plt.plot(users_cmp, ai_curve, label="AI-assisted")

plt.xlabel("Number of Users")
plt.ylabel("Average Throughput per User (Mbps)")
plt.title("AI-assisted vs TR-6026 Switching Decisions")

plt.legend()
plt.grid(True)
plt.show()


# ==========================================================
# TABLE 1: AI vs TR-6026 (CLEAR DECISION TABLE)
# ==========================================================
print("\n=== AI vs TR-6026 Decision Comparison ===\n")

header = (
    f"{'Users':<6}"
    f"{'TR TP':<10}"
    f"{'TR Mode':<12}"
    f"{'AI TP':<10}"
    f"{'AI Mode':<12}"
    f"{'Winner':<12}"
)

print(header)
print("-" * len(header))


for i, n in enumerate(users_cmp):

    tr = round(tr6026_curve[i], 2)
    ai = round(ai_curve[i], 2)

    tr_mode = "Broadcast" if tr == broadcast_only[i] else "Unicast"
    ai_mode = "Broadcast" if ai == broadcast_only[i] else "Unicast"

    if ai > tr:
        winner = "AI better"
    elif tr > ai:
        winner = "TR better"
    else:
        winner = "Same perf"

    print(f"{n:<6}{tr:<10}{tr_mode:<12}{ai:<10}{ai_mode:<12}{winner:<12}")


# ==========================================================
# TABLE 2: ALL STRATEGIES (FULL COMPARISON)
# ==========================================================
print("\n=== Full Strategy Comparison Table ===\n")

header = (
    f"{'Users':<6}"
    f"{'Unicast':<10}"
    f"{'Broadcast':<11}"
    f"{'TR TP':<9}"
    f"{'TR Mode':<11}"
    f"{'AI TP':<9}"
    f"{'AI Mode':<11}"
    f"{'Best Strategy':<15}"
)

print(header)
print("-" * len(header))


for i, n in enumerate(users_cmp):

    u = round(unicast_only[i], 2)
    b = round(broadcast_only[i], 2)
    tr = round(tr6026_curve[i], 2)
    ai = round(ai_curve[i], 2)

    tr_mode = "Broadcast" if tr == b else "Unicast"
    ai_mode = "Broadcast" if ai == b else "Unicast"

    best_val = max(u, b, tr, ai)

    if best_val == ai:
        best = "AI-assisted"
    elif best_val == tr:
        best = "TR-6026"
    elif best_val == b:
        best = "Broadcast"
    else:
        best = "Unicast"

    print(f"{n:<6}{u:<10}{b:<11}{tr:<9}{tr_mode:<11}{ai:<9}{ai_mode:<11}{best:<15}")
