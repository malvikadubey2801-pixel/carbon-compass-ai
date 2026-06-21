import streamlit as st
import base64
import random
from datetime import datetime
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Carbon Compass AI",
    layout="wide"
)

# ---------------- BACKGROUND ----------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    h1, h2, h3 {{
        color: white !important;
    }}

    .block-container {{
        background-color: rgba(0,0,0,0.55);
        padding: 20px;
        border-radius: 15px;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("assets/BG.png")

# ---------------- TITLE ----------------
st.title("🌱 Carbon Compass AI")
st.caption("Track • Reduce • Grow • Sustain")

# ---------------- CLOCK ----------------
now = datetime.now().strftime("%d %B %Y | %H:%M:%S")
st.write("🕒 Current Time:", now)

# ---------------- USER INFO ----------------
name = st.text_input("Enter Your Name")

occupation = st.selectbox(
    "Occupation",
    ["Student", "Working Professional", "Researcher", "Teacher", "Other"]
)

diet = st.selectbox(
    "Diet Type",
    ["Vegan", "Vegetarian", "Mixed", "High Meat Consumption"]
)

st.header("🌍 Daily Activity Logger")

car = st.number_input("Car Travel (km)", 0)
bike = st.number_input("Bike Travel (km)", 0)
ac = st.number_input("AC Usage (hours)", 0)
lift = st.number_input("Lift Trips", 0)

# ---------------- SCIENTIFIC FACTS ----------------
facts = [
    "Transport contributes ~25% of global CO₂ emissions.",
    "One tree absorbs ~21kg CO₂ per year.",
    "AC usage can account for 30% of home electricity.",
    "A 10km car ride emits ~2.4kg CO₂.",
    "Cycling produces zero emissions.",
]

st.markdown("### 🌍 Environmental Insight")
st.info(random.choice(facts))

# ---------------- CALCULATION ----------------
if st.button("Calculate Footprint"):

    # DIET IMPACT (NEW)
    diet_score = {
        "Vegan": 2,
        "Vegetarian": 4,
        "Mixed": 8,
        "High Meat Consumption": 12
    }[diet]

    # OCCUPATION IMPACT (NEW)
    occ_score = {
        "Student": 3,
        "Working Professional": 6,
        "Researcher": 4,
        "Teacher": 5,
        "Other": 5
    }[occupation]

    score = (
        car * 0.21 +
        bike * 0.05 +
        ac * 0.5 +
        lift * 0.1 +
        diet_score +
        occ_score
    )

    st.success(f"🌍 Your Carbon Score: {score:.2f}")

    # ---------------- PLANT GROWTH ----------------
    if score < 10:
        plant = "🌱 Seed"
    elif score < 20:
        plant = "🌿 Sprout"
    elif score < 40:
        plant = "🌳 Tree"
    else:
        plant = "🌲 Forest"

    st.metric("Your Plant Growth", plant)

    # ---------------- AI RECOMMENDATION (DETAILED UPGRADE) ----------------
    st.subheader("🧠 AI Sustainability Advisor")

    if score > 35:
        st.error("🚨 High Environmental Impact Detected")

        st.markdown("""
        **Detailed Analysis:**
        - Your transport usage is high (car + lift)
        - Diet has significant carbon contribution
        - AC usage increases energy footprint

        **AI Recommendations:**
        - Replace 50% car travel with walking/public transport
        - Reduce AC usage by 1–2 hours daily
        - Shift 2–3 meals/week to vegetarian options
        - Take stairs instead of lift whenever possible
        """)

    elif score > 18:
        st.warning("🌿 Moderate Carbon Footprint")

        st.markdown("""
        **Analysis:**
        - Balanced but improvable lifestyle

        **Recommendations:**
        - Reduce short car trips (<3km)
        - Increase walking/cycling frequency
        - Try low-meat meals twice a week
        - Optimize AC usage with timers
        """)

    else:
        st.success("🌱 Excellent Sustainable Lifestyle!")

        st.markdown("""
        Keep it up!
        - You already maintain low emissions
        - Continue using eco-friendly transport
        - Maintain plant-based diet balance
        """)

    # ---------------- GRAPH ----------------
    df = pd.DataFrame({
        "Activity": ["Car", "Bike", "AC", "Lift", "Diet", "Occupation"],
        "Impact": [
            car * 0.21,
            bike * 0.05,
            ac * 0.5,
            lift * 0.1,
            diet_score,
            occ_score
        ]
    })

    fig = px.pie(df, names="Activity", values="Impact",
                 title="Carbon Footprint Breakdown")
    st.plotly_chart(fig, use_container_width=True)
