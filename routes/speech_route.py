# zenify_backend/controllers/speech_controller.py

import os
from flask import Blueprint, jsonify
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

speech_controller = Blueprint('speech_controller', __name__)

load_dotenv()
speech_key = os.getenv('AZURE_SPEECH_KEY')
service_region = os.getenv('AZURE_SPEECH_REGION')

def setup_speech_recognition():
    # Create a speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Create an audio configuration using the default microphone
    audio_config = speechsdk.AudioConfig(use_default_microphone=True)
    # Create a speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    return speech_recognizer

@speech_controller.route('/speech/recognize', methods=['GET'])
def recognize_speech():
    """
    Example endpoint to trigger speech recognition.
    This will listen via the microphone and return recognized text.
    """
    speech_recognizer = setup_speech_recognition()

    # Prompt (logging) user to say something
    print("Please say something...")

    # Start recognition
    result = speech_recognizer.recognize_once()

    text_recognized = ""
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        text_recognized = result.text
        print(f"You said: {text_recognized}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")

    return jsonify({"recognized_text": text_recognized})
