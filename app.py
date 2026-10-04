import streamlit as st
import datetime
from groq import Groq

st.set_page_config(page_title="Timôteé däl Ai", page_icon="🤖", layout="centered")

st.markdown("""
<style>
h1 { color: #4338ca; text-align: center; font-weight: 900; font-size: 3em; }
.stButton>button { background: linear-gradient(90deg, #667eea, #764ba2); color: white!important; width: 100%; border-radius: 25px; font-weight: bold; padding: 15px; }
.chat-you { background: #c7d2fe; padding: 12px; border-radius: 15px; margin: 8px 0; color: #1e1b4b!important; font-weight: 600; }
.chat-ai { background: #ffffff; padding: 15px; border-radius: 15px; border-left: 5px solid #667eea; margin: 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.2); color: #000000!important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🤖 Timôteé däl Ai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-weight:bold; color:#555;'>By CEO Timothy Okoye | SS3B Igboukwu | Okoye Family Crest 👑</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>🌐 Family Motto: Unity, Wisdom & Progress | 🛡️ Well Organized App</p>", unsafe_allow_html=True)

st.success("📚 TEACHER: Type 'Computer Networking' to see my SS3B Assignment!")

if "messages" not in st.session_state:
    st.session_state.messages = []

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    has_brain = True
except:
    has_brain = False
    client = None

NETWORKING_ASSIGNMENT = """
**TOPIC: Computer Networking: Meaning, Purpose, Importance and Benefits**
**By: Okoye Timothy - SS3B Igboukwu**

**What is Computer Networking?**
Computer Networking is the connection of two or more computers together to share information and resources.

**Purpose:**
1. Resource Sharing: One printer shared saves money.
2. Communication: Email, WhatsApp, video calls.
3. Collaboration: Many students work on same project via Google Docs.

**Core Concepts:**
Meaning, How Computers are Networked (Cables, Wi-Fi, Switch, Router), Resource Sharing, Communication, Collaboration.

**Importance and Benefits:**
Fast sharing, reduces cost, remote access, learning via YouTube, Banking via Opay, supports my AI project.

**Examples:** LAN - School Lab, WAN - Internet, PAN - Bluetooth, MAN - Igboukwu town.

**Conclusion:** Networking changed world. Without it my AI cannot work.
"""

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-you'>👤 <b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-ai'>🤖 <b>Timôteé:</b><br>{msg['content']}</div>", unsafe_allow_html=True)

question = st.text_input("💬 Ask me anything (try: 'Computer Networking'):")

def get_answer(q):
    ql = q.lower()
    if "network" in ql or "assignment" in ql or "ss3b" in ql:
        return NETWORKING_ASSIGNMENT
    if "who built you" in ql or "who created you" in ql:
        return "I was built by **CEO Timothy Okoye**, SS3B Igboukwu! From Okoye Family - Motto: Unity, Wisdom & Progress! 👑"
    if has_brain and client:
        try:
            completion = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "system", "content": "You are Timôteé däl Ai, built by Timothy Okoye SS3B. If asked about networking, provide assignment."}, {"role": "user", "content": q}])
            return completion.choices[0].message.content
        except:
            pass
    return f"Great question! Ask me about 'Computer Networking' to see my SS3B assignment!"

if st.button("🚀 Ask Timôteé däl Ai"):
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        ans = get_answer(question)
        st.session_state.messages.append({"role": "assistant", "content": ans})
        st.rerun()

st.divider()
st.caption(f"© {datetime.datetime.now().year} Okoye Family | CEO Timothy | Igboukwu 👑")