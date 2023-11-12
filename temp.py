import streamlit as st
from transformers import pipeline

chatbot = pipeline("text-generation", model='EleutherAI/gpt-neo-2.7B')

def generate_response(prompt):
    response = chatbot(prompt, max_length=50)
    return response[0]["generated_text"].strip()

prompt = st.chat_input("say")
if prompt:
    st.write(generate_response(prompt))
