from simulator.traffic_simulator import TrafficSimulator


def main():
    sim = TrafficSimulator(5)

    changes = [0, 5, 10, 20, -10, -5]

    for t, change in enumerate(changes):
        state = sim.step(change)
        print(
            f"Time {t}: Users={state.user_count}, "
            f"Load={state.load:.2f}"
        )


if __name__ == "__main__":
    main()

