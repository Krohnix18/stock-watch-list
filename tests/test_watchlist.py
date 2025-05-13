from flask import Flask
from app.routes import app as flask_app

def test_app_starts():
    assert isinstance(flask_app, Flask)