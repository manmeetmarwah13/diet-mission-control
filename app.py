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
    </style>
    """, unsafe_allow_html=True)

# --- ADVANCED NUTRIENT ENGINE ---
nutrients = {
    "Macronutrients": {
        "Calories": {"current": 1625, "target": 2600, "unit": "kcal", "type": "intentional"},
        "Protein": {"current": 141, "target": 140, "unit": "g", "type": "core"},
        "Fats": {"current": 60, "target": 70, "unit": "g", "type": "core"},
        "Carbs": {"current": 80, "target": 150, "unit": "g", "type": "intentional"},
        "Fiber": {"current": 25, "target": 30, "unit": "g", "type": "core"},
        "Sodium": {"current": 800, "target": 2500, "unit": "mg", "type": "deficiency"}
    },
    "Micronutrients": {
        "Vitamin C": {"current": 90, "target": 90, "unit": "mg", "type": "core"},
        "Vitamin A": {"current": 700, "target": 900, "unit": "mcg", "type": "core"},
        "Vitamin B12": {"current": 1.2, "target": 2.4, "unit": "mcg", "type": "conditional"},
        "Vitamin D": {"current": 8500, "target": 4000, "unit": "IU", "note": "(Weekly dose averaged)", "type": "core"},
        "Omega-3": {"current": 660, "target": 1000, "unit": "mg", "type": "deficiency"},
        "Iron": {"current": 11, "target": 18, "unit": "mg", "type": "conditional"},
        "Calcium": {"current": 800, "target": 1000, "unit": "mg", "type": "core"},
        "Zinc": {"current": 9, "target": 12, "unit": "mg", "type": "core"},
        "Potassium": {"current": 3200, "target": 3500, "unit": "mg", "type": "core"},
        "Magnesium": {"current": 250, "target": 400, "unit": "mg", "type": "deficiency"}
    }
}

# --- HEADER ---
st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
st.divider()

tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    # ROW 1: TOP METRICS
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Calories", f"{nutrients['Macronutrients']['Calories']['current']} kcal", "-975 (Intentional Deficit)")
    c2.metric("Protein", f"{nutrients['Macronutrients']['Protein']['current']}g", "🎯 100% Target")
    
    # 🚨 REFINED DEFICIENCY ALERT ENGINE
    true_deficiencies = []
    intentional_lows = []
    
    for cat in nutrients:
        for item, data in nutrients[cat].items():
            if (data['current'] / data['target']) < 0.75:
                if data.get('type') == 'deficiency':
                    true_deficiencies.append(item)
                elif data.get('type') in ['intentional', 'conditional']:
                    intentional_lows.append(item)

    with c3:
        st.write("**🛡️ Status Engine**")
        if true_deficiencies:
            st.error(f"🔴 Deficiencies: {', '.join(true_deficiencies)}")
        if intentional_lows:
            st.warning(f"🟡 Intentional/Low: {', '.join(intentional_lows)}")
        if not true_deficiencies and not intentional_lows:
            st.success("System Optimized")
            
    c4.metric("Burn Status", "Fat Oxidation", "🔥 Active")

    st.write("### 📈 Nutrient Saturation")
    col_macro, col_micro = st.columns(2)
    
    with col_macro:
        st.markdown("#### **Core Macronutrients**")
        for item, data in nutrients["Macronutrients"].items():
            progress = min(data['current'] / data['target'], 1.0)
            
            # Smart Sodium Feedback
            suffix = ""
            if item == "Sodium":
                if data['current'] < 1500: suffix = " — ⚠️ Low (Increase Electrolytes)"
                elif data['current'] > 2500: suffix = " — 🚨 High (Reduce Salt)"
                else: suffix = " — ✅ Optimal"
            
            st.write(f"**{item}**: {data['current']} / {data['target']} {data['unit']}{suffix}")
            st.progress(progress)

    with col_micro:
        st.markdown("#### **Micronutrient Matrix**")
        for item, data in nutrients["Micronutrients"].items():
            progress = min(data['current'] / data['target'], 1.0)
            label = f"🔴 **{item.upper()} (CRITICAL)**" if item == "Magnesium" else f"**{item}**"
            st.write(f"{label}: {data['current']} / {data['target']} {data['unit']}")
            if "note" in data: st.caption(data['note'])
            st.progress(progress)

with tab2:
    st.subheader("🍱 Tactical Nutrition (Vertical List)")
    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🍎 FIRST MEAL (02:30 PM)"):
            st.write("1 Apple")
            st.write("1 Banana")
            st.write("5 Almonds")
            st.write("1 Walnut")
        with st.expander("☕ TEA/COFFEE (05:00 PM)"):
            st.write("250ml Iced Americano")
            st.write("OR 1 Cup Black Coffee")
            st.write("OR 1 Cup Tea with Stevia Sugar")
        with st.expander("🥛 PRE-MEAL (08:30 PM)"):
            st.write("1 Spoon Flax Seeds")
            st.write("250ml Water")
    with col_b:
        with st.expander("🍗 SECOND MEAL (09:00 PM)"):
            st.write("400g Chicken Breast Sautéed (15g Butter)")
            st.write("150g Amul Dahi")
            st.write("3 Eggs (2 Boiled Egg Whites + 1 Whole Egg)")
            st.write("1 Roti")
            st.write("1 Cucumber")
            st.info("Includes Good Monk Sachet #1 & #2")
        with st.expander("🥗 ALT SECOND MEAL (09:00 PM)"):
            st.write("400g Chicken Breast Sautéed (15g Butter)")
            st.write("150g Amul Dahi")
            st.write("3 Eggs (2 Boiled Egg Whites + 1 Whole Egg)")
            st.write("Sautéed Veggies (Onion + Capsicum with Beans or Carrot)")
            st.write("50g Boiled Cauliflower Sautéed (5g Butter)")
            st.write("1 Cucumber")
            st.info("Includes Good Monk Sachet #1 & #2")

with tab3:
    st.subheader("🕒 Daily Execution Timeline")
    timeline = [("01:00 PM", "Wake Up", 1.0), ("02:30 PM", "First Meal", 0.85), ("05:00 PM", "Tea/Coffee", 0.70), ("08:30 PM", "Pre-Meal", 0.50), ("09:00 PM", "Second Meal", 0.40), ("10:00 PM", "Vitamins & Minerals", 0.25), ("01:00 AM", "Fibre Intake", 0.10)]
    for time, event, prog in timeline:
        col_t, col_p = st.columns([1, 4])
        with col_t: st.write(f"**{time}**")
        with col_p: st.write(event); st.progress(prog)

# --- SIDEBAR TELEMETRY ---
st.sidebar.header("Daily Telemetry")
water = st.sidebar.slider("Water Intake (Liters)", 0.0, 6.0, 4.1)

if water >= 3.5:
    st.sidebar.success("✅ Hydration optimal")
else:
    st.sidebar.warning(f"⚠️ Hydration Low ({water}L). Target 3.5L+")
