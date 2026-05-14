import streamlit as st
import json
import os
import time
from streamlit_geolocation import streamlit_geolocation

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

/* SUBTITLE */
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

/* INPUT */
.stTextInput input {{
    background-color: {input_bg} !important;
    color: {text} !important;
    border-radius: 12px !important;
    border: 2px solid #000000 !important;
    padding: 12px !important;
    font-size: 17px !important;
}}

/* LABEL */
.stTextInput label {{
    color: {text} !important;
    font-weight: bold !important;
    font-size: 17px !important;
}}

/* BUTTON */
.stButton > button {{
    background-color: {button};
    color: white;
    border: none;
    border-radius: 15px;
    padding: 14px 30px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
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

/* INFO BOX */
.info-box {{
    background-color: {card_bg};
    padding: 25px;
    border-radius: 18px;
    margin-top: 20px;
    box-shadow: 0px 3px 15px {shadow};
    color: {text};
    font-size: 18px;
    line-height: 1.8;
}}

/* ALERT TEXT */
[data-testid="stAlert"] {{
    color: {"black" if not dark_mode else "white"} !important;
}}

[data-testid="stAlert"] * {{
    color: {"black" if not dark_mode else "white"} !important;
}}

div[data-baseweb="notification"] {{
    color: {"black" if not dark_mode else "white"} !important;
}}

div[data-baseweb="notification"] * {{
    color: {"black" if not dark_mode else "white"} !important;
}}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class="title">
🚨 Activate SOS
</div>

<div class="subtitle">
Quick emergency assistance for unsafe situations
</div>
""", unsafe_allow_html=True)

# CARD START
st.markdown('<div class="card">', unsafe_allow_html=True)

# LIVE LOCATION
location_data = streamlit_geolocation()

if location_data and location_data["latitude"]:

    latitude = location_data["latitude"]
    longitude = location_data["longitude"]

    location = f"Latitude: {latitude}, Longitude: {longitude}"

    st.success("📍 Live location detected successfully")

else:

    location = "Location not detected"

    st.warning("Please allow location access in your browser")

# EMERGENCY INPUT
danger = st.text_input("⚠️ Describe Emergency")

# SOS BUTTON
if st.button("🚨 ACTIVATE SOS"):

    st.markdown("""
    <div class="alert-box">
    🚨 SOS ACTIVATED 🚨
    <br><br>
    Emergency contacts have been alerted.
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1)

    # LOAD CONTACTS
    FILE_NAME = "contacts.json"

    try:

        if os.path.exists(FILE_NAME):

            with open(FILE_NAME, "r") as file:
                contacts = json.load(file)

            st.markdown("## 📞 Alerted Contacts")

            for contact in contacts:

                if isinstance(contact, dict):

                    st.success(
                        f"{contact.get('name')} alerted successfully"
                    )

        else:
            st.warning("No emergency contacts saved.")

    except:
        st.error("Unable to load emergency contacts.")

    # POLICE ALERT
    st.warning("🚔 Nearby police station alert simulated")

    # SYSTEM ACTIVATED
    st.info("📡 Emergency response system activated")

    # DETAILS
    st.markdown(f"""
    <div class="info-box">

    <b>📍 Live Location:</b><br>
    {location}

    <b>⚠️ Emergency Situation:</b><br>
    {danger}

    </div>
    """, unsafe_allow_html=True)

# CARD END
st.markdown('</div>', unsafe_allow_html=True)