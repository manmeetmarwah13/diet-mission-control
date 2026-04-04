import streamlit as st
import pandas as pd
import json

# --- DASHBOARD CONFIG ---
st.set_page_config(page_title="Mission Control: Full Stack", layout="wide")
st.title("🛡️ Mission Control: Consuming vs. Upper Limits")

# --- DATA SOURCE: EST. INTAKE VS TARGETS/LIMITS ---
# Based on your latest nutrient analysis
metrics = {
    "Calories": {"current": 1950, "target": 2300, "unit": "kcal", "status": "Deficit (Loss)"},
    "Protein": {"current": 141, "target": 140, "unit": "g", "status": "Optimal"},
    "Carbs": {"current": 90, "target": 130, "unit": "g", "status": "Low (Fat Loss)"},
    "Fats": {"current": 70, "target": 80, "unit": "g", "status": "Optimal"},
    "Fiber": {"current": 38, "target": 40, "unit": "g", "status": "Excellent"},
    "Iron": {"current": 34, "target": 19, "unit": "mg", "status": "High (Safe)"},
    "Zinc": {"current": 13.5, "target": 17, "unit": "mg", "status": "Slight Gap"},
    "Vitamin D": {"current": 8900, "target": 2000, "unit": "IU", "status": "Corrective"},
    "Magnesium": {"current": 300, "target": 440, "unit": "mg", "status": "Filling Gap"},
    "Omega-3": {"current": 1800, "target": 500, "unit": "mg", "status": "Therapeutic"}
}

# --- SECTION 1: SYSTEM DIAGNOSTICS (THE LIMITS) ---
st.subheader("📊 Full Spectrum: Intake vs. Upper Limits")

# Creating a comparison table for quick scanning
df_data = []
for nutrient, data in metrics.items():
    df_data.append({
        "Nutrient": nutrient,
        "Current Consuming": f"{data['current']} {data['unit']}",
        "Target/Limit": f"{data['target']} {data['unit']}",
        "Status": data['status']
    })

st.table(pd.DataFrame(df_data))

st.divider()

# --- SECTION 2: LIVE CONSUMPTION TRACKER ---
st.subheader("⚡ Live Input")
col_input1, col_input2, col_input3 = st.columns(3)

with col_input1:
    cur_cal = st.number_input("Calories In", value=metrics["Calories"]["current"])
    cur_pro = st.number_input("Protein In (g)", value=metrics["Protein"]["current"])
with col_input2:
    cur_water = st.slider("Water Intake (L)", 0.0, 6.0, 4.0)
    cur_mag = st.number_input("Magnesium (mg)", value=metrics["Magnesium"]["current"])
with col_input3:
    st.write("**Quick Checklist:**")
    st.checkbox("1:00 PM Water/Jeera", value=True)
    st.checkbox("9:00 PM Power Meal", value=True)
    st.checkbox("3:45 AM Isabgol Cleanse")

# --- SECTION 3: VISUAL LIMIT GAUGES ---
st.divider()
st.subheader("🌡️ Performance Gauges")
g1, g2, g3 = st.columns(3)

# Progress bars to show how close you are to the limit/target
g1.write(f"**Protein Target ({metrics['Protein']['target']}g)**")
g1.progress(min(cur_pro/metrics['Protein']['target'], 1.0), text=f"{cur_pro}g")

g2.write(f"**Calorie Limit ({metrics['Calories']['target']} kcal)**")
g2.progress(min(cur_cal/metrics['Calories']['target'], 1.0), text=f"{cur_cal} kcal")

g3.write(f"**Magnesium Goal ({metrics['Magnesium']['target']}mg)**")
g3.progress(min(cur_mag/metrics['Magnesium']['target'], 1.0), text=f"{cur_mag}mg")

# --- SECTION 4: EXPORT ---
st.divider()
if st.button("🚀 Finalize & Export Sync File"):
    sync_out = {"calories": cur_cal, "protein": cur_pro, "water": cur_water, "magnesium": cur_mag}
    st.download_button("Download JSON", json.dumps(sync_out), "diet_sync.json")
