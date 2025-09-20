"""
Personal Finance Chatbot

This Streamlit application provides intelligent guidance on personal finance topics
such as savings, taxes, and investments. It uses keyword-based responses for specific
topics and an AI model for general queries. Includes a savings calculator for
compound interest calculations.

Features:
- Keyword detection for savings, taxes, investments
- AI-powered conversational responses
- Savings calculator with compound interest
- Chat history maintenance
- User-friendly interface

Dependencies:
- streamlit
- transformers
- torch
"""

import streamlit as st
from transformers import pipeline
import logging
import torch

logging.basicConfig(level=logging.INFO)

# Initialize the chatbot model pipeline (using a conversational model)
@st.cache_resource
def load_chatbot():
    """
    Load the DialoGPT-small model for conversational AI.
    Cached to avoid reloading on every run.
    """
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")
    return chatbot

chatbot = load_chatbot()

# App title and description
st.title("Personal Finance Chatbot")
st.write("Ask me about savings, taxes, and investments for intelligent guidance!")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def generate_response(user_input):
    """
    Generate a response based on user input.
    Uses keyword detection for specific finance topics,
    falls back to AI model for general queries.
    """
    # Basic keyword-based guidance
    user_input_lower = user_input.lower()
    if any(keyword in user_input_lower for keyword in ["save", "saving", "savings"]):
        return "Saving money is crucial for financial security. Aim to save at least 20% of your income. Consider automated transfers to a savings account. For example, if you earn $3000/month, save $600. Over time, this builds wealth."
    elif any(keyword in user_input_lower for keyword in ["tax", "taxes"]):
        return "Taxes can be complex. Keep records of all income and deductions. Use tax software or consult a professional. Common deductions include mortgage interest, charitable donations, and business expenses. File on time to avoid penalties."
    elif any(keyword in user_input_lower for keyword in ["invest", "investment", "investing"]):
        return "Investing helps grow your money. Start with low-risk options like index funds. Diversify across stocks, bonds, and real estate. Understand your risk tolerance and invest regularly. Remember, past performance doesn't guarantee future results."
    else:
        # Use the AI model for other queries
        try:
            from transformers import Conversation
            conversation = Conversation(user_input)
            response = chatbot(conversation)
            return response.generated_responses[-1]
        except Exception as e:
            return "I'm sorry, I couldn't process that. Can you ask about savings, taxes, or investments?"

# Simple savings calculator in sidebar
st.sidebar.header("Savings Calculator")

currency = st.sidebar.selectbox("Select Currency", ["INR (₹)", "USD ($)"])

principal_label = "Initial Amount (₹)" if currency == "INR (₹)" else "Initial Amount ($)"
principal = st.sidebar.number_input(principal_label, min_value=0.0, value=1000.0)

rate = st.sidebar.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0)
time = st.sidebar.number_input("Years", min_value=1, value=10)

if st.sidebar.button("Calculate"):
    amount = principal * (1 + rate/100)**time
    symbol = "₹" if currency == "INR (₹)" else "$"
    st.sidebar.write(f"Future Value: {symbol}{amount:.2f}")

# User input field
user_input = st.text_input("You:", key="input")

# Process user input and generate response
if user_input:
    response = generate_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
