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
        color: black !important;
        font-weight: 800;
    }}

    .block-container {{
        background-color: rgba(255,255,255,0.80);
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

# ---------------- USER INPUT ----------------
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

# ---------------- FACTS ----------------
facts = [
    "Transport contributes ~25% of global CO₂ emissions.",
    "One tree absorbs ~21kg CO₂ per year.",
    "Cycling produces zero emissions.",
    "Walking is the most eco-friendly transport.",
    "AC usage is a major energy consumer."
]

st.markdown("### 🌍 Environmental Insight")
st.info(random.choice(facts))

# ---------------- CALCULATION ----------------
if st.button("Calculate Footprint"):

    diet_score = {
        "Vegan": 2,
        "Vegetarian": 4,
        "Mixed": 8,
        "High Meat Consumption": 12
    }[diet]

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

    # ---------------- AI ADVISOR (FIXED CLEAN UI) ----------------
    st.markdown("### 🧠 AI Sustainability Advisor")

    if score > 35:
        st.error("High Environmental Impact Detected 🚨")

        st.markdown("**Analysis:**")
        st.write("- High transport usage increases emissions")
        st.write("- Diet contributes significantly")
        st.write("- AC usage increases energy footprint")

        st.markdown("**Recommendations:**")
        st.write("- Reduce car travel & use public transport")
        st.write("- Reduce AC usage by 1–2 hours daily")
        st.write("- Shift towards vegetarian meals")
        st.write("- Use stairs instead of lift")

    elif score > 18:
        st.warning("Moderate Carbon Footprint 🌿")

        st.markdown("**Analysis:**")
        st.write("- Balanced lifestyle with room for improvement")

        st.markdown("**Recommendations:**")
        st.write("- Reduce short car trips")
        st.write("- Increase walking/cycling")
        st.write("- Optimize AC usage")

    else:
        st.success("Excellent Sustainable Lifestyle 🌱")

        st.markdown("**Analysis:**")
        st.write("- Very low carbon footprint lifestyle")

        st.markdown("**Keep Doing:**")
        st.write("- Continue eco-friendly habits")
        st.write("- Maintain walking/cycling routine")
        st.write("- Keep diet sustainable")

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
