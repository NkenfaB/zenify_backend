from flask import Flask, request
from flask_cors import CORS
from db.db import create_app
from routes.auth_routes import auth_routes
from dotenv import load_dotenv
from config import Config
# from controller.chat_controller import chat_controller
# from controller.speech_controller import speech_controller
import os
load_dotenv()

app = create_app()

CORS(app, resources={r"/*": {"origins": "https://blue-dune-091d25a0f.4.azurestaticapps.net"}})

# Handle preflight requests (OPTIONS)
@app.before_request
def handle_options_request():
    if request.method == 'OPTIONS':
        return '', 200

app.register_blueprint(auth_routes, url_prefix='/api/auth')
#app.register_blueprint(chat_controller, url_prefix='/api')
#app.register_blueprint(speech_controller, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)


# import os
# from flask import Flask
# from config import Config

# # Import your controllers
# from controller.chat_controller import chat_controller
# from controller.speech_controller import speech_controller


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     # Register Blueprints
#     app.register_blueprint(chat_controller, url_prefix='/api')
#     app.register_blueprint(speech_controller, url_prefix='/api')
    

#     return app

# if __name__ == '__main__':
#     # Create the Flask app
#     flask_app = create_app()
#     # Run the server
#     flask_app.run(debug=True, host='0.0.0.0', port=5000)