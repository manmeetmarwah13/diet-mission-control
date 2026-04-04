import streamlit as st
import pandas as pd
import json
import plotly.graph_objects as go

# --- DASHBOARD CONFIG ---
st.set_page_config(page_title="Mission Control: Full Spectrum", layout="wide")

# --- NAVIGATION ---
page = st.sidebar.radio("Navigate", ["📊 Live Dashboard", "🍱 The Meal Vault"])

# --- DATA: INTAKE VS UPPER LIMITS ---
# Comprehensive list of all metrics with units
metrics_data = {
    "Nutrient": ["Calories", "Protein", "Carbs", "Fats", "Fiber", "Iron", "Zinc", "Vitamin D", "Magnesium", "Omega-3"],
    "Current": [1950, 141, 90, 70, 38, 34, 13.5, 8900, 300, 1800],
    "Limit": [2300, 140, 130, 80, 40, 19, 17, 2000, 440, 500],
    "Unit": ["kcal", "g", "g", "g", "g", "mg", "mg", "IU", "mg", "mg"]
}
df = pd.DataFrame(metrics_data)

# --- PAGE 1: LIVE DASHBOARD ---
if page == "📊 Live Dashboard":
    st.title("🛡️ Mission Control: System Diagnostics")
    
    # Section 1: Core Macros (Progress Bar Layout)
    st.subheader("🚀 Live Status: Core Macros")
    
    # We focus on the 5 core items you requested
    core_items = ["Calories", "Protein", "Carbs", "Fats", "Fiber"]
    
    for item in core_items:
        row = df[df["Nutrient"] == item].iloc[0]
        current = row["Current"]
        limit = row["Limit"]
        unit = row["Unit"]
        progress = min(current / limit, 1.0)
        
        # Displaying with a custom progress bar label
        st.write(f"**{item}**: {current} / {limit} {unit}")
        st.progress(progress)
    
    st.divider()

    # Section 2: Full Spectrum Interactive Chart
    st.subheader("🌡️ Intake vs. Upper Limits")
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

# --- PAGE 2: THE MEAL VAULT (DEDICATED COLUMNAR VIEW) ---
elif page == "🍱 The Meal Vault":
    st.title("🍱 The Meal Vault & Daily Protocol")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🕒 Feeding Schedule (1 PM - 4 AM)")
        st.markdown("""
        ### **1:00 PM - Metabolic Trigger**
        - 500ml Water (Jeera/Coriander Rotation)
        
        ### **2:00 PM - The Nutrient Break**
        - 1 Banana + 150g Papaya/Apple
        - 5 Soaked Almonds + 1 Walnut
        - **Supp:** 1x HK Vitals Multivitamin
        
        ### **9:00 PM - The Power Meal**
        - **MWF:** 400g Chicken (Iron Pan) + 300g Curd + 2 Eggs + Roti
        - **TTS:** 400g Chicken + 300g Curd + Sautéed Veggies
        - **Supp:** 2x Omega-3 + 2x Good Monk
        """)

    with col2:
        st.header("🌙 Nightly Protocol")
        st.markdown("""
        ### **3:15 AM - The Wind-Down**
        - Magnesium Glycinate (250-400mg)
        
        ### **3:45 AM - Nightly Cleanse**
        - 1 Spoon Isabgol in 250ml Water
        """)
        
        st.warning("**Diagnostic Alert:** Current intake is low on Calcium (450mg vs 1000mg) and Potassium. Consider adding leafy greens to the TTS chicken rotation.")

# --- SIDEBAR EXPORT ---
st.sidebar.divider()
if st.sidebar.button("🚀 Sync to diet_sync.json"):
    sync_data = df.set_index("Nutrient")["Current"].to_dict()
    st.sidebar.download_button("Download JSON", json.dumps(sync_data), "diet_sync.json")    "calories": cur_cal, "protein": cur_pro, "carbs": cur_carb, 
    "fats": cur_fat, "fiber": cur_fiber, "unit": "standard"
}

st.download_button(
    label="🚀 Export diet_sync.json for Apple Health",
    data=json.dumps(sync_data),
    file_name="diet_sync.json",
    mime="application/json"
)
