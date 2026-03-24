# main.py

from simulator.traffic_simulator import simulate
import run_member3_graphs


def run_simulation_logs():
    # User & Content Provider log output removed
    pass


def run_analysis():
    print("\n=== ANALYTICS: GRAPHS & TABLES ===\n")
    # ✅ FIX: call the correctly named function
    run_member3_graphs.run_all_member3_graphs()


if __name__ == "__main__":
    print("\n===== BUILDATHON MAIN ENTRY POINT =====\n")

    # 1️⃣ FIRST: show content-provider + user activity
    # run_simulation_logs()

    # 2️⃣ THEN: show graphs and tables (blocking, expected)
    run_analysis()

    print("\n===== END OF EXECUTION =====\n")
