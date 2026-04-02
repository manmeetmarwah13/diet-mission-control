import streamlit as st
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests

# --- CONFIG & THEME ---
st.set_page_config(page_title="Mission Control 90KG", page_icon="⚡", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# High-end Animations
lottie_health = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_5njp3v83.json") # Heartbeat
lottie_loading = load_lottieurl("https://assets1.apps.lottiefiles.com/datafiles/bZ97S67Xf0S6Z6G/data.json") # Processing

# --- CUSTOM CSS FOR ANIMATIONS ---
st.markdown("""
    <style>
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .stMetaData { animation: fadeIn 2s; }
    .main { background-color: #0e1117; }
    div.stButton > button:first-child {
        background-color: #00f2fe; color: black; border-radius: 20px;
        transition: all 0.3s ease-in-out;
    }
    div.stButton > button:hover { transform: scale(1.05); background-color: #4facfe; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
with st.container():
    left, right = st.columns([3, 1])
    with left:
        st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
        st.subheader("System Status: Peak Performance Mode")
    with right:
        st_lottie(lottie_health, height=100, key="heart")

# --- INTERACTIVE DASHBOARD TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Live Metrics", "🍱 Meal Vault", "🕒 Time-Stream"])

with tab1:
    # Sidebar Logic moved to metrics
    st.sidebar.header("Telemetry Input")
    water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 2.5)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Deficit", "-1155 kcal", "🔥 Optimal")
    col2.metric("Protein Saturation", "141g", "🎯 Goal Met")
    col3.metric("Ketosis Level", "Moderate", "📈 Increasing")

    # Animated Chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = water,
        title = {'text': "Hydration Status (Liters)"},
        gauge = {'axis': {'range': [0, 5]}, 'bar': {'color': "#00f2fe"}}
    ))
    fig.update_layout(paper_bgcolor="#0e1117", font={'color': "white"}, height=300)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.write("### 🍱 Tactical Nutrition Breakdown")
    st.write("Click each category to see the precise fuel components.")
    
    with st.expander("🍎 LIGHT MEAL (2:30 PM)"):
        st.write("""
        * **1 Apple** (Medium)
        * **1 Banana** (Medium)
        * **5 Almonds** (Soaked preferred)
        * **1 Walnut**
        * **Supplement:** HK Multivitamin + Good Monk Sachet #1
        """)
        st.progress(20)

    with st.expander("🍗 MAIN LOAD (9:00 PM)"):
        st.write("""
        * **400g Chicken Breast** (Sauteed in 15g Amul Butter)
        * **150g Amul Dahi** (Curd)
        * **2 Egg Whites + 1 Whole Egg**
        * **1 Cucumber** (Sliced)
        * **1 Roti** (Whole Wheat)
        * **Supplement:** 2x Omega-3 + Good Monk Sachet #2
        """)
        st.progress(85)

    with st.expander("🥦 ALT MAIN LOAD (Veggie Swap)"):
        st.write("""
        * **400g Chicken Breast** (15g Butter)
        * **Sautéed Veggies** (Onion + Capsicum + Beans/Carrot)
        * **50g Cauliflower** (5g Butter)
        * **2 Egg Whites + 1 Whole Egg**
        * **150g Amul Dahi**
        """)
        st.progress(75)

with tab3:
    st.write("### 🕒 The 1PM - 4AM Cycle")
    # Using a professional vertical timeline aesthetic
    items = [
        ("1:00 PM", "🟢 System Wake & Hydrate"),
        ("2:30 PM", "🍎 Light Fuel Intake"),
        ("5:00 PM", "☕ Caffeine Spike (Iced Americano)"),
        ("8:30 PM", "🛡️ Flax Seed Primer"),
        ("9:00 PM", "🥩 Massive Protein Load"),
        ("1:00 AM", "🧹 Digestive Sweep (Isabgol)"),
        ("4:00 AM", "💤 Shutdown & Fat Oxidation")
    ]
    for time, event in items:
        st.write(f"**{time}** — {event}")
        st.divider()

# --- FOOTER WARNINGS ---
if water < 3.5:
    st.error("⚠️ CRITICAL: Low Hydration detected. Increase water to protect kidneys from high protein urea.")
else:
    st.success("✅ System Nominal. Hydration levels supporting protein synthesis.")
