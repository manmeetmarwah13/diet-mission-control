import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- DASHBOARD CONFIG ---
st.set_page_config(page_title="Mission Control", layout="wide")

# --- DATA SOURCE ---
# Unified data for all requested metrics
metrics = {
    "Nutrient": ["Calories", "Protein", "Carbs", "Fats", "Fiber", "Iron", "Zinc", "Vitamin D", "Magnesium", "Omega-3"],
    "Current": [1950, 141, 90, 70, 38, 34, 13.5, 8900, 300, 1800],
    "Limit": [2300, 140, 130, 80, 40, 19, 17, 2000, 440, 500],
    "Unit": ["kcal", "g", "g", "g", "g", "mg", "mg", "IU", "mg", "mg"]
}
df = pd.DataFrame(metrics)

# --- NAVIGATION ---
# Using tabs for a cleaner "separate page" feel
tab1, tab2 = st.tabs(["📊 Live Dashboard", "🍱 The Meal Vault"])

# --- TAB 1: LIVE DASHBOARD ---
with tab1:
    st.title("🛡️ System Diagnostics")
    
    # Image 1 Style: Progress Bars for Core Macros
    st.subheader("🚀 Core Macro Progress")
    core_cols = st.columns(5)
    core_list = ["Calories", "Protein", "Carbs", "Fats", "Fiber"]
    
    for i, name in enumerate(core_list):
        row = df[df["Nutrient"] == name].iloc[0]
        val, lim, unit = row["Current"], row["Limit"], row["Unit"]
        progress = min(val / lim, 1.0)
        
        with core_cols[i]:
            st.metric(label=f"{name} ({unit})", value=f"{val}", delta=f"{val-lim} vs Target")
            st.progress(progress)

    st.divider()

    # Image 2 & 3 Style: Unified Diagnostic Chart
    st.subheader("🌡️ Full Spectrum Analysis")
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Current Intake',
        x=df['Nutrient'], y=df['Current'],
        marker_color='#1f77b4',
        text=[f"{v}{u}" for v, u in zip(df['Current'], df['Unit'])],
        textposition='outside'
    ))
    fig.add_trace(go.Bar(
        name='Upper Limit',
        x=df['Nutrient'], y=df['Limit'],
        marker_color='#ff7f0e',
        text=[f"{v}{u}" for v, u in zip(df['Limit'], df['Unit'])],
        textposition='outside'
    ))
    
    fig.update_layout(barmode='group', height=500, margin=dict(t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: THE MEAL VAULT (Separate Columnar Page) ---
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
            st.write("• **MWF:** 400g Chicken + 300g Curd + 2 Eggs + Roti")
            st.write("• **TTS:** 400g Chicken + 300g Curd + Sautéed Veggies")
            st.write("• **Supp:** 2x Omega-3 + 2x Good Monk")

    with col_night:
        st.header("🌙 Nightly Protocol")
        with st.expander("3:15 AM - The Wind-Down", expanded=True):
            st.write("• Magnesium Glycinate (250-400mg)")
            
        with st.expander("3:45 AM - Nightly Cleanse", expanded=True):
            st.write("• 1 Spoon Isabgol in 250ml Water")
            
        st.info("**Mission Status:** Fixing Calcium (45% of Target) and Potassium gaps.")
