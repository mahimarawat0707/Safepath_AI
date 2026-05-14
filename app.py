import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="SafePath AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# DARK MODE TOGGLE

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

dark_mode = st.toggle(
    "🌙 Dark Mode",
    value=st.session_state.dark_mode
)

st.session_state.dark_mode = dark_mode

# LIGHT MODE COLORS
if not dark_mode:

    bg = "linear-gradient(to bottom right, #fff0f5, #ffe4ec)"
    sidebar = "#ffd6e7"
    title = "#ff4f81"
    card_bg = "white"
    text = "#444444"
    button = "#ff69b4"
    button_hover = "#ff3f8e"
    shadow = "rgba(255,105,180,0.2)"
    footer = "#ff4f81"
    sidebar_text = "#535353"

# DARK MODE COLORS
else:

    bg = "#000000"
    sidebar = "#000000"
    title = "#ffffff"
    card_bg = "#1a1a1a"
    text = "#ffffff"
    button = "#555555"
    button_hover = "#777777"
    shadow = "rgba(255,255,255,0.1)"
    footer = "#d3d3d3"
    sidebar_text = "#ffffff"

# CUSTOM CSS
st.markdown(f"""
<style>

/* MAIN APP */
.stApp {{
    background: {bg};
}}

/* REMOVE STREAMLIT DEFAULT ELEMENTS */
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
    background-color: {sidebar} !important;
    border-right: 2px solid #333333;
}}

/* SIDEBAR CONTENT */
[data-testid="stSidebarContent"] {{
    background: {sidebar} !important;
}}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {{
    color: {sidebar_text} !important;
    font-size: 18px;
}}

/* SIDEBAR SCROLLBAR */
section[data-testid="stSidebar"] ::-webkit-scrollbar {{
    width: 8px;
}}

section[data-testid="stSidebar"] ::-webkit-scrollbar-track {{
    background: {sidebar};
}}

section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {{
    background: #444444;
    border-radius: 10px;
}}

/* TITLE */
.title {{
    font-size: 70px;
    font-weight: bold;
    color: {title};
    text-align: center;
    margin-top: 20px;
}}

/* SUBTITLE */
.subtitle {{
    text-align: center;
    font-size: 24px;
    color: {text};
    margin-bottom: 50px;
}}

/* CARDS */
.card {{
    background-color: {card_bg};
    padding: 35px;
    border-radius: 25px;
    box-shadow: 0px 5px 25px {shadow};
    text-align: center;
    transition: 0.3s;
    margin-bottom: 20px;
}}

.card:hover {{
    transform: scale(1.03);
}}

/* CARD TITLES */
.card-title {{
    font-size: 28px;
    font-weight: bold;
    color: {title};
    margin-bottom: 15px;
}}

/* CARD TEXT */
.card-text {{
    font-size: 18px;
    color: {text};
    line-height: 1.8;
}}

/* BUTTONS */
.stButton > button {{
    background-color: {button};
    color: white;
    border-radius: 15px;
    border: none;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: bold;
    transition: 0.3s;
}}

.stButton > button:hover {{
    background-color: {button_hover};
    transform: scale(1.05);
}}

/* FOOTER */
.footer {{
    text-align: center;
    color: {footer};
    font-size: 18px;
    margin-top: 50px;
}}

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("### Your Safety, Our Priority")

st.sidebar.markdown("---")

# HERO SECTION
st.markdown("""
<div class="title">
🛡️ SafePath AI
</div>

<div class="subtitle">
AI-powered safety companion for women
</div>
""", unsafe_allow_html=True)

# FEATURE CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">

    <div class="card-title">
    🤖 AI Safety Guidance
    </div>

    <div class="card-text">
    Get intelligent real-time guidance during unsafe situations.
    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">

    <div class="card-title">
    🚨 Emergency SOS
    </div>

    <div class="card-text">
    Quickly activate emergency alerts and support systems.
    </div>

    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">

    <div class="card-title">
    📍 Safety Tips
    </div>

    <div class="card-text">
    Learn practical precautions for travel and emergencies.
    </div>

    </div>
    """, unsafe_allow_html=True)

# WHY SECTION
st.markdown("---")

st.markdown("""
<div class="card">

<div class="card-title">
✨ Why SafePath AI?
</div>

<div class="card-text">

Many women experience fear and anxiety while traveling alone.

<br><br>

🛡️ AI-powered guidance  
<br>
🚨 Emergency support  
<br>
💖 Emotional reassurance  
<br>
👥 Accessibility-focused tools

<br><br>

Built with ❤️ using Python, Streamlit, Gemma 4 & Ollama

</div>

</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
Made with 💖 by Mahima
</div>
""", unsafe_allow_html=True)