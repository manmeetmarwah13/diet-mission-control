import streamlit as st
import pandas as pd
import json

# --- DASHBOARD CONFIG ---
st.set_page_config(page_title="Mission Control: Elite", layout="wide")
st.title("🛡️ Mission Control: Optimized Protocol")

# --- DATA SOURCE: LATEST TARGETS ---
TARGETS = {
    "calories": 1950,
    "protein": 140,
    "carbs": 90,
    "fats": 70,
    "fiber": 35,
    "water": 4.0,
    "magnesium": 440,
    "omega3": 1800
}

# --- SIDEBAR: LIVE TRACKING ---
st.sidebar.header("📊 Daily Input")
calories = st.sidebar.number_input("Calories (kcal)", value=TARGETS["calories"])
protein = st.sidebar.number_input("Protein (g)", value=TARGETS["protein"])
carbs = st.sidebar.number_input("Carbs (g)", value=TARGETS["carbs"])
fats = st.sidebar.number_input("Fats (g)", value=TARGETS["fats"])
water = st.sidebar.slider("Water (L)", 0.0, 6.0, 4.0)

# --- SECTION 1: MACRO PERFORMANCE ---
st.subheader("🚀 Live Dashboard: Core Macros")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Calories", f"{calories} kcal", f"{calories - TARGETS['calories']} vs Target")
c2.metric("Protein", f"{protein}g", "Optimal" if 135 <= protein <= 145 else "Adjust")
c3.metric("Carbs", f"{carbs}g", "Fat Loss Zone")
c4.metric("Water", f"{water}L", f"{round(water - TARGETS['water'], 1)}L")

st.divider()

# --- SECTION 2: THE MEAL VAULT (1 PM - 4 AM) ---
st.subheader("🍱 The Meal Vault")
tabs = st.tabs(["🕒 Schedule", "💊 Supplements", "🥗 Micronutrient Status"])

with tabs[0]:
    st.info("**Fast Window:** 4 AM - 1 PM | **Feed Window:** 1 PM - 4 AM")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        **1:00 PM: Metabolic Trigger**
        - Functional Wake-up Water (500ml)
        - *Rotation:* Jeera (M/Th) | Coriander (T/F)
        
        **2:00 PM: The Nutrient Break**
        - 1 Medium Banana + 150g Papaya/Apple
        - 5 Soaked Almonds + 1 Walnut
        """)
    with col_b:
        st.markdown("""
        **9:00 PM: The Power Meal**
        - **MWF:** 400g Chicken (Iron Pan) + 300g Curd + 2 Eggs + Roti
        - **TTS:** 400g Chicken + 300g Curd + Sautéed Veggie Medley
        - *Total 2 tsp Desi Ghee*
        """)

with tabs[1]:
    st.success("Corrective & Maintenance Stack")
    st.write("- **Morning:** 1x HK Vitals Multivitamin")
    st.write("- **9:00 PM:** 2x Omega-3 (1.1g EPA/700mg DHA) + 2x Good Monk")
    st.write("- **3:15 AM:** Magnesium Glycinate/Citrate (250-400mg)")
    st.write("- **3:45 AM:** 1 Spoon Isabgol (Digestive Sweep)")

with tabs[2]:
    st.warning("Focus Areas")
    st.progress(0.45, text="Calcium (Current: 450mg / Target: 1000mg)")
    st.progress(0.51, text="Potassium (Current: 1800mg / Target: 3500mg)")
    st.write("💡 *Tip: Increase leafy greens or coconut water to fix Potassium.*")

# --- SECTION 3: SYNC & EXPORT ---
st.divider()
sync_data = {
    "calories": calories,
    "protein": protein,
    "carbs": carbs,
    "fats": fats,
    "water": water,
    "magnesium": 300, # Estimated current supplement + diet
    "timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")
}

st.download_button(
    label="📲 Export to diet_sync.json",
    data=json.dumps(sync_data),
    file_name="diet_sync.json",
    mime="application/json"
)
