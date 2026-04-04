import streamlit as st
import pandas as pd
import json

# --- DASHBOARD CONFIG ---
st.set_page_config(page_title="Mission Control", layout="wide")

# --- DATA SOURCE ---
metrics = {
    "Nutrient": ["Calories", "Protein", "Carbs", "Fats", "Fiber", "Iron", "Zinc", "Vitamin D", "Magnesium", "Omega-3", "Vitamin C", "Calcium", "Potassium", "Vitamin B12"],
    "Current": [1950, 140, 90, 70, 35, 32.0, 13.5, 8900, 300, 450, 120.0, 450.0, 1800, 3.5],
    "Limit": [2300, 140, 130, 80, 40, 19.0, 17, 2000, 500, 500, 80.0, 1000.0, 3500, 2.5],
    "Unit": ["kcal", "g", "g", "g", "g", "mg", "mg", "IU", "mg", "mg", "mg", "mg", "mg", "mcg"]
}
df = pd.DataFrame(metrics)

# --- NAVIGATION ---
tab1, tab2 = st.tabs(["📊 Live Dashboard", "🍱 The Meal Vault"])

# --- TAB 1: LIVE DASHBOARD ---
with tab1:
    st.title("🛡️ System Diagnostics")
    
    # Section 1: Core Macro Progress (Top Row)
    st.subheader("🚀 Core Macro Progress")
    core_list = ["Calories", "Protein", "Carbs", "Fats", "Fiber"]
    cols = st.columns(len(core_list))
    
    for i, name in enumerate(core_list):
        row = df[df["Nutrient"] == name].iloc[0]
        curr, lim, unit = row["Current"], row["Limit"], row["Unit"]
        progress = min(curr / lim, 1.0)
        
        with cols[i]:
            st.write(f"**{name}**")
            st.write(f"{curr} / {lim} {unit}")
            st.progress(progress)

    st.divider()

    # Section 2: Full Spectrum Analysis
    st.subheader("🌡️ Full Spectrum: Consuming vs. Upper Limit")
    grid_cols = st.columns(2)
    
    for idx, row in df.iterrows():
        with grid_cols[idx % 2]:
            curr, lim, unit, name = row["Current"], row["Limit"], row["Unit"], row["Nutrient"]
            progress = min(curr / lim, 1.0)
            
            st.write(f"**{name}**: {curr} / {lim} {unit}")
            st.progress(progress)
            
            # Custom Status Lines for specific nutrients
            if name == "Vitamin C":
                st.caption("Avg consume")
            elif name == "Iron":
                st.caption("⚠️ High but safe (diet-based)")
            elif name == "Calcium":
                st.caption("⚠️ Low")
            
            st.write("") # Spacer

# --- TAB 2: THE MEAL VAULT ---
with tab2:
    st.title("🍱 The Meal Vault & Daily Protocol")
    col_meal, col_night = st.columns(2)
    
    with col_meal:
        st.header("🕒 Feeding Schedule")
        with st.expander("1:00 PM - Metabolic Trigger", expanded=True):
            st.write("• 500ml Water (Jeera/Coriander Rotation)")
        with st.expander("2:00 PM - The Nutrient Break", expanded=True):
            st.write("• 1 Banana + 150g Papaya/Apple")
            st.write("• 5 Soaked Almonds + 1 Walnut")
            st.write("• **Supp:** 1x HK Vitals Multivitamin")
        with st.expander("9:00 PM - The Power Meal", expanded=True):
            st.write("• **MWF:** 400g Chicken (Iron Pan) + 300g Curd + 2 Eggs + Roti")
            st.write("• **TTS:** 400g Chicken + 300g Curd + Sautéed Veggies")
            st.write("• **Supp:** 2x Omega-3 + 2x Good Monk")

    with col_night:
        st.header("🌙 Nightly Protocol")
        with st.expander("3:15 AM - The Wind-Down", expanded=True):
            st.write("• Magnesium Glycinate (250-400mg)")
        with st.expander("3:45 AM - Nightly Cleanse", expanded=True):
            st.write("• 1 Spoon Isabgol in 250ml Water")
