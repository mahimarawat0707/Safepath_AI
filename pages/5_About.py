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

/* CARD */
.card {{
    background-color: {card_bg};
    padding: 35px;
    border-radius: 25px;
    box-shadow: 0px 5px 25px {shadow};
    margin-bottom: 30px;
}}

/* SECTION TITLE */
.section-title {{
    color: {title};
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 15px;
}}

/* TEXT */
.info-text {{
    color: {text};
    font-size: 18px;
    line-height: 1.9;
}}

/* TECH BOX */
.tech-box {{
    background-color: {"#fff0f5" if not dark_mode else "#2b2b2b"};
    padding: 18px;
    border-radius: 18px;
    margin-top: 15px;
    color: {text};
    font-size: 18px;
    box-shadow: 0px 3px 15px {shadow};
}}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class="title">
ℹ️ About SafePath AI
</div>

<div class="subtitle">
AI-powered women safety assistant
</div>
""", unsafe_allow_html=True)

# ABOUT CARD
st.markdown(f"""
<div class="card">

<div class="section-title">
🛡️ What is SafePath AI?
</div>

<div class="info-text">

SafePath AI is a smart women safety application designed to help users
during unsafe or emergency situations.

The app provides:

<br><br>

🚨 Emergency SOS activation  
<br>
🤖 AI-powered safety guidance  
<br>
📞 Emergency contact management  
<br>
📍 Safety awareness tips  
<br>
🛰️ Live location-based assistance  

<br><br>

The goal of SafePath AI is to make women feel safer,
more confident, and supported while traveling or being alone.

</div>

</div>
""", unsafe_allow_html=True)

# TECHNOLOGIES
st.markdown(f"""
<div class="card">

<div class="section-title">
⚙️ Technologies Used
</div>

<div class="tech-box">
🐍 Python
</div>

<div class="tech-box">
🎨 Streamlit
</div>

<div class="tech-box">
💎 Gemma 4
</div>

<div class="tech-box">
🦙 Ollama
</div>

</div>
""", unsafe_allow_html=True)

# CREATOR SECTION
st.markdown(f"""
<div class="card">

<div class="section-title">
💖 Built With Passion
</div>

<div class="info-text">

SafePath AI was created to combine Artificial Intelligence
with real-world safety support.

Built with ❤️ by Mahima

</div>

</div>
""", unsafe_allow_html=True)