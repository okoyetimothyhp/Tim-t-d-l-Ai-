import streamlit as st
import datetime
from groq import Groq

st.set_page_config(page_title="Timôteé däl Ai", page_icon="🧠", layout="centered")

st.markdown("""
<style>
h1 { color: #0a3d8f; text-align: center; font-weight: 900; font-size: 2.8em; margin-top: -10px; }
.stButton>button { background: linear-gradient(90deg, #0a3d8f, #2d8cff); color: white!important; width: 100%; border-radius: 25px; font-weight: bold; padding: 12px; border: none; }
.chat-you { background: #dbeafe; padding: 12px; border-radius: 15px; margin: 8px 0; color: #1e1b4b!important; font-weight: 600; }
.chat-ai { background: #ffffff; padding: 15px; border-radius: 15px; border-left: 5px solid #0a3d8f; margin: 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.2); color: #000000!important; }
</style>
""", unsafe_allow_html=True)

try:
    c1,c2,c3 = st.columns([1,2,1])
    with c2:
        st.image("logo.png", use_container_width=True)
except:
    st.markdown("<h1 style='text-align:center;'>🧠</h1>", unsafe_allow_html=True)

st.markdown("<h1>Timôteé däl Ai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-weight:bold;'>By CEO Timothy Okoye | SS3B Igboukwu | Okoye Family Crest 👑</p>", unsafe_allow_html=True)
st.success("📚 TEACHER: Type 'Computer Networking' to see my SS3B Assignment!")

if "messages" not in st.session_state:
    st.session_state.messages = []

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    has_brain = True
except:
    has_brain = False
    client = None

NETWORKING_ASSIGNMENT = """COMPUTER NETWORKING: Meaning, Purpose, Importance and Benefits
By: Okoye Timothy Chukwuebuka - SS3B Igboukwu

MEANING: Connection of 2+ computers to share info.

PURPOSE: Resource Sharing, Communication, Collaboration.

IMPORTANCE: Fast sharing, reduces cost, remote access, YouTube learning, Opay banking, supports AI.

EXAMPLES: LAN - School Lab, WAN - Internet, PAN - Bluetooth, MAN - Igboukwu.

CONCLUSION: Networking changed world.
"""

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-you'>👤 <b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-ai'>🧠 <b>Timôteé:</b><br>{msg['content']}</div>", unsafe_allow_html=True)

question = st.text_input("💬 Ask me anything:")

def get_answer(q):
    ql = q.lower()
    if "network" in ql or "assignment" in ql:
        return NETWORKING_ASSIGNMENT
    if has_brain and client:
        try:
            comp = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"system","content":"You are Timôteé däl Ai by Timothy Okoye"},{"role":"user","content":q}])
            return comp.choices[0].message.content
        except:
            pass
    return "Type 'Computer Networking' to see my assignment!"

if st.button("🚀 Ask Timôteé däl Ai"):
    if question:
        st.session_state.messages.append({"role":"user","content":question})
        st.session_state.messages.append({"role":"assistant","content":get_answer(question)})
        st.rerun()

# DOWNLOAD SECTION
st.divider()
st.markdown("### 📥 Download Center")
colA, colB = st.columns(2)
with colA:
    st.download_button("📄 Download Assignment", data=NETWORKING_ASSIGNMENT, file_name="Networking_Assignment_Timothy_SS3B.txt", mime="text/plain")
with colB:
    st.download_button("🧠 Download AI Info", data=f"Timôteé däl Ai by CEO Timothy\n{NETWORKING_ASSIGNMENT}", file_name="Timotee_Info.txt", mime="text/plain")

st.code("Share Link: https://qsqvg2srsjpwkoa8tvbb.streamlit.app")
st.caption(f"© {datetime.datetime.now().year} Okoye Family | CEO Timothy")