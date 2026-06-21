import streamlit as st
import base64
import random
from datetime import datetime
import plotly.express as px
import pandas as pd

# ---------------- PAGE ----------------
st.set_page_config(page_title="Carbon Compass AI", layout="wide")

# ---------------- BACKGROUND ----------------
def set_bg(image_file):
    try:
        with open(image_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}

            /* DARK PREMIUM TITLE */
            .title {{
                text-align: center;
                font-size: 58px;
                font-weight: 900;
                color: #0B2E13;
                text-shadow: 2px 2px 10px rgba(255,255,255,0.6);
            }}

            .subtitle {{
                text-align: center;
                font-size: 18px;
                color: #1B4332;
                font-weight: 600;
            }}

            /* GLASS UI */
            div[data-testid="stMetric"] {{
                background: rgba(255,255,255,0.85);
                padding: 15px;
                border-radius: 18px;
                box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
            }}

            label {{
                color: #0B2E13 !important;
                font-weight: 600;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        st.warning("Background not found. Check file name.")

# ⚠️ YOUR FILE NAME (IMPORTANT)
set_bg("assets/bg.png.png")

# ---------------- TITLE ----------------
st.markdown("<div class='title'>🌱 Carbon Compass AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Track • Reduce • Grow • Sustain</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- LIVE DATE & TIME (WHITE) ----------------
st.markdown(
    f"""
    <h4 style="
    color:white;
    font-weight:700;
    text-shadow:2px 2px 6px rgba(0,0,0,0.7);
    ">
    ⏰ {datetime.now().strftime('%d %B %Y | %H:%M:%S')}
    </h4>
    """,
    unsafe_allow_html=True
)

# ---------------- USER INPUT ----------------
name = st.text_input("👤 Enter Name")

occupation = st.selectbox(
    "Occupation",
    ["Student", "Professional", "Researcher", "Teacher", "Other"]
)

car = st.number_input("🚗 Car Travel (km)", 0)
bike = st.number_input("🏍 Bike Travel (km)", 0)
ac = st.number_input("❄ AC Usage (hours)", 0)
lift = st.number_input("🛗 Lift Trips", 0)

food = st.selectbox(
    "🍽 Diet",
    ["Vegan", "Vegetarian", "Mixed", "Non-Vegetarian"]
)

# ---------------- FACT SYSTEM ----------------
if "fact_index" not in st.session_state:
    st.session_state.fact_index = 0

facts = [
    "A tree absorbs ~22 kg CO₂ per year.",
    "Public transport reduces emissions by 40%.",
    "LED bulbs save up to 75% energy.",
    "Walking produces almost zero emissions.",
    "Carpooling reduces pollution significantly.",
    "Reducing AC usage saves energy."
]

# ---------------- CALCULATION ----------------
def compute():
    return {
        "Car": car * 0.21,
        "Bike": bike * 0.10,
        "AC": ac * 0.85,
        "Lift": lift * 0.03
    }

# ---------------- MAIN APP ----------------
if st.button("🌍 Analyze My Impact"):

    breakdown = compute()
    total = sum(breakdown.values())

    # ---------------- XP + LEVEL ----------------
    xp = max(0, 500 - total * 10)
    level = int(xp // 100) + 1

    # ---------------- ECO SYSTEM ----------------
    if total < 5:
        persona = "🌲 Climate Champion"
        plant = "🌲 FOREST"

    elif total < 10:
        persona = "🌿 Eco Warrior"
        plant = "🌳 TREE"

    elif total < 20:
        persona = "🌱 Green Learner"
        plant = "🌿 SPROUT"

    else:
        persona = "⚡ Carbon Explorer"
        plant = "🌱 SEED"

    # ---------------- METRICS ----------------
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🌍 Carbon Score", f"{total:.2f}")

    with c2:
        st.metric("⭐ XP", int(xp))

    with c3:
        st.metric("🏆 Level", level)

    with c4:
        st.metric("🌿 Persona", persona)

    # ---------------- ECOSYSTEM ----------------
    st.subheader("🌱 Ecosystem Growth")
    st.markdown(f"# {plant}")

    # ---------------- AI COACH ----------------
    highest = max(breakdown, key=breakdown.get)

    st.subheader("🧠 AI Coach")

    if highest == "AC":
        st.info(f"""
Hi {name},

AC usage is your highest emission source.

Reducing it by 1 hour can significantly improve your footprint.
""")

    elif highest == "Car":
        st.info(f"""
Hi {name},

Transport contributes most to your emissions.

Try walking or public transport for short trips.
""")

    elif highest == "Bike":
        st.info(f"""
Hi {name},

Your travel frequency is high.

Combine trips to reduce emissions.
""")

    else:
        st.info(f"""
Hi {name},

Your emissions are balanced.

Keep improving small habits daily.
""")

    # ---------------- MISSIONS ----------------
    st.subheader("🎯 Daily Missions")

    missions = ["Use reusable bottle", "Avoid plastic bags"]

    if car > 5:
        missions.append("Replace one car trip with walking")

    if ac > 3:
        missions.append("Reduce AC usage by 1 hour")

    for m in missions:
        st.write("✅", m)

    # ---------------- CHART ----------------
    st.subheader("📊 Emission Breakdown")

    df = pd.DataFrame({
        "Source": list(breakdown.keys()),
        "CO2": list(breakdown.values())
    })

    fig = px.pie(df, values="CO2", names="Source", title="Carbon Sources")
    st.plotly_chart(fig, use_container_width=True)

    # ---------------- FACTS BUTTON ----------------
    colA, colB = st.columns([3,1])

    with colB:
        st.markdown("### 🌍 Live Fact")

        st.markdown(
            f"""
            <div style="
            background: rgba(255,255,255,0.85);
            padding: 15px;
            border-radius: 15px;
            min-height: 120px;
            ">
            🌱 {facts[st.session_state.fact_index]}
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("🔄 New Fact"):
            st.session_state.fact_index = (st.session_state.fact_index + 1) % len(facts)

    # ---------------- ACHIEVEMENTS ----------------
    st.subheader("🏆 Achievements")

    if total < 20:
        st.success("🌱 Eco Starter")

    if total < 10:
        st.success("🌿 Green Guardian")

    if total < 5:
        st.success("🌳 Planet Protector")

    # ---------------- FUTURE IMPACT ----------------
    annual = total * 365
    saved = annual * 0.20

    st.subheader("📈 Future Impact")
    st.metric("Potential Annual CO₂ Savings", f"{saved:.0f} kg")