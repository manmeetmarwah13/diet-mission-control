import streamlit as st

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="90KG Mission Control", page_icon="⚡", layout="wide")

# --- UI STYLING ---
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
    /* Alert Colors */
    .critical { color: #e74c3c; font-weight: bold; }
    .warning { color: #f39c12; font-weight: bold; }
    .optimal { color: #2ecc71; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- ADVANCED NUTRIENT ENGINE (New Targets Applied) ---
nutrients = {
    "Macronutrients": {
        "Calories": {"current": 1625, "target": 2600, "unit": "kcal"},
        "Protein": {"current": 141, "target": 140, "unit": "g"},
        "Fats": {"current": 60, "target": 70, "unit": "g"},
        "Carbs": {"current": 80, "target": 150, "unit": "g"}, # Updated Target
        "Fiber": {"current": 25, "target": 30, "unit": "g"},
        "Sodium": {"current": 800, "target": 2500, "unit": "mg"} # New Addition
    },
    "Micronutrients": {
        "Vitamin C": {"current": 90, "target": 90, "unit": "mg"},
        "Vitamin A": {"current": 700, "target": 900, "unit": "mcg"},
        "Vitamin B12": {"current": 1.2, "target": 2.4, "unit": "mcg"}, # Renamed
        "Vitamin D": {"current": 8500, "target": 4000, "unit": "IU", "note": "(Weekly dose averaged)"}, # Context Added
        "Omega-3": {"current": 660, "target": 1000, "unit": "mg"},
        "Iron": {"current": 11, "target": 18, "unit": "mg"},
        "Calcium": {"current": 800, "target": 1000, "unit": "mg"},
        "Zinc": {"current": 9, "target": 12, "unit": "mg"},
        "Potassium": {"current": 3200, "target": 3500, "unit": "mg"}, # Updated Target
        "Magnesium": {"current": 250, "target": 400, "unit": "mg"} 
    }
}

# --- HEADER ---
st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
st.divider()

tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    # ROW 1: TOP METRICS
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Calories", f"{nutrients['Macronutrients']['Calories']['current']} kcal", "-975 vs TDEE")
    c2.metric("Protein", f"{nutrients['Macronutrients']['Protein']['current']}g", "🎯 Goal Met")
    
    # DEFICIENCY ALERT ENGINE LOGIC
    low_nutrients = []
    for cat in nutrients:
        for item, data in nutrients[cat].items():
            perc = (data['current'] / data['target'])
            if perc < 0.75:
                low_nutrients.append(f"{item} ({int(perc*100)}%)")

    with c3:
        st.write("**🛡️ Deficiency Alert Engine**")
        if low_nutrients:
            st.error(f"Low Levels: {', '.join(low_nutrients)}")
        else:
            st.success("All Systems Optimized")
            
    c4.metric("Burn Status", "Fat Oxidation", "🔥 Active")

    st.write("### 📈 Nutrient Saturation")
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
            
            # Special Highlight for Magnesium
            label = f"**{item}**"
            if item == "Magnesium":
                label = f"🔴 **MAGNESIUM (CRITICAL)**"
            
            st.write(f"{label}: {data['current']} / {data['target']} {data['unit']}")
            if "note" in data:
                st.caption(data['note'])
            st.progress(progress)

with tab2:
    st.subheader("🍱 Tactical Nutrition (Line-by-Line)")
    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🍎 FIRST MEAL (02:30 PM)"):
            st.write("1 Apple", "1 Banana", "5 Almonds", "1 Walnut")
        with st.expander("☕ TEA/COFFEE (05:00 PM)"):
            st.write("250ml Iced Americano", "OR 1 Cup Black Coffee", "OR 1 Cup Tea with Stevia Sugar")
        with st.expander("🥛 PRE-MEAL (08:30 PM)"):
            st.write("1 Spoon Flax Seeds", "250ml Water")
    with col_b:
        with st.expander("🍗 SECOND MEAL (09:00 PM)"):
            st.write("400g Chicken Breast Sautéed (15g Butter)", "150g Amul Dahi", "3 Eggs (2 Boiled Egg Whites + 1 Whole Egg)", "1 Roti", "1 Cucumber")
            st.info("Includes Good Monk Sachet #1 & #2")
        with st.expander("🥗 ALT SECOND MEAL (09:00 PM)"):
            st.write("400g Chicken Breast Sautéed (15g Butter)", "150g Amul Dahi", "3 Eggs (2 Boiled Egg Whites + 1 Whole Egg)", "Sautéed Veggies (Onion + Capsicum with Beans or Carrot)", "50g Boiled Cauliflower Sautéed (5g Butter)", "1 Cucumber")
            st.info("Includes Good Monk Sachet #1 & #2")

with tab3:
    st.subheader("🕒 Daily Execution Timeline")
    timeline = [("01:00 PM", "Wake Up", 1.0), ("02:30 PM", "First Meal", 0.85), ("05:00 PM", "Tea/Coffee", 0.70), ("08:30 PM", "Pre-Meal", 0.50), ("09:00 PM", "Second Meal", 0.40), ("10:00 PM", "Vitamins & Minerals", 0.25), ("01:00 AM", "Fibre Intake", 0.10)]
    for time, event, prog in timeline:
        col_t, col_p = st.columns([1, 4])
        with col_t: st.write(f"**{time}**")
        with col_p: st.write(event); st.progress(prog)

st.sidebar.header("Daily Telemetry")
water = st.sidebar.slider("Water Intake (Liters)", 0.0, 6.0, 4.16)
if water < 4.5: st.sidebar.warning("⚠️ Increase water")
else: st.sidebar.success("✅ Hydration Optimal")
