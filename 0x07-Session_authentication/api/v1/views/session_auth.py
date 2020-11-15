#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from os import getenv
from models.user import User
from typing import TypeVar, List


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def new_view_session():
    """ New view session

        Args:
            request: Look the request

        Return:
            User instance based in cooikie
    """
    email = request.form.get('email')
    passwd = request.form.get('password')

    if email is None or email == '':
        return make_response(jsonify({"error": "email missing"}), 400)

    if passwd is None or passwd == '':
        return make_response(jsonify({"error": "password missing"}), 400)

    exist_user: TypeVar('User')

    try:
        exist_user = User.search({"email": email})[0]
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not exist_user.is_valid_password(passwd):
        return make_response(jsonify({"error": "wrong password"}), 401)

    from api.v1.app import auth
    session_id = auth.create_session(exist_user.id)

    user = exist_user.to_json()

    response = jsonify(user)
    response.set_cookie('SESSION_NAME', session_id)

    return response
