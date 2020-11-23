#!/usr/bin/env python3
""" Flask module """
from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """ Logout session

        args:
            session_id

        return
            redirect main or 403 error
    """
    session_id = request.cookies.get('session_id', None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/', code=302)


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """ Sessions Login User """
    try:
        email = request.form['email']
        pwd = request.form['password']
    except KeyError:
        abort(401)

    if (AUTH.valid_login(email, pwd)):
        session_id = AUTH.create_session(email)
        if session_id is not None:
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response

    abort(401)


@app.route('/', methods=['GET'])
def hello_world() -> str:
    """ Greetings """
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """ Make a new user """
    try:
        email = request.form['email']
        pwd = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, pwd)
    except ValueError:
        msg = {"message": "email already registered"}
        return jsonify(msg), 400

    msg = {"email": user.email, "message": "user created"}

    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
