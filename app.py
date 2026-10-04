import streamlit as st
import datetime
from groq import Groq

st.set_page_config(page_title="Timôteé däl Ai", page_icon="🧠", layout="centered")

st.markdown("<style>h1{color:#0a3d8f;text-align:center;font-weight:900;} .stButton>button{background:#0a3d8f;color:white!important;width:100%;border-radius:25px;font-weight:bold;padding:12px;}</style>", unsafe_allow_html=True)

# LOGO
try:
    c1,c2,c3 = st.columns([1,2,1])
    with c2: st.image("logo.png", use_container_width=True)
except: st.markdown("<h1 style='text-align:center'>🧠</h1>", unsafe_allow_html=True)

st.markdown("<h1>Timôteé däl Ai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'><b>By CEO Timothy Okoye | SS3B Igboukwu | Okoye Family 👑</b></p>", unsafe_allow_html=True)
st.success("📚 Type 'Computer Networking' to see assignment!")

if "messages" not in st.session_state: st.session_state.messages = []

ASSIGNMENT = """COMPUTER NETWORKING ASSIGNMENT - SS3B
By Okoye Timothy Chukwuebuka

1. MEANING: Connection of 2+ computers to share resources.
2. PURPOSE: Resource Sharing, Communication, Collaboration.
3. HOW: Cables, Wi-Fi, Switch, Router.
4. BENEFITS: Fast sharing, cheap, remote learning, Opay, YouTube, supports AI.
5. TYPES: LAN (School Lab), WAN (Internet), PAN (Bluetooth), MAN (Igboukwu Town).
6. CONCLUSION: Networking connects Igboukw