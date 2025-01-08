# zenify_backend/app.py

import os
from flask import Flask
from config import Config

# Import your controllers
from controller.chat_controller import chat_controller
from controller.speech_controller import speech_controller


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(chat_controller, url_prefix='/api')
    app.register_blueprint(speech_controller, url_prefix='/api')
    

    return app

if __name__ == '__main__':
    # Create the Flask app
    flask_app = create_app()
    # Run the server
    flask_app.run(debug=True, host='0.0.0.0', port=5000)
