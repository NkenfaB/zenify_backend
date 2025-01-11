from flask import Blueprint, request, jsonify
from models import User, db
from utils import generate_token, verify_token

auth_routes = Blueprint('auth', __name__)

# Sign Up Route
@auth_routes.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Log In Route
@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = generate_token({'id': user.id, 'email': user.email})
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Forgot Password Route
@auth_routes.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if user:
        token = generate_token({'id': user.id, 'email': user.email})
        # In a real app, send this token via email
        return jsonify({'reset_token': token}), 200
    else:
        return jsonify({'error': 'Email not found'}), 404
