import streamlit as st
import ollama

# PAGE CONFIG
st.set_page_config(
    page_title="AI Safety Guidance",
    page_icon="🤖",
    layout="wide"
)

# LOAD DARK MODE STATE
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

dark_mode = st.session_state.dark_mode

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
    sidebar_text = "#535353"

# DARK MODE COLORS
else:

    bg = "#000000"
    sidebar = "#1a1a1a"
    title = "#ffffff"
    card_bg = "#111111"
    text = "#ffffff"
    button = "#444444"
    button_hover = "#666666"
    shadow = "rgba(255,255,255,0.1)"
    sidebar_text = "#ffffff"

# CUSTOM CSS
st.markdown(f"""
<style>

/* APP */
.stApp {{
    background: {bg};
}}

/* REMOVE STREAMLIT DEFAULTS */
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
    background: {sidebar} !important;
}}

section[data-testid="stSidebar"] * {{
    color: {sidebar_text} !important;
}}

/* PAGE TITLE */
.page-title {{
    font-size: 55px;
    font-weight: bold;
    color: {title};
    text-align: center;
    margin-top: 20px;
    margin-bottom: 30px;
}}

/* CARD */
.card {{
    background-color: {card_bg};
    padding: 35px;
    border-radius: 25px;
    box-shadow: 0px 5px 25px {shadow};
    margin-top: 20px;
    margin-bottom: 20px;
}}

/* CARD TEXT */
.card-text {{
    color: {text};
    font-size: 18px;
    line-height: 1.8;
}}

/* TEXT AREA */
.stTextArea textarea {{
    background-color: {card_bg} !important;
    color: {text} !important;
    border: 2px solid #000000 !important;
    border-radius: 15px !important;
    font-size: 18px !important;
}}

/* TEXT AREA LABEL */
.stTextArea label {{
    color: {text} !important;
    font-size: 18px !important;
    font-weight: bold !important;
}}

/* PLACEHOLDER TEXT */
.stTextArea textarea::placeholder {{
    color: #666666 !important;
}}

/* BUTTON */
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

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class="page-title">
🤖 AI Safety Guidance
</div>
""", unsafe_allow_html=True)

# INFO CARD
st.markdown("""
<div class="card">
<div class="card-text">

Describe your situation and SafePath AI will provide practical safety-focused guidance.

Examples:

• Someone is following me  
• I feel unsafe in a cab  
• I am walking alone at night  
• A stranger is behaving suspiciously

</div>
</div>
""", unsafe_allow_html=True)

# USER INPUT
user_input = st.text_area(
    "Describe your situation",
    height=180,
    placeholder="Type here..."
)

# BUTTON
if st.button("Get Guidance"):

    if user_input.strip() != "":

        with st.spinner("Getting safety guidance..."):

            response = ollama.chat(

                model='gemma3:1b',

                messages=[

                    {
                        'role': 'system',
                        'content': '''
You are a women's safety assistant.

Give calm, short, practical safety guidance.

Rules:
- Maximum 4 bullet points
- Keep answers short
- Do not create panic
- Give practical advice
- Encourage contacting trusted people or authorities if needed
'''
                    },

                    {
                        'role': 'user',
                        'content': user_input
                    }

                ],

                options={
                    "num_predict": 120,
                    "temperature": 0.3
                }

            )

            answer = response['message']['content']

        st.markdown(f"""
        <div class="card">
        <div class="card-text">
        {answer}
        </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Please describe your situation.")