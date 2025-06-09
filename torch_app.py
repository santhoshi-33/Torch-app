import streamlit as st
from generate_response import generate_response

st.title("🔥 TORCH - RAG Chatbot 🔥")

user_input = st.text_input("Ask me a question:")
if user_input:
    response = generate_response(user_input)
    st.write("🤖 TORCH:", response)
