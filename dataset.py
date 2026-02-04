import csv
from simulator.traffic_simulator import simulate

def generate_dataset(filename="simulation_dataset.csv"):
    results = simulate()

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "time",
            "hour",
            "users",
            "content",
            "redundancy",
            "sinr_linear",
            "congestion",
            "service_continuity"
        ])

        for r in results:
            writer.writerow([
                r["time"],
                r["hour"],
                r["users"],
                r["content"],
                r["redundancy"],
                r["sinr_linear"],
                r["congestion"],
                r["service_continuity"]
            ])

    print("Dataset saved as simulation_dataset.csv")

if __name__ == "__main__":
    generate_dataset()