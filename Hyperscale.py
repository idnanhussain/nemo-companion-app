import streamlit as st
import openai
import os

# Function to get response from OpenAI GPT-4
def get_llm_response(user_input):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Title of the web app
st.title("Nemo - AI Companion")

# Text input for user message
user_input = st.text_input("Say something to Nemo:")

# If user provides input, get response from LLM and update conversation history
if user_input:
    response = get_llm_response(user_input)
    st.session_state.conversation.append(("You", user_input))
    st.session_state.conversation.append(("Nemo", response))

# Display conversation history
for speaker, message in st.session_state.conversation:
    st.write(f"{speaker}: {message}")
