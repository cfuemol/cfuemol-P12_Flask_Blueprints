import os
import logging
from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    logging.info('GET /')
    return "<h1>Página Principal</h1>"

@main_bp.route('/info')
def info():
    logging.info("GET /info")
    instance = os.getenv("HOSTNAME", "unknown")
    port = os.getenv("PORT", "8080")
    return jsonify({"instance": instance, "port": port})