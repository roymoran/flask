# pylint: disable=line-too-long
"""Entry point for flask app."""
import os
from flask import Flask, Response
from flask_cors import CORS
from src.app.init_logger import InitLogger

logger = InitLogger.instance('app', os.environ["APP_ENV"])
logger.info('app started')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def root():
    """root index"""
    return Response(status="200")

@app.route("/info", methods=["GET"])
def info():
    """app info"""
    return {
        'version': 'v0.0.2',
    }