#!/usr/bin/env python3
"""
    Encrypt a string
"""
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str = '') -> str:
    """
        Hashed the password

        Args:
            password: string to hashed
        Return:
            hashed password
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'),
                           bcrypt.gensalt(prefix=b"2b"))

    hash_str: str = str(hashed.decode())

    return hash_str


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            Register User

            Args:
                email: string with email user
                password: string to hashed

            Return:
                User registered
        """
        try:
            consult = self._db.find_user_by(email=email)
            raise ValueError(f'<{consult.email}> already exists.')

        except NoResultFound:
            passwd: str = _hash_password(password)
            user = self._db.add_user(email, passwd)

        return user
