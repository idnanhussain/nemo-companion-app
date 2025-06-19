from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

print("API Key Loaded:", openai.api_key)  # Add this for debugging


# Function to get response from OpenAI Chat API
def get_llm_response(user_input):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a compassionate AI companion named Nemo."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()

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
