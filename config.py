import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    AZURE_SPEECH_KEY = os.getenv('AZURE_SPEECH_KEY')
    AZURE_SPEECH_REGION = os.getenv('AZURE_SPEECH_REGION')
    AZURE_OPENAI_KEY = os.getenv('AZURE_OPENAI_KEY')
