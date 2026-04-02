import streamlit as st
import plotly.graph_objects as go

# --- PAGE SETUP ---
st.set_page_config(page_title="90KG Mission Control", page_icon="🚀", layout="wide")

# --- CUSTOM THEME ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    div[data-testid="stMetricValue"] { color: #00f2fe; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
st.subheader("System Status: Fat Oxidation Active")

# --- SIDEBAR LOGS ---
st.sidebar.header("Daily Telemetry")
day_type = st.sidebar.selectbox("Current Day Plan", ["Standard (With Roti)", "Alt (Extra Veggies)"])
water_l = st.sidebar.slider("Water Intake (Liters)", 0.0, 5.0, 2.5)
steps = st.sidebar.number_input("Step Count", min_value=0, value=1000)

# --- CALCULATED DATA (USDA/ICMR Based) ---
protein = 141
fats = 82
carbs = 87 if day_type == "Standard (With Roti)" else 65
calories = 1445 if day_type == "Standard (With Roti)" else 1280

# --- TOP METRICS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Calories", f"{calories} kcal", "-1155 vs TDEE")
m2.metric("Protein", f"{protein}g", "Target: 140g")
m3.metric("Carbs", f"{carbs}g", "Low Carb")
m4.metric("Fats", f"{fats}g", "Hormonal Support")

# --- INTERACTIVE MACRO CHART ---
st.write("### 📊 Macro Nutrient Distribution")
fig = go.Figure(data=[go.Pie(
    labels=['Protein', 'Fats', 'Carbs'], 
    values=[protein*4, fats*9, carbs*4], 
    hole=.4,
    marker_colors=['#00f2fe', '#4facfe', '#71e3ff']
)])
fig.update_layout(template="plotly_dark", height=350, margin=dict(l=0, r=0, b=0, t=0))
st.plotly_chart(fig, use_container_width=True)

# --- THE 1PM - 4AM SCHEDULE ---
st.write("### 🕒 Daily Execution Cycle")
with st.container():
    t1, t2 = st.columns(2)
    with t1:
        st.info("**01:00 PM** | 🟢 Wake Up (Hydrate)")
        st.info("**02:30 PM** | 🍎 Light Meal (Apple, Banana, Nuts)")
        st.info("**05:00 PM** | ☕ Iced Americano (Fat Burn)")
        st.info("**08:30 PM** | 🛡️ Flax Seeds Primer")
    with t2:
        st.success("**09:00 PM** | 🍗 Main Load (Chicken, Eggs, Dahi)")
        st.success("**10:00 PM** | 💊 HK Multis + Omega 3")
        st.success("**01:00 AM** | 🧹 Isabgol (Digestive Sweep)")
        st.success("**04:00 AM** | 💤 Sleep (Repair Mode)")

# --- MICRONUTRIENT RADAR (From your Good Monk Screenshot) ---
st.write("### 🧬 Bio-Optimization (Good Monk 2x)")
col_a, col_b, col_c, col_d = st.columns(4)
col_a.metric("Probiotics", "260 Cr", "Gut Health")
col_b.metric("Ashwagandha", "135mg", "Stress Control")
col_c.metric("Brahmi", "40mg", "Focus")
col_d.metric("Vitamin D3", "60k IU", "Weekly")

# --- WARNING SYSTEM ---
st.divider()
if water_l < 3.5:
    st.error(f"⚠️ DANGER: Water is {water_l}L. Kidney stress risk with {protein}g protein! Drink up.")
elif steps < 3000:
    st.warning(f"⚠️ METABOLIC STALL: Current steps ({steps}) are too low. Aim for 3000 to boost loss.")
else:
    st.success("✅ SYSTEM NOMINAL: You are crushing the 90kg goal.")
