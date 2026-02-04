# decision_engine/train_data_generator.py

import csv
from decision_engine.decision_engine import decide_delivery_mode


def generate_ml_training_data(
    input_csv="simulation_dataset.csv",
    output_csv="ml_training_data.csv"
):
    """
    Uses utility-based decision engine (teacher)
    to generate labels for ML model (student).

    Features:
    - service_continuity_diff
    - spectrum_efficiency_diff
    - congestion_diff

    Label:
    - 1 → ATSC
    - 0 → UNICAST
    """

    with open(input_csv, "r") as f_in, open(output_csv, "w", newline="") as f_out:
        reader = csv.DictReader(f_in)
        writer = csv.writer(f_out)

        # 🔹 Header
        writer.writerow([
            "service_continuity_diff",
            "spectrum_efficiency_diff",
            "congestion_diff",
            "label"
        ])

        for row in reader:
            # -----------------------------
            # KPI construction (REALISTIC)
            # -----------------------------

            service_continuity = float(row["service_continuity"])
            congestion = float(row["congestion"])

            # Unicast KPIs (more sensitive to congestion)
            unicast_kpis = {
                "service_continuity": service_continuity,
                "spectrum_efficiency": 0.6,
                "congestion": congestion
            }

            # ATSC KPIs (broadcast advantage)
            atsc_kpis = {
                "service_continuity": service_continuity * 0.9,
                "spectrum_efficiency": 0.8,
                "congestion": congestion * 0.6
            }

            # -----------------------------
            # Teacher decision
            # -----------------------------
            decision = decide_delivery_mode(
                unicast_kpis,
                atsc_kpis
            )

            label = 1 if decision == "ATSC" else 0

            # -----------------------------
            # Feature differences
            # -----------------------------
            writer.writerow([
                atsc_kpis["service_continuity"] - unicast_kpis["service_continuity"],
                atsc_kpis["spectrum_efficiency"] - unicast_kpis["spectrum_efficiency"],
                unicast_kpis["congestion"] - atsc_kpis["congestion"],
                label
            ])

    print(f"✅ ML training data saved as {output_csv}")


if __name__ == "__main__":
    generate_ml_training_data()