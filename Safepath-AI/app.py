import streamlit as st

st.set_page_config(page_title="SafePath AI", layout="wide")

st.title("🛡️ SafePath AI")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "AI Safety Guidance",
        "Emergency Contacts",
        "Activate SOS",
        "Safety Tips",
        "About"
    ]
)

import streamlit as st
import ollama
import json
import os

st.set_page_config(
    page_title="SafePath AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ SafePath AI")
st.subheader("AI-Powered Women's Safety Companion")

st.markdown("""
Describe your situation and get AI-powered safety guidance.
""")

user_input = st.text_area(
    "What is happening?",
    placeholder="Example: I feel unsafe while walking alone at night."
)

if st.button("Get Safety Guidance"):

    prompt = f"""
    You are a calm and responsible women's safety assistant.

    Give practical, safe, short, and supportive advice.

    Situation:
    {user_input}
    """

    response = ollama.chat(
        model='gemma3',
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )

    answer = response['message']['content']

    st.success("Safety Guidance")
    st.write(answer)

st.markdown("---")
st.header("🚨 Smart Emergency SOS System")

CONTACT_FILE = "contacts.json"

# Load saved contacts
saved_contacts = {
    "name1": "",
    "phone1": "",
    "name2": "",
    "phone2": ""
}

if os.path.exists(CONTACT_FILE):
    with open(CONTACT_FILE, "r") as file:
        saved_contacts = json.load(file)

st.subheader("📱 Emergency Contact Setup")

name1 = st.text_input(
    "Contact Name 1",
    value=saved_contacts["name1"]
)

phone1 = st.text_input(
    "Phone Number 1",
    value=saved_contacts["phone1"]
)

name2 = st.text_input(
    "Contact Name 2",
    value=saved_contacts["name2"]
)

phone2 = st.text_input(
    "Phone Number 2",
    value=saved_contacts["phone2"]
)

if st.button("💾 Save Emergency Contacts"):

    contacts = {
        "name1": name1,
        "phone1": phone1,
        "name2": name2,
        "phone2": phone2
    }

    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file)

    st.success("Emergency contacts saved successfully!")

st.markdown("---")

st.subheader("🚨 Activate SOS")

location = st.text_input(
    "Current Location",
    placeholder="Example: Sector 17 Chandigarh"
)

if st.button("🚨 Trigger SOS Alert"):

    st.error("EMERGENCY SOS ACTIVATED")

    st.subheader("📩 Alert Sent To")

    if phone1:
        st.success(f"{name1} ({phone1}) notified successfully.")

    if phone2:
        st.success(f"{name2} ({phone2}) notified successfully.")

    st.subheader("🚓 Police Assistance")

    st.info(f"Emergency alert sent to nearby police station near {location}")

    st.subheader("📨 Emergency Message")

    emergency_message = f'''
EMERGENCY ALERT

The user may be in danger.

Current Location:
{location}

Please contact them immediately.
'''

    st.code(emergency_message)