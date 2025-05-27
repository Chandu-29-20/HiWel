import streamlit as st

# MUST come first
st.set_page_config(page_title="E-Commerce Chatbot", page_icon="🛍️")

from dotenv import load_dotenv
import os
from ecommbot.retrieval_generation import generation
from ecommbot.ingest import ingestdata

# Load environment variables
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Initialize vector store and chain
@st.cache_resource
def get_chain():
    vstore = ingestdata("C:\\Users\\Chandana\\Desktop\\E-Commerce-Chatbot1\\data\\mightymerge.io__th52bne0.csv")
    return generation(vstore)

chain = get_chain()

# UI
st.title("🛒 E-Commerce Chatbot")
st.markdown("Ask me about product(I will suggest you based on reviews provided by customers)")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input form with automatic clear
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_input")
    submit = st.form_submit_button("Send")

if submit and user_input:
    response = chain.invoke(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display conversation
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")

