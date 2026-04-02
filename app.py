import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- FORCE THEME & UI FIXES ---
st.set_page_config(page_title="Mission Control 90KG", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 8px 8px 0 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    st.sidebar.header("Telemetry Input")
    water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 2.5)
    steps = st.sidebar.number_input("Step Count", value=1000)

    # 4-COLUMN TOP ROW
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Daily Calories", "1445 kcal", "-1155 vs TDEE")
    c2.metric("Target Protein", "141g", "🎯 100%")
    c3.metric("Target Fats", "82g", "Stable")
    c4.metric("Nutrients & Minerals", "A-Z Mix", "Mg + Zn + Fe")

    # NUTRIENT SATURATION CHART (Miro Style)
    st.write("### 📈 Nutrient Saturation Levels")
    data = {
        "Item": ["Protein", "Carbs", "Fats", "Fiber", "Magnesium", "Zinc", "Vit C"],
        "Current": [141, 87, 82, 28, 380, 12, 95],
        "Goal": [140, 150, 85, 35, 420, 11, 100]
    }
    df = pd.DataFrame(data)
    df['Percent'] = (df['Current'] / df['Goal']) * 100

    fig = go.Figure(go.Bar(
        x=df['Item'], y=df['Percent'],
        marker_color=['#2ecc71' if x >= 90 else '#f1c40f' for x in df['Percent']],
        text=[f"{int(x)}%" for x in df['Percent']],
        textposition='auto',
    ))
    fig.update_layout(yaxis=dict(range=[0, 120]), height=350, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🍱 Tactical Nutrition (Click to Expand)")
    m1, m2 = st.columns(2)
    with m1:
        with st.expander("🍎 LIGHT MEAL (2:30 PM)"):
            st.write("- 1 Apple + 1 Banana")
            st.write("- 5 Almonds + 1 Walnut")
            st.write("- Good Monk Sachet #1")
    with m2:
        with st.expander("🍗 MAIN LOAD (9:00 PM)"):
            st.write("- 400g Chicken (Butter)")
            st.write("- 150g Dahi + 3 Eggs")
            st.write("- 1 Roti + Cucumber")
            st.write("- Good Monk Sachet #2")

    st.write("### 💎 Mineral & Vitamin Matrix")
    n1, n2, n3, n4 = st.columns(4)
    n1.write("**Probiotics:** 260 Crore")
    n1.write("**Ashwagandha:** 135mg")
    n2.write("**Vitamin D3:** 60k IU")
    n2.write("**Magnesium:** 420mg")
    n3.write("**Vitamin C:** 32.4mg")
    n3.write("**B12:** 1.5mcg")
    n4.write("**Zinc:** 3.4mg")
    n4.write("**Iron:** 11.2mg")

with tab3:
    st.subheader("🕒 The 1PM - 4AM Cycle Progress")
    # Progression visual (filling bars based on likely completion)
    tasks = [("01:00 PM", "Wake & Hydrate", 1.0), ("02:30 PM", "Light Meal", 0.85), ("05:00 PM", "Iced Americano", 0.7), 
             ("08:30 PM", "Flax Primer", 0.4), ("09:00 PM", "Main Load", 0.3), ("01:00 AM", "Isabgol", 0.1)]
    
    for time, task, p in tasks:
        st.write(f"**{time}** | {task}")
        st.progress(p)

# --- FINAL STATUS ---
st.divider()
if water < 3.5:
    st.warning(f"⚠️ Low Hydration: {water}L. Aim for 4L.")
else:
    st.success(f"✅ System Nominal: {water}L Hydration.")
