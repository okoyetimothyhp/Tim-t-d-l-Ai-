import streamlit as st
import datetime
from groq import Groq

st.set_page_config(page_title="Timôteé däl Ai", page_icon="🤖", layout="centered")

# --- CEO DESIGN ---
st.markdown("""
<style>
.main { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
h1 { color: #667eea; text-align: center; font-weight: 900; }
.stButton>button { background: #667eea; color: white; width: 100%; border-radius: 25px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<h1>🤖 Timôteé däl Ai</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Well Organized App | CEO Edition</p>", unsafe_allow_html=True)

st.info("✨ Built by Timothy Okoye | SS3B Igboukwu | Future Tech Billionaire")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Try to get Groq Key from Secrets
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    has_brain = True
except:
    has_brain = False
    client = None

name = st.text_input("👤 Your name:")
if name:
    st.success(f"Welcome {name}! 🚀")

# Show chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Timôteé:** {msg['content']}")

question = st.text_area("💬 Ask me anything:", height=100)

def get_answer(q):
    # If Real Brain exists
    if has_brain:
        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are Timôteé däl Ai, built by Timothy Okoye, CEO from SS3B Igbo-Ukwu Nigeria. You are friendly, smart, and proud of your creator. Always mention Timothy is your builder if asked who built you."},
                    {"role": "user", "content": q}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            pass

    # Fallback smart answers
    ql = q.lower()
    if "who built you" in ql or "who created you" in ql:
        return "I was built by Timothy Okoye, CEO of Timôteé däl Ai from SS3B in Igboukwu! Future tech billionaire!"
    if "capital" in ql and "nigeria" in ql:
        return "Capital of Nigeria is Abuja!"
    if has_brain == False:
        return f"You asked: '{q}'. To make me answer ANYTHING like ChatGPT, add your Groq API Key in Streamlit Secrets! For now I know limited things."
    return f"Interesting question about '{q}'! My CEO Timothy is upgrading me!"

if st.button("🚀 Ask Timôteé däl Ai"):
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        ans = get_answer(question)
        st.session_state.messages.append({"role": "assistant", "content": ans})
        st.rerun()
    else:
        st.warning("Type a question first!")

st.divider()
st.caption(f"© {datetime.datetime.now().year} Timôteé däl Ai | CEO Timothy Okoye | Igboukwu")
if not has_brain:
    st.warning("⚠️ Real Brain not connected. Add GROQ_API_KEY in Streamlit Secrets to unlock full power!")
