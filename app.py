import streamlit as st

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="90KG Mission Control", page_icon="⚡", layout="wide")

# --- STYLING (Matching Blue Gradient Progress Bars) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    [data-testid="stMetric"] {
        background-color: #ffffff; border: 1px solid #dee2e6;
        padding: 15px; border-radius: 12px;
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00f2fe 0%, #4facfe 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# --- NUTRITION DATA ENGINE ---
nutrients = {
    "Macronutrients": {
        "Calories": {"current": 1625, "target": 2600, "unit": "kcal"},
        "Protein": {"current": 140, "target": 140, "unit": "g"},
        "Fats": {"current": 60, "target": 70, "unit": "g"},
        "Fiber": {"current": 25, "target": 30, "unit": "g"},
        "Carbs": {"current": 80, "target": 200, "unit": "g"}
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
st.divider()

# --- NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    # ROW 1: TOP METRICS (Added Fiber Intake here as requested)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Calories", "1625 kcal", "-975 vs TDEE")
    c2.metric("Protein", "140g", "🎯 Target Hit")
    c3.metric("Fiber Intake", "25g", "Target: 30g")
    c4.metric("Burn Status", "Fat Oxidation", "🔥 Active")

    st.write("### 📈 Nutrient Saturation")
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("**Core Macros**")
        for item, data in nutrients["Macronutrients"].items():
            progress = min(data['current'] / data['target'], 1.0)
            st.write(f"{item} ({data['current']}/{data['target']} {data['unit']})")
            st.progress(progress)

    with col_right:
        st.markdown("**💎 Mineral & Vitamin Matrix**")
        # Integrated directly into the Live Dashboard column as requested
        st.caption("Daily Bio-Optimization Status")
        m1, m2 = st.columns(2)
        with m1:
            st.write("• **Probiotics:** 260 Cr")
            st.write("• **Ashwagandha:** 135mg")
            st.write("• **Magnesium:** 250mg")
        with m2:
            st.write("• **Omega-3:** 660mg")
            st.write("• **Vitamin D3:** 60k IU (W)")
            st.write("• **Vitamin C:** 90mg")

with tab2:
    st.subheader("🍱 Tactical Nutrition")
    # Clean 1-line food entries as requested
    col_a, col_b = st.columns(2)
    
    with col_a:
        with st.expander("🍎 FIRST MEAL (02:30 PM)"):
            st.write("1 Apple + 1 Banana + 5 Almonds + 1 Walnut")
            
        with st.expander("🥛 PRE-MEAL (08:30 PM)"):
            st.write("1 Spoon Flax Seeds + 250ml Water")

    with col_b:
        with st.expander("🍗 SECOND MEAL (09:00 PM)"):
            st.write("400g Chicken (15g Butter) + 150g Dahi + 3 Eggs + 1 Roti + 1 Cucumber")
            st.info("Includes Good Monk Sachet #1 & #2")

        with st.expander("🥗 ALT SECOND MEAL (09:00 PM)"):
            st.write("400g Chicken (5g Butter) + 150g Dahi + 3 Eggs + Cucumber + Sautéed Veggies (Onion/Capsicum/Beans/Carrot) + 50g Cauliflower")
            st.info("Includes Good Monk Sachet #1 & #2")

with tab3:
    st.subheader("🕒 The 1PM - 4AM Cycle Progress")
    # Updated Timeline and Terminology
    timeline = [
        ("01:00 PM", "Wake Up", 1.0),
        ("02:30 PM", "First Meal", 0.85),
        ("05:00 PM", "Coffee/Tea", 0.70),
        ("08:30 PM", "Pre-Meal", 0.50),
        ("09:00 PM", "Second Meal", 0.40),
        ("10:00 PM", "Vitamins & Minerals", 0.25),
        ("01:00 AM", "Fibre Intake", 0.10)
    ]
    
    for time, event, prog in timeline:
        col_t, col_p = st.columns([1, 4])
        with col_t:
            st.write(f"**{time}**")
        with col_p:
            st.write(event)
            st.progress(prog)

# --- FOOTER ---
st.divider()
st.sidebar.header("Telemetry Input")
water = st.sidebar.slider("Water Intake (Liters)", 0.0, 6.0, 4.16)
if water < 4.0:
    st.sidebar.warning("⚠️ Increase water for high protein processing.")
else:
    st.sidebar.success("✅ Hydration Optimal.")
