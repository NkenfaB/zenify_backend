# zenify_backend/app.py

import os
from flask import Flask
from config import Config
from db.db import create_app, db

# Import your controllers
from controller.chat_controller import chat_controller
from controller.speech_controller import speech_controller
from routes.auth_routes import auth_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(chat_controller, url_prefix='/api')
    app.register_blueprint(speech_controller, url_prefix='/api')
    app.register_blueprint(auth_routes, url_prefix='/api/auth')

    

    return app

if __name__ == '__main__':
    # Create the Flask app
    flask_app = create_app()
    # Run the server
    flask_app.run(debug=True, host='0.0.0.0', port=5000)
