from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "postgresql://zen_data_user:iUNhGc5a3pU1A6jauu8uLBhNGPzHpGti@dpg-cu0qa8dsvqrc73eilv1g-a.oregon-postgres.render.com/zen_data"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Create all tables
    with app.app_context():
        db.create_all()

    return app