#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from os import getenv
from models.user import User
from typing import TypeVar, List


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ New view session

        Args:
            request: Look the request

        Return:
            User instance based in cooikie
    """
    email = request.form.get('email')

    if not email:
        return make_response(jsonify({"error": "email missing"}), 400)

    passwd = request.form.get('password')
    if not passwd:
        return make_response(jsonify({"error": "password missing"}), 400)

    exist_user: TypeVar('User')

    try:
        exist_user = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not exist_user:
        return jsonify({"error": "no user found for this email"}), 404

    from api.v1.app import auth
    for user in exist_user:
        if (user.is_valid_password(passwd)):
            session_id = auth.create_session(user.id)
            response = make_response(user.to_json())
            response.set_cookie('SESSION_NAME', session_id)
            return response

    return make_response(jsonify({"error": "wrong password"}), 401)
