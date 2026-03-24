import sys
import os
import streamlit as st

# ✅ Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run_member3_graphs import run_all_member3_graphs

st.title("📊 Simulation Dashboard")

figs = run_all_member3_graphs()

for i, fig in enumerate(figs):
    st.subheader(f"Graph {i+1}")
    st.pyplot(fig)