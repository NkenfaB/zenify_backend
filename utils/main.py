# from utils import recognize_speech, chat_with_user
# from .chat_bot import *
# from .speech_recognition import *
from speech_recognition import recognize_speech
# from gemini_bot import chat_with_user
from gemini_health_bot import chat_with_bot

def main():
    # chat_history = []
    
    bot_response = chat_with_bot()

    # speech_result = recognize_speech()
    # bot_response = chat_with_user(speech_result,conversation_history)

    # conversation_history.append({"role": "user", "content": speech_result})
    # conversation_history.append({"role": "assistant", "content": bot_response})
    

    # print(bot_response)

if __name__ == "__main__":
    main()
