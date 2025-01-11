
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv('GEMINI_KEY')
gemini_model = os.getenv('GEMINI_MODEL')

# Configure the generative AI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(gemini_model)
from speech_recognition import recognize_speech


# def chat_with_bot():
#     system_prompt = """You are a mental health assessment chatbot. Your role is to:
#     1. Ask relevant diagnostic questions based on standard mental health assessments
#     2. Show empathy and professional courtesy
#     3. Collect information systematically
#     4. Never provide medical advice or diagnosis
#     5. Direct users to professional help when necessary"""

#     user_input = recognize_speech()

#     # model = genai.GenerativeModel("gemini-1.5-flash")
#     chat = model.start_chat(
#         history=[
#             {"role": "user", "parts": "Hello"},
#             {"role": "model", "parts": system_prompt},
#         ]
#     )
#     response = chat.send_message(user_input)
#     print(response.text)
#     # response = chat.send_message("How many paws are in my house?")
#     # print(response.text)

# chat_with_bot()

def chat_with_bot():
    system_prompt = """You are a mental health assessment chatbot. Your role is to:
    1. Ask relevant diagnostic questions based on standard mental health assessments
    2. Show empathy and professional courtesy
    3. Collect information systematically
    4. Never provide medical advice or diagnosis
    5. Direct users to professional help when necessary"""

    # Initialize chat history
    chat_history = [
        {"role": "model", "parts": system_prompt}
    ]

    while True:
        # Collect user input
        user_input = recognize_speech()
        
        if user_input:  # Ensure user input is valid
            chat_history.append({"role": "user", "parts": user_input})

            # Start chat with the current history
            chat = model.start_chat(history=chat_history)
            response = chat.send_message(user_input)
            print("Chatbot:", response.text)

            # Append the assistant's response to chat history
            chat_history.append({"role": "model", "parts": response.text})
        else:
            print("No valid input received from the user.")

        # Optionally, add a way to exit the chat
        if user_input and "exit" in user_input.lower():
            print("Ending the chat.")
            break

# Run the chatbot
# chat_with_bot()