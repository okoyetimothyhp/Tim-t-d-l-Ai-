import streamlit as st
import datetime
from groq import Groq

st.set_page_config(page_title="Timôteé däl Ai", page_icon="🤖", layout="centered")

# --- BEAUTIFUL CEO DESIGN ---
st.markdown("""
<style>
.main { background-color: #f8f9ff; }
h1 { color: #4338ca; text-align: center; font-weight: 900; font-size: 3em; }
.stButton>button { background: linear-gradient(90deg, #667eea, #764ba2); color: white; width: 100%; border-radius: 25px; font-weight: bold; padding: 15px; }
.chat-you { background: #e0e7ff; padding: 10px; border-radius: 15px; margin: 5px; }
.chat-ai { background: white; padding: 15px; border-radius: 15px; border-left: 5px solid #667eea; margin: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# LOGO HEADER
st.markdown("<h1>🤖 Timôteé däl Ai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-weight:bold; color:#555;'>By CEO Timothy Okoye | SS3B Igboukwu | Okoye Family Crest 👑</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>🌐 Family Motto: Unity, Wisdom & Progress | 🛡️ Well Organized App</p>", unsafe_allow_html=True)

# ASSIGNMENT BANNER FOR TEACHER
st.success("📚 TEACHER: Type 'Computer Networking' to see my SS3B Assignment embedded in this AI!")

if "messages" not in st.session_state:
    st.session_state.messages = []

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    has_brain = True
except:
    has_brain = False
    client = None

# THE SECRET ASSIGNMENT KNOWLEDGE BASE
NETWORKING_ASSIGNMENT = """
**TOPIC: Computer Networking: Meaning, Purpose, Importance and Benefits**
**By: Okoye Timothy - SS3B Igboukwu**

**What is Computer Networking?**
Computer Networking is the connection of two or more computers together to share information and resources. For example, when we connect the computers in our school computer lab together with cables or Wi-Fi, it becomes a network. My AI project Timôteé däl Ai is hosted on the internet network.

**Purpose:**
1. Resource Sharing: One printer shared saves money. Share files, data, internet.
2. Communication: Email, WhatsApp, Facebook, video calls.
3. Collaboration: Many students work on same project via Google Docs.

**Core Concepts:**
a) Meaning of Networking
b) How Computers are Networked: Cables, Wi-Fi, Switch, Router
c) Resource Sharing
d) Communication
e) Collaboration

**Importance and Benefits:**
a) Fast information sharing
b) Reduces cost
c) Remote access from home
d) Learning via YouTube
e) Business/Banking via Opay
f) Supports my AI project

**Examples:** LAN - School Lab, WAN - Internet, PAN - Bluetooth, MAN - Igboukwu town.

**Conclusion:** Networking changed world. Without it my AI cannot work. Every school should have good network.
"""

# CHAT DISPLAY
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-you'>👤 <b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-ai'>🤖 <b>Timôteé:</b><br>{msg['content']}</div>", unsafe_allow_html=True)

question = st.text_input("💬 Ask me anything (try: 'Computer Networking assignment'):")

def get_answer(q):
    ql = q.lower()

    # IF TEACHER ASKS FOR ASSIGNMENT - SHOW IT DIRECTLY!
    if "network" in ql or "assignment" in ql or "ss3b" in ql:
        return NETWORKING_ASSIGNMENT

    if "who built you" in ql or "who created you" in ql or "owner" in ql:
        return "I was built by **CEO Timothy Okoye**, SS3B Igboukwu! From Okoye Family - Motto: Unity, Wisdom & Progress! 👑 He built me as Well Organized App!"

    if has_brain and client:
        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are Timôteé däl Ai, built by Timothy Okoye SS3B Igboukwu. You are proud of Okoye Family. You have embedded assignment about Computer Networking. If asked about networking, provide detailed assignment. Always mention Timothy is builder."},
                    {"role": "user", "content": q}
                ]
            )
            return completion.choices[0].message.content
        except:
            pass

    if not has_brain:
        return f"You asked: '{q}'.\n\n{NETWORKING_ASSIGNMENT}\n\n(Add GROQ_API_KEY in Secrets to make me answer ANY question like ChatGPT!)"

    return f"Great question about '{q}'! My builder Timothy Okoye taught me about Computer Networking. Ask me about 'Computer Networking' to see my SS3B assignment!"

if st.button("🚀 Ask Timôteé däl Ai"):
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        ans = get_answer(question)
        st.session_state.messages.append({"role": "assistant", "content": ans})
        st.rerun()
    else:
        st.warning("Type a question first!")

st.divider()
col1, col2 = st.columns(2)
with col1:
    st.caption(f"© {datetime.datetime.now().year} Okoye Family")
with col2:
    st.caption(f"CEO Timothy | Igboukwu 👑")

if not has_brain:
    st.error("⚠️ Add GROQ_API_KEY in Streamlit Secrets → Settings → Secrets to unlock ChatGPT brain!")