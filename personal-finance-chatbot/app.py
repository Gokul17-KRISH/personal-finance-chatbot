import streamlit as st
from transformers import pipeline
import re

# Initialize the HuggingFace conversational model pipeline
@st.cache(allow_output_mutation=True)
def load_hf_chatbot():
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
    return chatbot

hf_chatbot = load_hf_chatbot()

# Enhanced financial advice database
FINANCIAL_ADVICE = {
    "savings": [
        "Try to save at least 20% of your income each month for emergencies and future goals.",
        "Use the 50/30/20 rule: 50% for needs, 30% for wants, 20% for savings and debt.",
        "Set up automatic transfers to your savings account right after payday.",
        "Build an emergency fund covering 3-6 months of living expenses.",
        "Consider high-yield savings accounts for better interest rates on your savings."
    ],
    "investing": [
        "Start investing early - compound interest works best over long time periods.",
        "Diversify your portfolio across stocks, bonds, and other asset classes.",
        "Consider low-cost index funds or ETFs for beginner-friendly investing.",
        "Invest in your retirement accounts (401k, IRA) for tax advantages.",
        "Never invest money you can't afford to lose - only invest with your risk tolerance in mind."
    ],
    "budgeting": [
        "Track all your income and expenses for at least one month to understand your spending patterns.",
        "Use budgeting apps like Mint, YNAB, or Personal Capital to monitor your finances.",
        "Prioritize essential expenses (housing, food, utilities) before discretionary spending.",
        "Review your budget monthly and adjust as needed based on changing circumstances.",
        "Set specific, measurable financial goals to stay motivated with your budget."
    ],
    "debt": [
        "Focus on paying off high-interest debt first (credit cards, payday loans).",
        "Consider the debt snowball method: pay minimums on all debts, extra on smallest balance.",
        "Avoid taking on new debt while trying to pay off existing debt.",
        "Negotiate with creditors for lower interest rates or payment plans if struggling.",
        "Build good credit habits to qualify for better loan terms in the future."
    ],
    "taxes": [
        "Keep detailed records of all income, expenses, and receipts throughout the year.",
        "Maximize tax-advantaged accounts like 401k, IRA, and HSA contributions.",
        "Don't forget about state taxes - they vary significantly by location.",
        "Consider working with a tax professional for complex situations.",
        "File your taxes early to avoid penalties and get refunds sooner."
    ],
    "retirement": [
        "Start saving for retirement as early as possible - even small amounts compound over time.",
        "Contribute enough to your 401k to get the full employer match - it's free money!",
        "Consider Roth IRA for tax-free growth if you expect to be in a higher tax bracket later.",
        "Diversify retirement investments and rebalance periodically.",
        "Plan for healthcare costs in retirement - they're often underestimated."
    ]
}

def calculate_compound_interest(principal, rate, time, compounds_per_year=12):
    """Calculate compound interest"""
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)
    interest = amount - principal
    return round(amount, 2), round(interest, 2)

# Streamlit UI
st.set_page_config(page_title="Advanced Personal Finance Chatbot", page_icon="💰")

st.title("💰 Advanced Personal Finance Chatbot")
st.write("Get intelligent guidance on savings, investments, taxes, budgeting, and more!")

# Sidebar with additional features
st.sidebar.header("🧮 Financial Calculators")
st.sidebar.write("Try these calculators:")

if st.sidebar.button("Compound Interest Calculator"):
    st.sidebar.write("💡 Tip: Use 'calculate compound interest [principal] [rate] [years]' in chat")

if st.sidebar.button("Budget Planning Tips"):
    st.sidebar.write("💡 Tip: Ask about 'budgeting' or 'budget' in the chat")

st.sidebar.header("📊 Quick Stats")
st.sidebar.write("• 20% of income should go to savings")
st.sidebar.write("• Emergency fund: 3-6 months expenses")
st.sidebar.write("• Good credit score: 670+")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def generate_enhanced_response(user_input):
    user_input_lower = user_input.lower()

    # Check for calculator requests
    if "calculate" in user_input_lower or "calculator" in user_input_lower:
        if "compound" in user_input_lower or "interest" in user_input_lower:
            return handle_compound_interest_calculator(user_input)
        elif "loan" in user_input_lower or "mortgage" in user_input_lower:
            return "For loan calculations, please provide: principal amount, interest rate (%), and loan term in years."

    # Enhanced keyword matching with multiple categories
    matched_categories = []

    for category, advice_list in FINANCIAL_ADVICE.items():
        keywords = {
            "savings": ["save", "saving", "savings", "emergency fund"],
            "investing": ["invest", "investment", "investing", "stock", "bond", "portfolio"],
            "budgeting": ["budget", "budgeting", "spending", "expense", "income"],
            "debt": ["debt", "loan", "credit card", "payoff", "interest"],
            "taxes": ["tax", "taxes", "deduction", "refund", "filing"],
            "retirement": ["retirement", "401k", "ira", "pension", "social security"]
        }

        if any(keyword in user_input_lower for keyword in keywords.get(category, [])):
            matched_categories.append(category)

    # Generate response based on matched categories
    if matched_categories:
        response = "Here's some advice on "
        if len(matched_categories) == 1:
            response += f"{matched_categories[0]}:\n\n"
            category = matched_categories[0]
            advice = FINANCIAL_ADVICE[category]
            response += f"• {advice[0]}\n"
            response += f"• {advice[1]}\n"
            if len(advice) > 2:
                response += f"• {advice[2]}"
        else:
            response += "the topics you mentioned:\n\n"
            for category in matched_categories[:2]:  # Limit to 2 categories
                advice = FINANCIAL_ADVICE[category]
                response += f"**{category.title()}:**\n"
                response += f"• {advice[0]}\n\n"

        return response
    else:
        # Use HuggingFace conversational model for general queries
        from transformers import Conversation
        conversation = Conversation(user_input)
        response = hf_chatbot(conversation)
        return response.generated_responses[-1]

def handle_compound_interest_calculator(user_input):
    """Handle compound interest calculations from user input"""
    # Try to extract numbers from the input
    numbers = re.findall(r'\d+\.?\d*', user_input)

    if len(numbers) >= 3:
        try:
            principal = float(numbers[0])
            rate = float(numbers[1])
            time = float(numbers[2])

            final_amount, interest_earned = calculate_compound_interest(principal, rate, time)

            return f"Compound Interest Calculation:\n\n" \
                   f"Principal: ${principal:,.2f}\n" \
                   f"Interest Rate: {rate}%\n" \
                   f"Time Period: {time} years\n\n" \
                   f"Final Amount: ${final_amount:,.2f}\n" \
                   f"Interest Earned: ${interest_earned:,.2f}"
        except ValueError:
            return "Please provide valid numbers for principal, rate, and time period."

    return "For compound interest calculation, please provide: principal amount, interest rate (%), and time period in years.\n" \
           "Example: 'calculate compound interest 10000 5 10'"

def generate_response(user_input):
    # Keep the old function for backward compatibility
    return generate_enhanced_response(user_input)

# Main chat interface
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history with better formatting
for i, (speaker, message) in enumerate(st.session_state.chat_history):
    if speaker == "You":
        st.markdown(f"**👤 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
    if i < len(st.session_state.chat_history) - 1:
        st.markdown("---")

# User input
user_input = st.text_input("Ask me anything about personal finance:", key="input", placeholder="e.g., How should I start investing?")

if user_input:
    with st.spinner("Thinking..."):
        response = generate_response(user_input)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

    # Auto-scroll to bottom
    st.rerun()

# Footer
st.markdown("---")
st.markdown("*Powered by HuggingFace Transformers & Streamlit*")
