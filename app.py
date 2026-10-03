import streamlit as st
import datetime

st.set_page_config(page_title="Timôteé däl Ai", page_icon="🤖", layout="centered")

st.title("🤖 Timôteé däl Ai")
st.subheader("Well Organized App - Level 2")
st.write("Welcome! I am the first AI built by Timothy Okoye from SS3B in Igboukwu!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

name = st.text_input("What is your name?")
if name:
    st.success(f"Hello {name}! Timôteé däl Ai is happy to meet you! 🚀")

st.divider()

# Show old messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.info(f"You: {msg['content']}")
    else:
        st.write(f"**Timôteé däl Ai Answer:** {msg['content']}")

question = st.text_area("Ask me anything:", key="q")

def get_smart_answer(q):
    q_lower = q.lower()
    
    if "who built you" in q_lower or "who created you" in q_lower or "who is your owner" in q_lower:
        return "I was built by Timothy Okoye, CEO of Timôteé däl Ai from SS3B in Igboukwu! He is a future tech billionaire."
    
    elif "full meaning" in q_lower and "ai" in q_lower:
        return "AI means Artificial Intelligence. It is technology that makes computers think and learn like humans."
    
    elif "what is ai" in q_lower:
        return "Artificial Intelligence (AI) is the simulation of human intelligence in machines. It allows computers to learn, reason, and make decisions."
    
    elif "nigeria" in q_lower and "capital" in q_lower:
        return "The capital of Nigeria is Abuja. Lagos is the largest city and former capital."
    
    elif "igboukwu" in q_lower or "igbo ukwu" in q_lower:
        return "Igbo-Ukwu is a historic town in Anambra State, Nigeria, famous for ancient bronze artifacts discovered in 1939. It is home to great people like CEO Timothy!"
    
    elif "who is timothy" in q_lower:
        return "Timothy Okoye is the CEO and Founder of Timôteé däl Ai, a young tech genius from SS3B in Igbo-Ukwu building the future of Africa!"
    
    elif "math" in q_lower or "2+2" in q_lower or "calculate" in q_lower:
        try:
            # Simple calculation attempt
            if "+" in q or "-" in q or "*" in q or "/" in q:
                return f"For maths: {q} - I can help! In Python, we use + - * / . Example: 2+2=4. Tell me the exact numbers!"
            return "I love Maths! Tell me what to calculate, e.g., What is 25 * 4 ?"
        except:
            return "Maths is the language of the universe!"
    
    elif "science" in q_lower:
        return "Science is the study of the world around us through observation and experiments. It includes Physics, Chemistry, and Biology."
    
    elif "time" in q_lower:
        return f"Current time is {datetime.datetime.now().strftime('%I:%M %p on %A, %B %d, %Y')}"
    
    elif "hello" in q_lower or "hi" in q_lower:
        return "Hello! 👋 I am Timôteé däl Ai. How can I help you today?"
    
    else:
        return f"You asked: '{q}'. That's a great question! I am still learning. My CEO Timothy is teaching me more every day. Soon I will answer everything like ChatGPT! For now, try asking: Who built you? What is AI? What is the capital of Nigeria?"

if st.button("Ask Timôteé däl Ai"):
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        answer = get_smart_answer(question)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()
    else:
        st.warning("Please type a question first!")

st.caption("Built by Timothy - CEO of Timôteé däl Ai | Level 2 - Future Tech Billionaire")