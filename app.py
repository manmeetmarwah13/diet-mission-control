import streamlit as st
import pandas as pd
import json
import plotly.graph_objects as go

# --- DASHBOARD CONFIG ---
st.set_page_config(page_title="Mission Control: Elite", layout="wide")
st.title("🛡️ Mission Control: Full Spectrum")

# --- DATA: INTAKE VS UPPER LIMITS ---
# Added all units as requested: g, kcal, mg, IU
metrics_data = {
    "Nutrient": ["Calories", "Protein", "Carbs", "Fats", "Fiber", "Iron", "Zinc", "Vitamin D", "Magnesium", "Omega-3"],
    "Current": [1950, 141, 90, 70, 38, 34, 13.5, 8900, 300, 1800],
    "Limit": [2300, 140, 130, 80, 40, 19, 17, 2000, 440, 500],
    "Unit": ["kcal", "g", "g", "g", "g", "mg", "mg", "IU", "mg", "mg"]
}
df = pd.DataFrame(metrics_data)

# --- SIDEBAR: LIVE INPUT ---
st.sidebar.header("⚡ Daily Live Update")
cur_cal = st.sidebar.number_input("Calories (kcal)", value=1950)
cur_pro = st.sidebar.number_input("Protein (g)", value=141)
cur_carb = st.sidebar.number_input("Carbs (g)", value=90)
cur_fat = st.sidebar.number_input("Fats (g)", value=70)
cur_fiber = st.sidebar.number_input("Fiber (g)", value=38)

# --- SECTION 1: INTERACTIVE PERFORMANCE CHART ---
st.subheader("📊 System Diagnostics: Consuming vs. Upper Limit")

# Interactive Bar Chart using Plotly
fig = go.Figure()
fig.add_trace(go.Bar(
    name='Current Consuming',
    x=df['Nutrient'], y=df['Current'],
    marker_color='rgb(55, 83, 109)',
    text=[f"{v} {u}" for v, u in zip(df['Current'], df['Unit'])],
    textposition='auto',
))
fig.add_trace(go.Bar(
    name='Target/Upper Limit',
    x=df['Nutrient'], y=df['Limit'],
    marker_color='rgb(26, 118, 255)',
    text=[f"{v} {u}" for v, u in zip(df['Limit'], df['Unit'])],
    textposition='auto',
))

fig.update_layout(barmode='group', height=500, margin=dict(l=20, r=20, t=20, b=20))
st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- SECTION 2: THE MEAL VAULT & SCHEDULE (RESTORED) ---
st.subheader("🍱 The Meal Vault & Daily Protocol")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### 🕒 Feeding Schedule (1 PM - 4 AM)")
    with st.expander("1:00 PM - Metabolic Trigger", expanded=True):
        st.write("- 500ml Water (Jeera/Coriander Rotation)")
    with st.expander("2:00 PM - The Nutrient Break", expanded=True):
        st.write("- 1 Banana + 150g Papaya/Apple")
        st.write("- 5 Soaked Almonds + 1 Walnut")
        st.write("- **Supp:** 1x HK Vitals Multivitamin")
    with st.expander("9:00 PM - The Power Meal", expanded=True):
        st.write("- **MWF:** 400g Chicken (Iron Pan) + 300g Curd + 2 Eggs + Roti")
        st.write("- **TTS:** 400g Chicken + 300g Curd + Sautéed Veggies")
        st.write("- **Supp:** 2x Omega-3 + 2x Good Monk")

with col_b:
    st.markdown("### 🌙 Nightly Protocol")
    with st.expander("3:15 AM - The Wind-Down"):
        st.write("- Magnesium Glycinate (250-400mg)")
    with st.expander("3:45 AM - Nightly Cleanse"):
        st.write("- 1 Spoon Isabgol in 250ml Water")
    
    st.info("**Current Focus:** Fix Calcium (45% of Target) and Potassium gaps.")

# --- SECTION 3: SYNC EXPORT ---
st.divider()
sync_data = {
    "calories": cur_cal, "protein": cur_pro, "carbs": cur_carb, 
    "fats": cur_fat, "fiber": cur_fiber, "unit": "standard"
}

st.download_button(
    label="🚀 Export diet_sync.json for Apple Health",
    data=json.dumps(sync_data),
    file_name="diet_sync.json",
    mime="application/json"
)
