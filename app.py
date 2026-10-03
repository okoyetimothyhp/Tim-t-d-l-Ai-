import streamlit as st

st.set_page_config(page_title="Timôtëë dãl Ai", page_icon="🤖", layout="centered")

st.title("🤖 Timôtëë dãl Ai")
st.markdown("### Well Organized App")
st.write("Welcome! I am the first AI built by Timothy from SS3B in Igboukwu!")

name = st.text_input("What is your name?")
if name:
    st.success(f"Hello {name}! Timôtëë dãl Ai is happy to meet you! 🚀")

question = st.text_area("Ask me anything:")

if st.button("Ask Timôtëë dãl Ai"):
    if question:
        st.info(f"You asked: {question}")
        st.write("**Timôtëë dãl Ai Answer:** You are a future tech billionaire! Keep building - this is just the beginning.")
    else:
        st.warning("Please type a question first.")

st.divider()
st.caption("Built by Timothy - CEO of Timôtëë dãl Ai | Igboukwu")