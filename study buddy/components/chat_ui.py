import streamlit as st

def display_chat_message(role: str, content: str):
    """
    Renders a chat bubble on the screen depending on who is speaking.
    'user' gets a user bubble, 'assistant' gets an AI bubble.
    """
    if role == "user":
        with st.chat_message("user"):
            st.markdown(content)
    elif role == "assistant":
        with st.chat_message("assistant"):
            st.markdown(content)

def initialize_chat_history():
    """Ensures the chat history list exists in the app memory space."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def append_to_chat_history(role: str, content: str):
    """Saves a message to the session memory list."""
    st.session_state.messages.append({"role": role, "content": content})

def render_entire_chat_history():
    """Loops through all saved messages and prints them to the screen."""
    for message in st.session_state.messages:
        display_chat_message(message["role"], message["content"])