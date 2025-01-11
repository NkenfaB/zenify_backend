import os
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv('GEMINI_KEY')
gemini_model = os.getenv('GEMINI_MODEL')

# Configure the generative AI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(gemini_model)

chat_route = Blueprint('chat_controller', __name__)

@chat_route.route('/chat', methods=['POST'])
def chat_with_bot():
    """
    Example endpoint to handle user messages to the mental health chatbot.
    Expects JSON { 'message': 'user message' }
    """
    # The system prompt can live here or be loaded from a config or text file
    system_prompt = """You are a mental health assessment chatbot. Your role is to:
    1. Ask relevant diagnostic questions based on standard mental health assessments
    2. Show empathy and professional courtesy
    3. Collect information systematically
    4. Never provide medical advice or diagnosis
    5. Direct users to professional help when necessary
    """

    user_data = request.get_json()
    user_input = user_data.get('message', '')

    # Start a chat session with the model
    chat = model.start_chat(
        history=[
            {"role": "model", "parts": system_prompt},
            {"role": "user", "parts": user_input}
        ]
    )
    response = chat.send_message(user_input)

    return jsonify({
        "response": response.text
    })
