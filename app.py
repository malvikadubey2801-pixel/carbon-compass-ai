import streamlit as st
import base64
import random
from datetime import datetime
import pandas as pd
import plotly.express as px

# ✅ AUTO REFRESH TOOL (correct way)
from streamlit_autorefresh import st_autorefresh

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

    h1, h2, h3, p {{
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

# ---------------- REAL-TIME CLOCK FIX ----------------
st_autorefresh(interval=1000, key="clock")

col1, col2 = st.columns([3, 1])

with col1:
    now = datetime.now().strftime("%d %B %Y | %H:%M:%S")
    st.write("🕒 Current Time:", now)

with col2:
    st.metric("Plant Level", "Seed 🌱")

st.divider()

# ---------------- USER INPUT ----------------
name = st.text_input("Enter Your Name")

occupation = st.selectbox(
    "Occupation",
    ["Student", "Working Professional", "Researcher", "Teacher", "Other"]
)

st.header("🌍 Daily Activity Logger")

car = st.number_input("Car Travel (km)", 0)
bike = st.number_input("Bike Travel (km)", 0)
ac = st.number_input("AC Usage (hours)", 0)
lift = st.number_input("Lift Trips", 0)

# ---------------- CALCULATION ----------------
if st.button("Calculate Footprint"):

    score = (
        car * 0.21 +
        bike * 0.05 +
        ac * 0.5 +
        lift * 0.1
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

    st.metric("Plant Growth", plant)

    # ---------------- AI RECOMMENDATION ----------------
    st.subheader("🧠 AI Advisor")

    if score > 30:
        st.error("High carbon usage ⚠ Reduce AC & car usage")
    elif score > 15:
        st.warning("Moderate footprint 🌿 Try eco-friendly options")
    else:
        st.success("Great job 🌱 Low footprint!")

    # ---------------- GRAPH ----------------
    df = pd.DataFrame({
        "Activity": ["Car", "Bike", "AC", "Lift"],
        "Impact": [
            car * 0.21,
            bike * 0.05,
            ac * 0.5,
            lift * 0.1
        ]
    })

    fig = px.pie(df, names="Activity", values="Impact", title="Carbon Breakdown")
    st.plotly_chart(fig)

# ---------------- DAILY FACT ----------------
facts = [
    "Public transport reduces emissions by 45%",
    "1 tree absorbs ~21kg CO₂ per year",
    "Turning off AC saves energy",
    "Walking reduces pollution instantly",
    "Plastic takes 500+ years to decompose"
]

st.markdown("### 🌍 Environmental Fact")
st.info(random.choice(facts))
