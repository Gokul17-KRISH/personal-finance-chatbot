# Personal Finance Chatbot

This is an advanced Personal Finance Chatbot built with Python, Streamlit, IBM Watson, HuggingFace Transformers, and Granite integration. It provides intelligent guidance on savings, taxes, investments, budgeting, debt management, and retirement planning using AI-powered natural language processing and conversational AI.

## Features

- **AI-Powered Conversations**: Uses HuggingFace DialoGPT for natural language understanding
- **IBM Watson Integration**: Advanced natural language processing and sentiment analysis
- **Financial Calculators**: Built-in compound interest calculator
- **Comprehensive Financial Advice**: Covers savings, investing, budgeting, debt, taxes, and retirement
- **Interactive Chat Interface**: User-friendly Streamlit web interface
- **Real-time Responses**: Instant financial guidance and calculations

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **IBM Watson**: Natural Language Understanding and Assistant services
- **HuggingFace Transformers**: Pre-trained conversational AI models
- **Granite**: Advanced AI model integration for enhanced responses

## Setup Instructions

### 1. IBM Watson Setup

1. Create an IBM Cloud account at [IBM Cloud](https://cloud.ibm.com)
2. Create Watson Assistant and Natural Language Understanding services
3. Get your API keys and service URLs from the IBM Cloud dashboard
4. Update the `.env` file with your credentials:
   ```
   WATSON_ASSISTANT_API_KEY=your_actual_api_key
   WATSON_ASSISTANT_URL=your_actual_service_url
   WATSON_NLU_API_KEY=your_actual_nlu_api_key
   WATSON_NLU_URL=your_actual_nlu_url
   WATSON_ASSISTANT_ID=your_assistant_id
   WATSON_SESSION_ID=your_session_id
   ```

### 2. Local Development Setup

1. Clone or download the project
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   # Copy .env.example to .env and fill in your IBM Watson credentials
   cp .env.example .env
   ```
5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
6. Open your browser at `http://localhost:8501`

### 3. Deployment to Streamlit Cloud

1. Create a free account at [Streamlit Cloud](https://streamlit.io/cloud)
2. Push your project to a GitHub repository
3. Connect your GitHub repo to Streamlit Cloud
4. Set up the following secrets in Streamlit Cloud:
   - `WATSON_ASSISTANT_API_KEY`
   - `WATSON_ASSISTANT_URL`
   - `WATSON_NLU_API_KEY`
   - `WATSON_NLU_URL`
   - `WATSON_ASSISTANT_ID`
   - `WATSON_SESSION_ID`
5. Deploy the app
6. Share the live demo URL

## Usage Examples

Ask the chatbot about:
- "How should I start saving money?"
- "What's the best way to invest $10,000?"
- "How do I create a budget?"
- "Calculate compound interest 10000 5 10"
- "What are the best tax saving strategies?"
- "How should I plan for retirement?"

## Hackathon Submission Tips

- **Demo URL**: Provide the Streamlit Cloud deployment URL
- **GitHub Repo**: Share your repository link
- **Screenshots**: Include screenshots of the chat interface
- **Video Demo**: Record a short demo video showing the features
- **Technical Details**: Highlight the IBM Watson, HuggingFace, and Granite integration
- **Innovation**: Emphasize the AI-powered financial guidance capabilities

## Troubleshooting

1. **Watson API Errors**: Ensure your API keys and URLs are correct in the `.env` file
2. **Model Loading Issues**: The first run may take time to download AI models
3. **Deployment Issues**: Check that all environment variables are set in Streamlit Cloud secrets

## Contributing

Feel free to enhance the chatbot with additional features like:
- More financial calculators
- Integration with financial APIs
- Advanced portfolio analysis
- Machine learning-based recommendations

If you need help with any setup steps, feel free to ask!
