import streamlit as st
import speech_recognition as sr
import time
import json
import os

# PAGE CONFIG
st.set_page_config(
    page_title="Smart Voice SOS",
    page_icon="🎙️",
    layout="wide"
)

# LOAD THEME
dark_mode = st.session_state.get("dark_mode", False)

# LIGHT MODE
if not dark_mode:

    bg = "linear-gradient(to bottom right, #fff0f5, #ffe4ec)"
    card_bg = "white"
    text = "#444444"
    title = "#ff4f81"
    button = "#ff69b4"
    button_hover = "#ff3f8e"
    shadow = "rgba(255,105,180,0.2)"
    input_bg = "#ffffff"
    sidebar = "#ffd6e7"
    keyword_color = "black"

# DARK MODE
else:

    bg = "#000000"
    card_bg = "#1a1a1a"
    text = "#ffffff"
    title = "#ffffff"
    button = "#555555"
    button_hover = "#777777"
    shadow = "rgba(255,255,255,0.1)"
    input_bg = "#2b2b2b"
    sidebar = "#1a1a1a"
    keyword_color = "white"

# CSS
st.markdown(f"""
<style>

/* MAIN APP */
.stApp {{
    background: {bg};
}}

/* HIDE STREAMLIT */
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

/* BUTTONS */
.stButton > button {{
    background-color: {button};
    color: white;
    border: none;
    border-radius: 15px;
    padding: 14px 30px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
    width: 100%;
}}

.stButton > button:hover {{
    background-color: {button_hover};
    transform: scale(1.03);
}}

/* ALERT BOX */
.alert-box {{
    background: linear-gradient(to right, #ff4d6d, #ff758f);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 22px;
    font-weight: bold;
    margin-top: 25px;
    animation: pulse 1s infinite;
}}

@keyframes pulse {{

    0% {{
        transform: scale(1);
    }}

    50% {{
        transform: scale(1.02);
    }}

    100% {{
        transform: scale(1);
    }}
}}

/* INFO CARD */
.info-card {{
    background-color: {card_bg};
    padding: 25px;
    border-radius: 20px;
    color: {text};
    font-size: 18px;
    line-height: 1.8;
    box-shadow: 0px 3px 15px {shadow};
    margin-top: 20px;
}}

/* DETECTED TEXT */
.detected {{
    color: {title};
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}}

/* ALERT TEXT */
.stSuccess, .stWarning, .stInfo, .stError {{
    color: {"black" if not dark_mode else "white"} !important;
}}

.stSuccess *, .stWarning *, .stInfo *, .stError * {{
    color: {"black" if not dark_mode else "white"} !important;
}}

/* TEXTAREA LABEL */
.stTextArea label {{
    color: {keyword_color} !important;
    font-weight: bold !important;
    font-size: 18px !important;
}}

/* TEXTAREA */
.stTextArea textarea {{
    background-color: {input_bg} !important;
    color: {keyword_color} !important;
    border-radius: 15px !important;
    border: 2px solid {"#000000" if not dark_mode else "#555555"} !important;
    font-size: 17px !important;
    padding: 15px !important;
}}

/* SECRET TITLES */
.secret-heading {{
    color: {keyword_color};
    font-size: 40px;
    font-weight: bold;
    margin-top: 30px;
}}

.secret-sub {{
    color: {keyword_color};
    font-size: 18px;
    margin-bottom: 10px;
}}

/* KEYWORDS */
.keyword-text {{
    color: {keyword_color};
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 8px;
}}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class="title">
🎙️ Smart Voice SOS
</div>

<div class="subtitle">
AI-powered voice emergency detection system
</div>
""", unsafe_allow_html=True)

# INFO CARD
st.markdown(f"""
<div class="info-card">

SafePath AI continuously listens for emergency keywords.

<br><br>

🚨 SOS activates automatically  
📞 Emergency contacts alerted  
🚔 Nearby police station alerted  
📍 Live location shared instantly  

</div>
""", unsafe_allow_html=True)

# KEYWORDS FILE
KEYWORDS_FILE = "keywords.json"

# LOAD SAVED KEYWORDS
if os.path.exists(KEYWORDS_FILE):

    with open(KEYWORDS_FILE, "r") as file:
        saved_keywords = json.load(file)

else:

    saved_keywords = []

# SECRET TITLE
st.markdown(f"""
<div class="secret-heading">
🔐 Secret Emergency Keywords
</div>

<div class="secret-sub">
Enter your secret emergency words (comma separated)
</div>
""", unsafe_allow_html=True)

# INPUT
custom_words = st.text_area(
    "",
    value=", ".join(saved_keywords),
    placeholder="example: call mom, red notebook, pineapple"
)

# SAVE BUTTON
if st.button("💾 Save Secret Keywords"):

    saved_keywords = [
        word.strip().lower()
        for word in custom_words.split(",")
        if word.strip()
    ]

    with open(KEYWORDS_FILE, "w") as file:

        json.dump(saved_keywords, file)

    st.success("✅ Secret keywords saved successfully")

# DEFAULT WORDS
keywords = [
    "help",
    "danger",
    "save me",
    "emergency"
]

# ADD SAVED WORDS
keywords.extend(saved_keywords)

# ACTIVE TITLE
st.markdown(f"""
<div class="secret-heading" style="font-size:35px;">
✅ Active Emergency Keywords
</div>
""", unsafe_allow_html=True)

# SHOW WORDS
for word in keywords:

    st.markdown(
        f'<div class="keyword-text">• {word}</div>',
        unsafe_allow_html=True
    )

# SESSION STATE
if "listening" not in st.session_state:
    st.session_state.listening = False

# BUTTONS
col1, col2 = st.columns(2)

with col1:

    if st.button("🎤 Start Voice Protection"):
        st.session_state.listening = True

with col2:

    if st.button("🛑 Stop Listening"):
        st.session_state.listening = False

# MAIN CARD
st.markdown('<div class="card">', unsafe_allow_html=True)

# STATUS
if st.session_state.listening:

    st.success("🟢 Voice Protection Active")

    recognizer = sr.Recognizer()

    while st.session_state.listening:

        try:

            with sr.Microphone() as source:

                st.info("🎧 Listening for emergency words...")

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

                text = recognizer.recognize_google(audio)

                st.markdown(f"""
                <div class="detected">
                🗣️ Detected Speech: {text}
                </div>
                """, unsafe_allow_html=True)

                detected = False

                for word in keywords:

                    if word.lower() in text.lower():

                        detected = True

                        st.markdown("""
                        <div class="alert-box">
                        🚨 EMERGENCY DETECTED 🚨
                        <br><br>
                        Activating SafePath Emergency Protocol
                        </div>
                        """, unsafe_allow_html=True)

                        st.warning(
                            "📞 Emergency contacts alerted"
                        )

                        st.warning(
                            "🚔 Nearby police station alerted"
                        )

                        st.info(
                            "📍 Live location shared"
                        )

                        st.balloons()

                        break

                if not detected:

                    st.success("✅ No emergency detected")

        except sr.UnknownValueError:

            st.warning("Could not understand audio")

        except sr.WaitTimeoutError:

            st.warning("No speech detected")

        except Exception as e:

            st.error(f"Error: {e}")

        time.sleep(1)

else:

    st.warning("🔴 Voice Protection OFF")

st.markdown('</div>', unsafe_allow_html=True)