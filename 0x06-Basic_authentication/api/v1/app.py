#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = getenv('AUTH_TYPE')

if auth:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def handle_req():
    if auth:
        expath = ['/api/v1/status/', '/api/v1/unauthorized/',
                  '/api/v1/forbidden/']
        if (auth.require_auth(request.path, expath)):
            if (auth.authorization_header(request.headers)):
                if (auth.current_user(request.remote_user)):
                    pass
                else:
                    return abort(403)
            else:
                return abort(401)
        else:
            pass

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
        Handle a unauthorized access

        Args:
            error: Error catch

        Return:
            Info of the error
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
        Handle a forbidden resource

        Args:
            error: Error catch

        Return:
            Info of the error
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
