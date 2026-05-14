import streamlit as st
import json
import os

# PAGE CONFIG
st.set_page_config(
    page_title="Emergency Contacts",
    page_icon="📞",
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
    sidebar = "#ffd6e7"
    sidebar_text = "#444444"

# DARK MODE
else:

    bg = "#000000"
    card_bg = "#1a1a1a"
    text = "#ffffff"
    title = "#ffffff"
    button = "#555555"
    button_hover = "#777777"
    shadow = "rgba(255,255,255,0.1)"
    sidebar = "#2b2b2b"
    sidebar_text = "#ffffff"

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

[data-testid="stSidebarContent"] {{
    background-color: {sidebar} !important;
}}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {{
    color: {sidebar_text} !important;
}}

/* TITLE */
.title {{
    font-size: 55px;
    font-weight: bold;
    color: {title};
    text-align: center;
    margin-top: 20px;
    margin-bottom: 10px;
}}

/* SUBTITLE */
.subtitle {{
    text-align: center;
    color: {text};
    font-size: 20px;
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

/* TEXT INPUT */
.stTextInput input {{
    background-color: {card_bg} !important;
    color: {text} !important;
    border: 2px solid #000000 !important;
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 17px !important;
}}

/* INPUT LABELS */
.stTextInput label {{
    color: {text} !important;
    font-size: 17px !important;
    font-weight: bold !important;
}}

/* BUTTON */
.stButton > button {{
    background-color: {button};
    color: white;
    border-radius: 15px;
    border: none;
    padding: 12px 25px;
    font-size: 17px;
    font-weight: bold;
    transition: 0.3s;
}}

.stButton > button:hover {{
    background-color: {button_hover};
    transform: scale(1.03);
}}

/* CONTACT BOX */
.contact-box {{
    background-color: {card_bg};
    padding: 20px;
    border-radius: 18px;
    margin-top: 15px;
    box-shadow: 0px 3px 15px {shadow};
}}

/* CONTACT NAME */
.contact-name {{
    color: {title};
    font-size: 22px;
    font-weight: bold;
}}

/* CONTACT PHONE */
.contact-phone {{
    color: {text};
    font-size: 18px;
    margin-top: 5px;
}}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class="title">
📞 Emergency Contacts
</div>

<div class="subtitle">
Save trusted contacts for emergency situations
</div>
""", unsafe_allow_html=True)

# FILE NAME
FILE_NAME = "contacts.json"

# LOAD CONTACTS SAFELY
try:

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            contacts = json.load(file)

    else:
        contacts = []

except:
    contacts = []

# ADD CONTACT CARD
st.markdown('<div class="card">', unsafe_allow_html=True)

name = st.text_input("Contact Name")
phone = st.text_input("Phone Number")

if st.button("➕ Save Contact"):

    if name and phone:

        contacts.append({
            "name": name,
            "phone": phone
        })

        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file)

        st.success("Contact Saved Successfully ✅")

        st.rerun()

    else:
        st.error("Please fill all fields")

st.markdown('</div>', unsafe_allow_html=True)

# SAVED CONTACTS TITLE
st.markdown("""
<div class="title" style="font-size:40px;">
Saved Contacts
</div>
""", unsafe_allow_html=True)

# DISPLAY CONTACTS
if len(contacts) == 0:

    st.info("No contacts saved yet.")

else:

    for contact in contacts:

        # SAFETY CHECK
        if isinstance(contact, dict):

            name = contact.get("name", "Unknown")
            phone = contact.get("phone", "No Number")

        else:

            name = str(contact)
            phone = "No Number"

        st.markdown(f"""
        <div class="contact-box">

        <div class="contact-name">
        👤 {name}
        </div>

        <div class="contact-phone">
        📱 {phone}
        </div>

        </div>
        """, unsafe_allow_html=True)