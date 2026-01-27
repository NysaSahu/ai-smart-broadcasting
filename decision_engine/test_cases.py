# test_cases.py
from decision_engine import ai_decide
from stability import StableDecision  # your hysteresis/stability logic

# -----------------------------
# TST-1: Smart switching
# -----------------------------
print("\n=== TST-1: Smart Switching Under Increasing Demand ===")
increasing_demand = [
    [2, 1, 20],
    [10, 5, 50],
    [50, 10, 80],
]

stable = StableDecision()  # Initialize stability tracker

for i, case in enumerate(increasing_demand):
    raw_mode = ai_decide(*case)
    mode = stable.check(raw_mode)  # Apply stability/hysteresis
    print(f"Step {i+1}: Input {case} => Raw Mode: {raw_mode}, Stable Mode: {mode}")

# -----------------------------
# TST-2: Stability under fluctuating demand
# -----------------------------
print("\n=== TST-2: Stability Under Fluctuating Demand ===")
fluctuating_demand = [
    [10, 5, 50],
    [11, 5, 52],
    [9, 5, 48],
    [10, 5, 51],
    [12, 6, 55],
    [9, 4, 49],
]

stable = StableDecision()  # reset stability for TST-2
for i, case in enumerate(fluctuating_demand):
    raw_mode = ai_decide(*case)
    mode = stable.check(raw_mode)
    print(f"Fluctuation {i+1}: Input {case} => Raw Mode: {raw_mode}, Stable Mode: {mode}")

# -----------------------------
# TST-3: Service continuity / policy fallback
# -----------------------------
print("\n=== TST-3: Service Continuity / Policy Fallback ===")
service_continuity = [
    [1, 1, 95],  # overloaded network -> fallback unicast
    [15, 6, 60], # moderate load -> multicast
]

stable = StableDecision()  # reset stability for TST-3
for i, case in enumerate(service_continuity):
    raw_mode = ai_decide(*case)
    mode = stable.check(raw_mode)
    print(f"Continuity {i+1}: Input {case} => Raw Mode: {raw_mode}, Stable Mode: {mode}")
