from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=getenv("DATABASE_URL", "sqlite:///watchlist.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY="dev-secret")
    
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app