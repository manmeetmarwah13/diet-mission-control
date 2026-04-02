import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- FORCE LIGHT THEME & FIXED COLORS ---
st.set_page_config(page_title="Mission Control 90KG", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    /* Force Light Background to fix the "Blackout" issue */
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    
    /* Card Styling */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 2px solid #e9ecef;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 MISSION CONTROL: 114kg ➔ 90kg")
st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📊 LIVE DASHBOARD", "🍱 MEAL VAULT", "🕒 TIME-STREAM"])

with tab1:
    st.sidebar.header("Daily Telemetry")
    water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 2.5)
    steps = st.sidebar.number_input("Step Count", value=1000)

    # 4-COLUMN TOP ROW
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Daily Calories", "1445 kcal", "Deficit: 1155")
    with c2: st.metric("Target Protein", "141g", "🎯 100%")
    with c3: st.metric("Target Fat/Carb", "82g / 87g", "Balanced")
    with c4: st.metric("Nutrients & Minerals", "Complete", "Vit A-Z + Mg")

    # ANIMATED BAR CHART (Similar to Image 3)
    st.write("### 📈 Nutrient Saturation Levels")
    nutrient_data = {
        "Nutrient": ["Protein", "Carbs", "Fats", "Fiber", "Magnesium", "Zinc", "Vit C"],
        "Value": [141, 87, 82, 35, 400, 15, 100],
        "Goal": [140, 150, 85, 30, 420, 11, 90]
    }
    df = pd.DataFrame(nutrient_data)
    df['Percent'] = (df['Value'] / df['Goal']) * 100

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Nutrient'], y=df['Percent'],
        marker_color=['#2ecc71' if x >= 90 else '#f1c40f' for x in df['Percent']],
        text=[f"{int(x)}%" for x in df['Percent']],
        textposition='auto',
    ))
    fig.update_layout(
        title="Daily Goal Fulfillment (%)",
        yaxis=dict(range=[0, 120]),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🍱 Tactical Nutrition (Expand for Details)")
    
    col_meal1, col_meal2 = st.columns(2)
    with col_meal1:
        with st.expander("🍎 LIGHT MEAL (2:30 PM)"):
            st.write("**Contents:**")
            st.write("- 1 Apple + 1 Banana")
            st.write("- 5 Almonds + 1 Walnut")
            st.write("- Good Monk Sachet #1")

    with col_meal2:
        with st.expander("🍗 MAIN LOAD (9:00 PM)"):
            st.write("**Contents:**")
            st.write("- 400g Chicken (Amul Butter)")
            st.write("- 150g Dahi + 3 Eggs")
            st.write("- 1 Cucumber + 1 Roti")
            st.write("- Good Monk Sachet #2")

    # DETAILED MINERAL LIST (Based on Good Monk Label)
    st.write("### 💎 Mineral & Vitamin Matrix")
    m1, m2, m3, m4 = st.columns(4)
    # Data derived from Good Monk label
    m1.write("**Probiotics:** 260 Crore")
    m1.write("**Ashwagandha:** 135mg")
    m2.write("**Vitamin D:** 60,000 IU (Weekly)")
    m2.write("**Magnesium:** (In progress)")
    m3.write("**Vitamin C:** 32.4mg")
    m3.write("**Vitamin B12:** 1.5mcg")
    m4.write("**Zinc:** 3.4mg")
    m4.write("**Iron:** 11.2mg")

with tab3:
    st.subheader("🕒 The 1PM - 4AM Cycle Progress")
    
    # Progress Calculation
    schedule_items = [
        ("01:00 PM", "Wake Up & Hydrate", 1.0),
        ("02:30 PM", "Light Meal", 0.8),
        ("05:00 PM", "Iced Americano", 0.6),
        ("08:30 PM", "Flax Seed Primer", 0.4),
        ("09:00 PM", "Main Power Meal", 0.3),
        ("01:00 AM", "Digestive Sweep", 0.1),
        ("04:00 AM", "Sleep Mode", 0.0)
    ]
    
    for time, event, prog in schedule_items:
        # Determine Color: Green if task is likely done, Yellow/Grey if not
        color = "green" if prog > 0.5 else "orange"
        st.write(f"**{time}** | {event}")
        st.progress(prog) 

# --- STATUS BAR ---
st.divider()
if water < 3.5:
    st.warning(f"⚠️ Status: Low Hydration ({water}L). Target 4L for Protein Processing.")
else:
    st.success(f"✅ Status: Optimal Hydration ({water}L). System Cleared.")    st.sidebar.header("Telemetry Input")
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
