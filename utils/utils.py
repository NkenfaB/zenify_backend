import jwt
import datetime
from flask import current_app

def generate_token(data):
    return jwt.encode(
        {
            **data,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    )

def verify_token(token):
    try:
        return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
