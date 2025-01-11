from flask import Flask, request
from flask_cors import CORS
from db.db import create_app
from routes.auth_routes import auth_routes
from dotenv import load_dotenv
from config import Config
import os

load_dotenv()

app = create_app()

# Update these values with your actual allowed domain(s)
ALLOWED_ORIGINS = [
    "https://blue-dune-091d25a0f.4.azurestaticapps.net",
    # If you have more domains, add them here
    # "https://some-other-domain.com",
]

# Configure Flask-CORS
# - resources: specify which URL patterns need CORS
# - origins:   specify the allowed domains
# - methods:   specify which methods can be used
# - allow_headers: which request headers are allowed
CORS(
    app,
    resources={r"/api/*": {"origins": ALLOWED_ORIGINS}},
    supports_credentials=True,
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
)

# Handle preflight requests (OPTIONS)
@app.before_request
def handle_options_request():
    if request.method == 'OPTIONS':
        return '', 200

# Register your blueprints
app.register_blueprint(auth_routes, url_prefix='/api/auth')
# app.register_blueprint(chat_controller, url_prefix='/api')
# app.register_blueprint(speech_controller, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
