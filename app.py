import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- UI CONFIG ---
st.set_page_config(page_title="90KG Mission Control", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    [data-testid="stMetric"] {
        background-color: #ffffff; border: 1px solid #dee2e6;
        padding: 15px; border-radius: 12px;
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
    water = st.sidebar.slider("Water Intake (L)", 0.0, 5.0, 4.1)
    steps = st.sidebar.number_input("Step Count", value=1000)

    # THE 4-COLUMN LAYOUT
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Daily Calories", "1445 kcal", "-1155 vs TDEE")
    c2.metric("Target Protein", "141g", "🎯 Peak")
    c3.metric("Macro Balance", "87g Carb / 82g Fat", "Optimal")
    
    # 4th Column: Detailed Nutrients & Minerals Matrix
    with c4:
        st.write("**💎 Total Nutrients**")
        st.caption("Daily Aggregated Intake")
        nutrients = {
            "Fiber": "35g",
            "Ashwagandha": "135mg",
            "Probiotics": "260 Cr",
            "Magnesium": "420mg",
            "Zinc": "3.4mg",
            "Iron": "11.2mg",
            "Vit D3": "60k IU",
            "Vit B12": "1.5mcg"
        }
        for n, q in nutrients.items():
            st.write(f"**{n}:** {q}")

    # ANIMATED CHART
    st.write("### 📈 Nutrient Saturation")
    data = {"Item": ["Protein", "Carbs", "Fats", "Fiber", "Mg", "Zn"],
            "Current": [141, 87, 82, 35, 420, 3.4],
            "Goal": [140, 150, 85, 30, 420, 11]}
    df = pd.DataFrame(data)
    df['%'] = (df['Current'] / df['Goal']) * 100
    fig = go.Figure(go.Bar(x=df['Item'], y=df['%'], marker_color='#2ecc71', text=df['Current']))
    fig.update_layout(height=300, margin=dict(t=0, b=0), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🍱 Tactical Nutrition (Restored)")
    m1, m2, m3 = st.columns(3)
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
    with m3:
        with st.expander("🥦 ALT MAIN (Veggie Swap)"):
            st.write("- 400g Chicken (15g Butter)")
            st.write("- Sautéed Onion/Capsicum/Carrot")
            st.write("- 50g Cauliflower")
            st.write("- 150g Dahi + 3 Eggs")

with tab3:
    st.subheader("🕒 The 1PM - 4AM Cycle Progress")
    # THE BLUE LINES: These show completion % of your day
    tasks = [("01:00 PM", "Wake & Hydrate", 1.0), ("02:30 PM", "Light Meal", 0.8), 
             ("05:00 PM", "Americano", 0.6), ("09:00 PM", "Main Load", 0.3)]
    for time, task, p in tasks:
        st.write(f"**{time}** | {task}")
        # Color changes based on progress
        bar_color = "green" if p > 0.5 else "blue"
        st.progress(p)

# --- FOOTER STATUS ---
st.divider()
if water < 3.5:
    st.warning(f"⚠️ LOW HYDRATION: {water}L. Increase intake!")
else:
    st.success(f"✅ SYSTEM NOMINAL: {water}L Hydration Verified.")
