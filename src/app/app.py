# pylint: disable=line-too-long
"""Entry point for discord flask app."""
import os
from flask import Flask, Response
from src.app.init_logger import InitLogger

logger = InitLogger.instance('app', os.environ["APP_ENV"])
logger.info('app started')

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    """root index"""
    return Response(status="200")
