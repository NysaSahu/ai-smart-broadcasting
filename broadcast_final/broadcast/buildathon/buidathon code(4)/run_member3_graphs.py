from ai_engine.graph_generator import plot_all_graphs

import math
import matplotlib.pyplot as plt
import csv

users_cmp = list(range(10, 201, 10))

TOTAL_UNICAST_CAPACITY = 50
BROADCAST_BASE = 20


def unicast_tp(n):
    return max(0.5, TOTAL_UNICAST_CAPACITY / n)


def broadcast_tp(n):
    return max(2.0, BROADCAST_BASE / math.sqrt(n))


unicast_only = []
broadcast_only = []
tr6026_curve = []
ai_curve = []


def run_all_member3_graphs():
    figs = []

    # ✅ CLEAR OLD DATA (important for Streamlit reruns)
    unicast_only.clear()
    broadcast_only.clear()
    tr6026_curve.clear()
    ai_curve.clear()

    # ✅ Get graphs from graph_generator
    figs.extend(plot_all_graphs(return_figs=True))

    NUSER_TH = 60
    AI_SWITCH = 40

    # Generate data
    for n in users_cmp:
        u_tp = unicast_tp(n)
        b_tp = broadcast_tp(n)
        tr_tp = b_tp if n > NUSER_TH else u_tp
        ai_tp = b_tp if n > AI_SWITCH else u_tp

        unicast_only.append(u_tp)
        broadcast_only.append(b_tp)
        tr6026_curve.append(tr_tp)
        ai_curve.append(ai_tp)

    # ================= GRAPH 6 =================
    fig1 = plt.figure()
    plt.plot(users_cmp, unicast_only, label="Unicast only")
    plt.plot(users_cmp, broadcast_only, label="Broadcast only")
    plt.plot(users_cmp, tr6026_curve, label="TR-6026 Hybrid")
    plt.plot(users_cmp, ai_curve, label="AI-assisted Hybrid")

    plt.xlabel("Number of Users")
    plt.ylabel("Average Throughput per User (Mbps)")
    plt.title("Delivery Strategy Performance under Increasing Load")
    plt.legend()
    plt.grid(True)

    figs.append(fig1)

    # ================= GRAPH 7 =================
    fig2 = plt.figure()
    plt.plot(users_cmp, tr6026_curve, label="TR-6026 (Non-AI)")
    plt.plot(users_cmp, ai_curve, label="AI-assisted")

    plt.xlabel("Number of Users")
    plt.ylabel("Average Throughput per User (Mbps)")
    plt.title("AI-assisted vs TR-6026 Switching Decisions")
    plt.legend()
    plt.grid(True)

    figs.append(fig2)

    return figs

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

    # ==========================================================
    # CSV EXPORT (OVERWRITES ON EVERY RUN)
    # ==========================================================
    with open("buildathon_results.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Number_of_Users",
            "Unicast_Throughput_Mbps",
            "Broadcast_Throughput_Mbps",
            "TR6026_Selected_Throughput_Mbps",
            "AI_Selected_Throughput_Mbps",
            "TR6026_Delivery_Mode",
            "AI_Delivery_Mode",
            "Best_Delivery_Strategy"
        ])

        for i, n in enumerate(users_cmp):
            unicast_tp_val = round(unicast_only[i], 2)
            broadcast_tp_val = round(broadcast_only[i], 2)
            tr_tp_val = round(tr6026_curve[i], 2)
            ai_tp_val = round(ai_curve[i], 2)

            tr_mode = "Broadcast" if tr_tp_val == broadcast_tp_val else "Unicast"
            ai_mode = "Broadcast" if ai_tp_val == broadcast_tp_val else "Unicast"

            best_val = max(
                unicast_tp_val,
                broadcast_tp_val,
                tr_tp_val,
                ai_tp_val
            )

            if best_val == ai_tp_val:
                best = "AI-assisted"
            elif best_val == tr_tp_val:
                best = "TR-6026"
            elif best_val == broadcast_tp_val:
                best = "Broadcast"
            else:
                best = "Unicast"

            writer.writerow([
                n,
                unicast_tp_val,
                broadcast_tp_val,
                tr_tp_val,
                ai_tp_val,
                tr_mode,
                ai_mode,
                best
            ])

    print("\nCSV exported: buildathon_results.csv")

    print("\nCSV exported: buildathon_results.csv")

# ==========================================================
# SAFE ENTRY POINT
# ==========================================================
if __name__ == "__main__":
    run_all_member3_graphs()
