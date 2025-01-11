from flask import Flask, request
from flask_cors import CORS
from db.db import create_app
from routes.auth_routes import auth_routes
from routes.chat_route import auth_routes
from routes.community_routes import auth_routes
from routes.gemini_route import auth_routes
from routes.speech_route import auth_routes
from routes.user_routes import auth_routes
from dotenv import load_dotenv
from config import Config
import os

load_dotenv()

app = create_app()

# Define allowed origins
ALLOWED_ORIGINS = [
    "https://blue-dune-091d25a0f.4.azurestaticapps.net",
]

# Configure Flask-CORS
CORS(
    app,
    resources={r"/api/*": {"origins": ALLOWED_ORIGINS}},
    supports_credentials=True,
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
)

# Register your blueprints after setting up CORS
app.register_blueprint(auth_routes, url_prefix='/api/auth')
# app.register_blueprint(chat_controller, url_prefix='/api')
# app.register_blueprint(speech_controller, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
