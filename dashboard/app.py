import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# Page Configuration
# ==================================================
st.set_page_config(
    page_title="AI Smart Broadcasting Dashboard",
    layout="wide"
)

# ==================================================
# Title & Description
# ==================================================
st.title("📡 AI Smart Broadcasting – System Dashboard")

st.markdown(
    """
    **Purpose of this dashboard**

    This dashboard visually demonstrates the complete system behavior:
    **network conditions → congestion → AI decision → delivery outcome**.

    It answers one simple question:

    > *What is happening in the network, how does AI react, and what is the outcome?*
    """
)

st.divider()

# ==================================================
# Dummy Time Axis (Placeholder for real simulation)
# ==================================================
time = np.arange(0, 100)

# ==================================================
# SECTION 1 — Network State (Input Layer)
# ==================================================
st.subheader("🟦 Network State (Input Layer)")

st.markdown(
    """
    This section shows the **raw network environment** the system is dealing with.
    """
)

# --- Dummy network inputs ---
users = 40 + 10 * np.sin(time / 8)
users[50:] += 35  # flash crowd after t=50

sinr = 25 + 5 * np.cos(time / 10) - (time > 60) * 6  # channel degradation

service_continuity = np.clip(1 - (users / 120), 0, 1)

# --- Plot: Network State ---
fig1, ax1 = plt.subplots()
ax1.plot(time, users, label="Users")
ax1.plot(time, sinr, label="SINR (dB)")
ax1.plot(time, service_continuity * 100, label="Service Continuity (%)")

ax1.set_xlabel("Time")
ax1.set_ylabel("Value")
ax1.set_title("Network State Over Time")
ax1.legend()

st.pyplot(fig1)

st.divider()

# ==================================================
# SECTION 2 — Network Congestion (Derived KPI)
# ==================================================
st.subheader("🟧 Network Congestion")

st.markdown(
    """
    This section visualizes **network congestion**, derived from user load.
    It explains *why* intelligent delivery decisions are needed.
    """
)

# --- Congestion metric (0 to 1) ---
congestion = np.clip(users / 120, 0, 1)

fig2, ax2 = plt.subplots()
ax2.plot(time, congestion, color="orange")
ax2.set_ylim(0, 1)
ax2.set_xlabel("Time")
ax2.set_ylabel("Congestion Level")
ax2.set_title("Network Congestion vs Time")

st.pyplot(fig2)

st.divider()

# ==================================================
# SECTION 3 — AI Intelligence Layer (Placeholder)
# ==================================================
st.subheader("🟨 AI Intelligence Layer")

st.markdown(
    """
    This section represents the **AI-driven delivery decision**.

    ⚠️ Currently using **placeholder logic**  
    (real AI model will be plugged in later by Member 2)
    """
)

# --- Placeholder AI decision ---
ai_decision = np.where(congestion > 0.7, "ATSC (Broadcast)", "UNICAST")

st.write("**AI Predicted Delivery Mode (over time):**")
st.write(ai_decision.tolist())

st.info(
    "AI Decision Logic (placeholder):\n"
    "- High congestion → ATSC (Broadcast)\n"
    "- Low congestion → Unicast"
)

st.divider()

# ==================================================
# SECTION 4 — Delivery Outcome (System Response)
# ==================================================
st.subheader("🟥 Delivery Outcome")

st.markdown(
    """
    This section shows the **impact of the AI decision** on the system.
    It closes the loop: **problem → decision → improvement**.
    """
)

# --- Placeholder outcome ---
post_congestion = congestion.copy()
post_congestion[congestion > 0.7] -= 0.3
post_congestion = np.clip(post_congestion, 0, 1)

fig3, ax3 = plt.subplots()
ax3.plot(time, congestion, label="Before AI")
ax3.plot(time, post_congestion, label="After AI")
ax3.set_ylim(0, 1)
ax3.set_xlabel("Time")
ax3.set_ylabel("Congestion Level")
ax3.set_title("Impact of AI on Congestion")
ax3.legend()

st.pyplot(fig3)

st.success(
    "Result: AI-based delivery switching reduces congestion "
    "and improves service continuity during high-load periods."
)