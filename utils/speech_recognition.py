
import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

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

def recognize_speech():
    speech_recognizer = setup_speech_recognition()

    # Prompt user to say something
    print("Please say something...")

    # Start recognition
    result = speech_recognizer.recognize_once()

    # Check result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"You said: {result.text}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")

    return result.text
# Call the function to start speech recognition
# recognize_speech()