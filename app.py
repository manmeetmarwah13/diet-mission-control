import streamlit as st

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="90KG Mission Control", page_icon="⚡", layout="wide")

# --- STYLING (Blue Gradient Progress Bars) ---
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

# --- COMPREHENSIVE NUTRIENT ENGINE ---
# Targets based on high-protein weight loss requirements for 114kg male
nutrients = {
    "Macronutrients": {
        "Calories": {"current": 1625, "target": 2600, "unit": "kcal"},
        "Protein": {"current": 140, "target": 140, "unit": "g"},
        "Fats": {"current": 60, "target": 70, "unit": "g"},
        "Carbs": {"current": 80, "target": 200, "unit": "g"},
        "Fiber": {"current": 25, "target": 30, "unit": "g"}
    },
    "Micronutrients": {
        "Vitamin C": {"current": 90, "target": 90, "unit": "mg"},
        "Vitamin A": {"current": 700, "target": 900, "unit": "mcg"},
        "Vitamin B-Complex": {"current": 1.2, "target": 2.4, "unit": "mcg"},
        "Vitamin D": {"current": 8500, "target": 4000, "unit": "IU"},
        "Omega-3": {"current": 660, "target": 1000, "unit": "mg"},
        "Iron": {"current": 11, "target": 18, "unit": "mg"},
        "Calcium": {"current": 800, "target": 1000, "unit": "mg"},
        "Zinc": {"current": 9, "target": 12, "unit": "mg"},
        "Potassium": {"current": 3200, "target": 4700, "unit": "mg"},
        "Magnesium": {"current": 250, "target": 400, "unit": "mg"}
    }
}

# --- HEADER ---
st.title("🚀 WEIGHT LOSS JOURNEY")
st.divider()

# --- NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    # Top Level Quick Stats
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Calories", f"{nutrients['Macronutrients']['Calories']['current']} kcal", "-975 vs TDEE")
    c2.metric("Protein", f"{nutrients['Macronutrients']['Protein']['current']}g", "🎯 Target Hit")
    c3.metric("Fiber Intake", f"{nutrients['Macronutrients']['Fiber']['current']}g", "Target: 30g")
    c4.metric("Burn Status", "Fat Oxidation", "🔥 Active")

    st.write("### 📈 Comprehensive Nutrient Saturation (Current vs Target)")
    
    col_macro, col_micro = st.columns(2)
    
    with col_macro:
        st.markdown("#### **Core Macronutrients**")
        for item, data in nutrients["Macronutrients"].items():
            progress = min(data['current'] / data['target'], 1.0)
            st.write(f"**{item}**: {data['current']} / {data['target']} {data['unit']}")
            st.progress(progress)

    with col_micro:
        st.markdown("#### **Micronutrient Matrix**")
        for item, data in nutrients["Micronutrients"].items():
            progress = min(data['current'] / data['target'], 1.0)
            st.write(f"**{item}**: {data['current']} / {data['target']} {data['unit']}")
            st.progress(progress)

with tab2:
    st.subheader("🍱 Tactical Nutrition (Line-by-Line)")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        with st.expander("🍎 FIRST MEAL (02:30 PM)"):
            st.write("1 Apple")
            st.write("1 Banana")
            st.write("5 Almonds")
            st.write("1 Walnut")
            
        with st.expander("🥛 PRE-MEAL (08:30 PM)"):
            st.write("1 Spoon Flax Seeds")
            st.write("250ml Water")

    with col_b:
        with st.expander("🍗 SECOND MEAL (09:00 PM)"):
            st.write("400g Chicken (15g Butter)")
            st.write("150g Dahi")
            st.write("3 Eggs")
            st.write("1 Roti")
            st.write("1 Cucumber")
            st.info("Includes Good Monk Sachet #1 & #2")

        with st.expander("🥗 ALT SECOND MEAL (09:00 PM)"):
            st.write("400g Chicken (5g Butter)")
            st.write("150g Dahi")
            st.write("3 Eggs")
            st.write("Cucumber")
            st.write("Sautéed Veggies (Onion/Capsicum/Beans/Carrot)")
            st.write("50g Cauliflower")
            st.info("Includes Good Monk Sachet #1 & #2")

with tab3:
    st.subheader("🕒 Daily Execution Timeline")
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

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Daily Telemetry")
water = st.sidebar.slider("Water Intake (Liters)", 0.0, 6.0, 4.16)
if water < 4.0:
    st.sidebar.warning("⚠️ Low Hydration")
else:
    st.sidebar.success("✅ Hydration Optimal")
