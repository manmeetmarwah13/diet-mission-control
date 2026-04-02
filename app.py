import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="90KG Mission Control", page_icon="⚡", layout="wide")

# --- UI OVERRIDE (Fixes Blackout/Visibility Issues) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    [data-testid="stMetric"] {
        background-color: #ffffff; border: 1px solid #dee2e6;
        padding: 15px; border-radius: 12px; box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .stProgress > div > div > div > div { background-color: #2ecc71; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA ENGINE ---
# Calculating based on your 400g Chicken + Eggs + Good Monk + Supplements
nutrients = {
    "Macro": {
        "Protein": {"current": 141, "goal": 140, "unit": "g"},
        "Carbs": {"current": 87, "goal": 150, "unit": "g"},
        "Fats": {"current": 82, "goal": 85, "unit": "g"},
        "Fiber": {"current": 35, "goal": 30, "unit": "g"}
    },
    "Micro": {
        "Probiotics": {"current": 260, "goal": 260, "unit": "Cr"},
        "Ashwagandha": {"current": 135, "goal": 150, "unit": "mg"},
        "Magnesium": {"current": 250, "goal": 400, "unit": "mg"},
        "Vitamin D3": {"current": 60000, "goal": 60000, "unit": "IU"},
        "Omega-3": {"current": 1300, "goal": 1300, "unit": "mg"},
        "Zinc": {"current": 9, "goal": 12, "unit": "mg"}
    }
}

# --- HEADER ---
st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    st.sidebar.header("Daily Telemetry")
    water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 4.1)
    
    # ROW 1: THE 4-COLUMN SUMMARY
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Daily Calories", "1445 kcal", "-1155 vs TDEE")
    c2.metric("Total Protein", f"{nutrients['Macro']['Protein']['current']}g", "🎯 Goal Met")
    c3.metric("Total Fats", f"{nutrients['Macro']['Fats']['current']}g", "Stable")
    
    with c4:
        st.write("**💎 Micro-Matrix**")
        for key, val in nutrients['Micro'].items():
            st.caption(f"{key}: {val['current']}{val['unit']}")

    # ROW 2: ANIMATED PROGRESS BARS (Style of Image 14)
    st.write("### 📈 Nutrient Saturation")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("**Core Macros**")
        for m, data in nutrients['Macro'].items():
            perc = min(data['current'] / data['goal'], 1.0)
            st.write(f"{m} ({data['current']}/{data['goal']}{data['unit']})")
            st.progress(perc)

    with col_b:
        st.markdown("**Bio-Optimizers**")
        for m, data in nutrients['Micro'].items():
            perc = min(data['current'] / data['goal'], 1.0)
            st.write(f"{m} ({data['current']}/{data['goal']}{data['unit']})")
            st.progress(perc)

with tab2:
    st.subheader("🍱 Tactical Nutrition Options")
    m1, m2, m3 = st.columns(3)
    
    with m1:
        with st.expander("🍎 LIGHT MEAL (2:30 PM)"):
            st.write("• 1 Apple + 1 Banana\n• 5 Almonds + 1 Walnut")
    
    with m2:
        with st.expander("🍗 MAIN LOAD (9:00 PM)"):
            st.write("• 400g Chicken (15g Butter)\n• 150g Dahi + 3 Eggs\n• 1 Roti + Cucumber")
            st.info("Good Monk Sachet #1 Integrated")

    with m3:
        with st.expander("🥦 ALT MAIN (Veggie Swap)"):
            st.write("• 400g Chicken + 5g Butter\n• Sautéed Onion/Capsicum/Carrot\n• 50g Cauliflower\n• 150g Dahi + 3 Eggs")
            st.info("Good Monk Sachet #2 Integrated")

with tab3:
    st.subheader("🕒 The 1PM - 4AM Cycle Progress")
    # THE BLUE LINES: Depict phase completion based on current time
    schedule = [
        ("01:00 PM", "Wake & Hydrate", 1.0),
        ("02:30 PM", "Light Meal", 0.9),
        ("05:00 PM", "Iced Americano", 0.7),
        ("08:30 PM", "Flax Seed Primer", 0.5),
        ("09:00 PM", "Main Power Meal", 0.4),
        ("10:00 PM", "Supplements (Zinc/C/Omega)", 0.3),
        ("01:00 AM", "Isabgol Sweep", 0.1),
        ("04:00 AM", "Sleep Repair", 0.05)
    ]
    
    for time, event, prog in schedule:
        st.write(f"**{time}** | {event}")
        st.progress(prog)

# --- FOOTER ---
st.divider()
if water < 4.0:
    st.error(f"⚠️ DANGER: Water at {water}L. Increase to 4.5L to process {nutrients['Macro']['Protein']['current']}g Protein.")
else:
    st.success(f"✅ System Nominal: {water}L Hydration Verified.")
