import streamlit as st

# LOAD THEME
dark_mode = st.session_state.get("dark_mode", False)

# LIGHT MODE
if not dark_mode:

    bg = "linear-gradient(to bottom right, #fff0f5, #ffe4ec)"
    card_bg = "white"
    text = "#444444"
    title = "#ff4f81"
    shadow = "rgba(255,105,180,0.2)"

# DARK MODE
else:

    bg = "#000000"
    card_bg = "#1a1a1a"
    text = "#ffffff"
    title = "#ffffff"
    shadow = "rgba(255,255,255,0.1)"

# CSS
st.markdown(f"""
<style>

/* MAIN */
.stApp {{
    background: {bg};
}}

/* HIDE STREAMLIT DEFAULTS */
#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

/* SIDEBAR */
section[data-testid="stSidebar"] {{
    background-color: {"#ffd6e7" if not dark_mode else "#1a1a1a"} !important;
}}

section[data-testid="stSidebar"] * {{
    color: {"#444444" if not dark_mode else "#ffffff"} !important;
}}

/* TITLE */
.title {{
    font-size: 60px;
    font-weight: bold;
    color: {title};
    text-align: center;
    margin-top: 20px;
}}

.subtitle {{
    text-align: center;
    color: {text};
    font-size: 22px;
    margin-bottom: 40px;
}}

/* TIP CARD */
.tip-card {{
    background-color: {card_bg};
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0px 5px 25px {shadow};
    margin-bottom: 25px;
    transition: 0.3s;
}}

.tip-card:hover {{
    transform: scale(1.02);
}}

.tip-title {{
    color: {title};
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 15px;
}}

.tip-text {{
    color: {text};
    font-size: 18px;
    line-height: 1.8;
}}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class="title">
📍 Safety Tips
</div>

<div class="subtitle">
Smart safety advice for everyday situations
</div>
""", unsafe_allow_html=True)

# TIP 1
st.markdown(f"""
<div class="tip-card">

<div class="tip-title">
🚶 Avoid Isolated Places
</div>

<div class="tip-text">
Try to stay in crowded and well-lit areas, especially at night.
Avoid shortcuts through empty roads or dark streets.
</div>

</div>
""", unsafe_allow_html=True)

# TIP 2
st.markdown(f"""
<div class="tip-card">

<div class="tip-title">
📱 Share Live Location
</div>

<div class="tip-text">
Share your live location with trusted friends or family members
when traveling alone or using public transport.
</div>

</div>
""", unsafe_allow_html=True)

# TIP 3
st.markdown(f"""
<div class="tip-card">

<div class="tip-title">
👀 Stay Aware of Surroundings
</div>

<div class="tip-text">
Avoid distractions like loud music while walking alone.
Be aware of nearby people, vehicles, and exits.
</div>

</div>
""", unsafe_allow_html=True)

# TIP 4
st.markdown(f"""
<div class="tip-card">

<div class="tip-title">
🚕 Verify Cab Details
</div>

<div class="tip-text">
Always match the cab number plate and driver details
before entering the vehicle.
</div>

</div>
""", unsafe_allow_html=True)

# TIP 5
st.markdown(f"""
<div class="tip-card">

<div class="tip-title">
🆘 Trust Your Instincts
</div>

<div class="tip-text">
If something feels unsafe, leave the place immediately
and contact someone you trust.
</div>

</div>
""", unsafe_allow_html=True)