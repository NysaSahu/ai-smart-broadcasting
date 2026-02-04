from simulator.traffic_simulator import simulate

if __name__ == "__main__":
    results = simulate()

    for r in results:
        print(
            f"t={r['time']} | "
            f"users={r['users']} | "
            f"content={r['content']} | "
            f"SINR={round(r['sinr_linear'],2)} | "
            f"cong={round(r['congestion'],2)} | "
            f"SC={round(r['service_continuity'],2)} | "
            f"events={r['events']}"
        )