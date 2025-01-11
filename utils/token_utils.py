import jwt
import datetime

SECRET_KEY = "your_secret_key"

def generate_token(data):
    return jwt.encode(
        {
            **data,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm='HS256'
    )

def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
