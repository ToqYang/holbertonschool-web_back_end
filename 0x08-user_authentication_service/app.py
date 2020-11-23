#!/usr/bin/env python3
""" Flask module """
from flask import Flask, jsonify, request, abort
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """ Sessions Login User """
    try:
        email = request.form['email']
        pwd = request.form['password']
    except KeyError:
        abort(401)

    if (AUTH.valid_login(email, pwd)):
        if (AUTH.create_session(email)) is not None:
            msg = {"email": email, "message": "logged in"}
            return jsonify(msg), 200

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
