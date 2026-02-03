import logging
from flask import Flask
from .routes import main_bp
from .api import api_bp

def create_app():
    app = Flask(__name__)

    # Logging
    logging.basicConfig(filename='logs/app.log', level=logging.INFO)

    # Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app