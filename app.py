import streamlit as st
import plotly.graph_objects as go

# --- CONFIG ---
st.set_page_config(page_title="Mission Control 90KG", page_icon="⚡", layout="wide")

# --- STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stExpander"] { 
        background-color: #161b22; 
        border: 1px solid #30363d; 
        border-radius: 10px;
    }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
st.markdown("---")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    st.sidebar.header("Telemetry Input")
    water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 2.5)
    steps = st.sidebar.number_input("Step Count", value=1000)

    # Top Metrics
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("Daily Calories", "1445 kcal", "-1155 vs TDEE")
    with c2: st.metric("Protein Intake", "141g", "🎯 100%")
    with c3: st.metric("Burn Status", "Fat Oxidation", "Active")

    # Gauge Chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = water,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Hydration (Liters)"},
        gauge = {'axis': {'range': [None, 5]}, 'bar': {'color': "#00f2fe"}}
    ))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white", 'family': "Arial"}, height=300)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🍱 Tactical Nutrition (Click to Expand)")
    
    with st.expander("🍎 LIGHT MEAL (2:30 PM)"):
        st.write("### Components:")
        st.write("- 1 Apple (Fiber & Pectin)")
        st.write("- 1 Banana (Potassium & Energy)")
        st.write("- 5 Almonds + 1 Walnut (Brain Fats)")
        st.info("💡 Tip: Eat the nuts first to slow down the sugar spike from the fruit.")

    with st.expander("🍗 MAIN LOAD (9:00 PM)"):
        st.write("### Components:")
        st.write("- 400g Chicken Breast (Sautéed in 15g Amul Butter)")
        st.write("- 150g Amul Dahi (Probiotic base)")
        st.write("- 2 Egg Whites + 1 Whole Egg")
        st.write("- 1 Cucumber + 1 Roti")
        st.success("💪 This meal provides ~110g of your total protein.")

    st.markdown("### 🧬 BIO-OPTIMIZATION (Good Monk 2x)")
    # Pulling exactly from your uploaded label
    b1, b2, b3 = st.columns(3)
    b1.metric("Probiotics", "260 Crore", "Gut Health")
    b2.metric("Ashwagandha", "135mg", "Cortisol Control")
    b3.metric("Brahmi", "40mg", "Focus")

with tab3:
    st.subheader("🕒 The 1PM - 4AM Cycle")
    schedule = {
        "01:00 PM": "🟢 Wake Up + Hydrate",
        "02:30 PM": "🍎 Light Meal",
        "05:00 PM": "☕ Iced Americano",
        "08:30 PM": "🛡️ Flax Seed Primer",
        "09:00 PM": "🥩 Main Power Meal",
        "01:00 AM": "🧹 Digestive Sweep (Isabgol)",
        "04:00 AM": "💤 Repair Mode (Sleep)"
    }
    for time, event in schedule.items():
        st.text(f"{time} | {event}")
        st.progress(0) # Visual separator

# --- ALERTS ---
if water < 3.5:
    st.error(f"⚠️ DANGER: Water intake at {water}L. Increase to 4L to flush high-protein urea.")
else:
    st.success("✅ System Nominal. Hydration levels optimized.")
