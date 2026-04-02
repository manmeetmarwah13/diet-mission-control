import streamlit as st
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
    /* Animated Progress Bar Styling */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# --- NIN & USDA BENCHMARK ENGINE ---
# Benchmarks adjusted for 114kg male / 6ft height
nutrients = {
    "Macronutrients": {
        "Calories": {"current": 1625, "target": 2600, "unit": "kcal", "status": "Deficit"},
        "Protein": {"current": 140, "target": 140, "unit": "g", "status": "Optimal"},
        "Fats": {"current": 60, "target": 70, "unit": "g", "status": "Hormone Support"},
        "Carbs": {"current": 80, "target": 200, "unit": "g", "status": "Low-Carb Mode"},
        "Fiber": {"current": 25, "target": 30, "unit": "g", "status": "Digestive Strength"}
    },
    "Micronutrients": {
        "Vitamin C": {"current": 90, "target": 90, "unit": "mg"},
        "Zinc": {"current": 9, "target": 12, "unit": "mg"},
        "Magnesium": {"current": 250, "target": 400, "unit": "mg"},
        "Vitamin D": {"current": 8500, "target": 4000, "unit": "IU"},
        "Omega3": {"current": 660, "target": 1000, "unit": "mg"}
    }
}

# --- HEADER ---
st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
st.caption("Standardized against USDA & NIN Benchmarks for 6ft/114kg Male")
st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    st.sidebar.header("Daily Telemetry")
    water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 4.16)
    
    # ROW 1: TOP METRICS (THE 4TH COLUMN INCLUDED)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Current Calories", f"{nutrients['Macronutrients']['Calories']['current']} kcal", "-975 kcal Deficit")
    c2.metric("Protein Intake", f"{nutrients['Macronutrients']['Protein']['current']}g", "🎯 100% Target")
    c3.metric("Burn Status", "Fat Oxidation", "🔥 Active")
    
    with c4:
        st.write("**💎 Micronutrient Gaps**")
        st.caption("Based on NIN/USDA Requirements")
        st.write(f"• **Zinc:** -3mg")
        st.write(f"• **Magnesium:** -150mg")
        st.write(f"• **Omega-3:** -340mg")

    # ROW 2: ANIMATED PROGRESS BARS (Style of Image 14)
    st.write("### 📈 Nutrition Dashboard")
    
    for category, items in nutrients.items():
        st.markdown(f"#### {category}")
        for item, data in items.items():
            col_text, col_bar = st.columns([1, 3])
            with col_text:
                st.write(f"**{item}**")
                st.caption(f"{data['current']}/{data['target']} {data['unit']}")
            with col_bar:
                # Calculate progress and determine color logic
                progress = min(data['current'] / data['target'], 1.0)
                st.progress(progress)
        st.write("") # Padding

with tab2:
    st.subheader("🍱 Tactical Nutrition (Click to Expand)")
    m1, m2 = st.columns(2)
    with m1:
        with st.expander("🍎 LIGHT MEAL (2:30 PM)"):
            st.write("• 1 Apple + 1 Banana\n• 5 Almonds + 1 Walnut\n• Good Monk Sachet #1")
    with m2:
        with st.expander("🍗 MAIN LOAD (9:00 PM)"):
            st.write("• 400g Chicken (15g Butter)\n• 150g Dahi + 3 Eggs\n• 1 Roti + Cucumber\n• Good Monk Sachet #2")

    st.write("### 💎 Mineral & Vitamin Matrix")
    n1, n2, n3, n4 = st.columns(4)
    n1.write("**Probiotics:** 260 Crore")
    n2.write("**Ashwagandha:** 135mg")
    n3.write("**Vitamin D3:** 60k IU (Weekly)")
    n4.write("**Vitamin C:** 32.4mg (Supp)")

with tab3:
    st.subheader("🕒 The 1PM - 4AM Cycle Progress")
    # Time-stream progress bars
    tasks = [("01:00 PM", "Wake & Hydrate", 1.0), ("02:30 PM", "Light Meal", 0.8), 
             ("09:00 PM", "Main Load", 0.4), ("01:00 AM", "Isabgol Sweep", 0.1)]
    for time, task, p in tasks:
        st.write(f"**{time}** | {task}")
        st.progress(p)

# --- FOOTER ---
st.divider()
st.success(f"✅ System Nominal: {water}L Hydration.")
