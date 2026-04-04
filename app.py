import streamlit as st
import pandas as pd
import json

# --- DASHBOARD CONFIG ---
st.set_page_config(page_title="Mission Control", layout="wide")

# --- DATA SOURCE ---
metrics = {
    "Nutrient": ["Calories", "Protein", "Carbs", "Fats", "Fiber", "Iron", "Zinc", "Vitamin D", "Magnesium", "Omega-3"],
    "Current": [1950, 141, 90, 70, 38, 34, 13.5, 8900, 300, 1800],
    "Limit": [2300, 140, 130, 80, 40, 19, 17, 2000, 440, 500],
    "Unit": ["kcal", "g", "g", "g", "g", "mg", "mg", "IU", "mg", "mg"]
}
df = pd.DataFrame(metrics)

# --- NAVIGATION ---
tab1, tab2 = st.tabs(["📊 Live Dashboard", "🍱 The Meal Vault"])

# --- TAB 1: LIVE DASHBOARD ---
with tab1:
    st.title("🛡️ System Diagnostics")
    
    # Section 1: Progress Bars with "Current / Target" Labels
    st.subheader("🚀 Core Macro Progress")
    core_list = ["Calories", "Protein", "Carbs", "Fats", "Fiber"]
    cols = st.columns(len(core_list))
    
    for i, name in enumerate(core_list):
        row = df[df["Nutrient"] == name].iloc[0]
        curr, lim, unit = row["Current"], row["Limit"], row["Unit"]
        progress = min(curr / lim, 1.0)
        
        with cols[i]:
            # Updated Label: Mentioning target explicitly (e.g., 141/140 g)
            st.write(f"**{name}**")
            st.write(f"{curr} / {lim} {unit}")
            st.progress(progress)

    st.divider()

    # Section 2: Metric Card Representation (Image 2 & 3 Style)
    st.subheader("🌡️ Full Spectrum Analysis")
    
    # Displaying all 10 nutrients as high-visibility cards
    card_cols = st.columns(5) 
    for idx, row in df.iterrows():
        col_idx = idx % 5
        with card_cols[col_idx]:
            delta_val = row["Current"] - row["Limit"]
            # Color coding: Green if meeting/exceeding (for protein), 
            # Red/Normal if exceeding a limit (for calories)
            st.metric(
                label=f"{row['Nutrient']} ({row['Unit']})",
                value=f"{row['Current']} / {row['Limit']}",
                delta=f"{round(delta_val, 1)} vs Target",
                delta_color="normal"
            )

# --- TAB 2: THE MEAL VAULT (RESTORED) ---
with tab2:
    st.title("🍱 The Meal Vault & Daily Protocol")
    col_meal, col_night = st.columns(2)
    
    with col_meal:
        st.header("🕒 Feeding Schedule")
        # Meal timing based on 1 PM to 4 AM protocol
        with st.expander("1:00 PM - Metabolic Trigger", expanded=True):
            st.write("• 500ml Water (Jeera/Coriander Rotation)")
        with st.expander("2:00 PM - The Nutrient Break", expanded=True):
            st.write("• 1 Banana + 150g Papaya/Apple")
            st.write("• 5 Soaked Almonds + 1 Walnut")
            st.write("• **Supp:** 1x HK Vitals Multivitamin")
        with st.expander("9:00 PM - The Power Meal", expanded=True):
            st.write("• **MWF:** 400g Chicken + 300g Curd + 2 Eggs + Roti")
            st.write("• **TTS:** 400g Chicken + 300g Curd + Sautéed Veggies")
            st.write("• **Supp:** 2x Omega-3 + 2x Good Monk")

    with col_night:
        st.header("🌙 Nightly Protocol")
        with st.expander("3:15 AM - The Wind-Down", expanded=True):
            st.write("• Magnesium Glycinate (250-400mg)")
        with st.expander("3:45 AM - Nightly Cleanse", expanded=True):
            st.write("• 1 Spoon Isabgol in 250ml Water")
