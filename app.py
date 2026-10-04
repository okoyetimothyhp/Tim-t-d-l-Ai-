import streamlit as st
import datetime
from groq import Groq
# --- DOWNLOAD SECTION - CEO FEATURE ---
st.divider()
st.markdown("<h3 style='text-align:center; color:#0a3d8f;'>📥 Download Center</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        label="📄 Download Assignment (TXT)",
        data=NETWORKING_ASSIGNMENT,
        file_name="Computer_Networking_Assignment_Timothy_SS3B.txt",
        mime="text/plain"
    )

with col2:
    st.download_button(
        label="🧠 Download My AI Info",
        data=f"Timôteé däl Ai\nBuilt by CEO Timothy Okoye\nSS3B Igboukwu\nOkoye Family - Unity, Wisdom & Progress\n\nLink: https://qsqvg2srsjpwkoa8tvbb.streamlit.app\n\n{NETWORKING_ASSIGNMENT}",
        file_name="Timotee_dal_Ai_Info.txt",
        mime="text/plain"
    )

st.markdown("<p style='text-align:center;'><b>Share my AI:</b> Just copy the link and send on WhatsApp!</p>", unsafe_allow_html=True)
st.code("https://qsqvg2srsjpwkoa8tvbb.streamlit.app", language="text")

st.set_page_config(page_title="Timôteé däl Ai", page_icon="🧠", layout="centered")

st.markdown("""
<style>
h1 { color: #0a3d8f; text-align: center; font-weight: 900; font-size: 2.8em; margin-top: -20px; }
.stButton>button { background: linear-gradient(90deg, #0a3d8f, #2d8cff); color: white!important; width: 100%; border-radius: 25px; font-weight: bold; padding: 15px; border: none; }
.chat-you { background: #dbeafe; padding: 12px; border-radius: 15px; margin: 8px 0; color: #1e1b4b!important; font-weight: 600; }
.chat-ai { background: #ffffff; padding: 15px; border-radius: 15px; border-left: 5px solid #0a3d8f; margin: 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.2); color: #000000!important; }
</style>
""", unsafe_allow_html=True)

# --- AI PROFILE LOGO ---
try:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo.png", use_container_width=True)
except:
    st.markdown("<h1 style='text-align:center;'>🧠</h1>", unsafe_allow_html=True)

st.markdown("<h1>Timôteé däl Ai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-weight:bold; color:#555;'>By CEO Timothy Okoye | SS3B Igboukwu | Okoye Family Crest 👑</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#0a3d8f; font-weight:700;'>🌐 Family Motto: Unity, Wisdom & Progress | 🛡️ Well Organized App</p>", unsafe_allow_html=True)

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
**COMPUTER NETWORKING: Meaning, Purpose, Importance and Benefits**
**By: Okoye Timothy Chukwuebuka - SS3B Igboukwu**

**1. MEANING:**
Computer Networking is the connection of two or more computers together to share information and resources.

**2. PURPOSE:**
- Resource Sharing: One printer for many computers.
- Communication: Email, WhatsApp, Video Calls.
- Collaboration: Many students work on same project via Google Docs.

**3. CORE CONCEPTS:**
Meaning, How Computers are Networked (Cables, Wi-Fi, Switch, Router), Resource Sharing, Communication, Collaboration.

**4. IMPORTANCE & BENEFITS:**
- Fast file sharing
- Reduces cost
- Remote access to school files
- Learning via YouTube
- Banking via Opay
- Supports my AI project (Without network, Timôteé cannot work)

**5. EXAMPLES:**
LAN - School Computer Lab, WAN - Internet, PAN - Bluetooth, MAN - Igboukwu town network.

**6. CONCLUSION:**
Networking changed the world. It connects Igboukwu to the whole world.
"""

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-you'>👤 <b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-ai'>🧠 <b>Timôteé:</b><br>{msg['content']}</div>", unsafe_allow_html=True)

question = st.text_input("💬 Ask me anything (try: 'Computer Networking'):")

def get_answer(q):
    ql = q.lower()
    if "network" in ql or "assignment" in ql or "ss3b" in ql:
        return NETWORKING_ASSIGNMENT
    if "who built you" in ql or "who created you" in ql or "founder" in ql:
        return "I was built by **CEO Timothy Okoye**, SS3B Igboukwu! From Okoye Family - Motto: Unity, Wisdom & Progress! 👑 My logo is the blue brain with circuit!"
    if has_brain and client:
        try:
            completion = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "system", "content": "You are Timôteé däl Ai, built by CEO Timothy Okoye SS3B Igboukwu. You are proud, royal, helpful. If user asks about networking, show the assignment."}, {"role": "user", "content": q}])
            return completion.choices[0].message.content
        except Exception as e:
            pass
    return f"You asked: '{q}'. Great question! Type **'Computer Networking'** to see my SS3B assignment for Mrs. Okoye!"

if st.button("🚀 Ask Timôteé däl Ai"):
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        ans = get_answer(question)
        st.session_state.messages.append({"role": "assistant", "content": ans})
        st.rerun()

st.divider()
st.caption(f"© {datetime.datetime.now().year} Okoye Family | CEO Timothy Okoye | Igboukwu 👑 | Timôteé däl Ai v2.0")