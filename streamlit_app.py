import streamlit as st
import json
import pandas as pd
from main import load_drones, score_drone

st.title("🚁 Drone Intelligence Agent")

drones = load_drones()
df = pd.DataFrame(drones)
df["Score"] = df.apply(score_drone, axis=1)
df_sorted = df.sort_values(by="Score", ascending=False)

st.subheader("📊 Ranked Drones")
st.dataframe(df_sorted)

st.success(f"🏆 Best Drone: {df_sorted.iloc[0]['id']} (Score: {df_sorted.iloc[0]['Score']:.2f})")
