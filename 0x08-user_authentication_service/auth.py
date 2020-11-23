#!/usr/bin/env python3
"""
    Encrypt a string
"""
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


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


def _generate_uuid(self) -> str:
    """ Generate uuid
        Return:
            uuid in string
    """
    UUID = str(uuid4())

    return UUID


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Verify is there a valid login

            Args:
                email: email of the user
                password: string hashed

            Return:
                True If its valid information
        """
        if email is None or password is None:
            return False

        try:
            user: User = self._db.find_user_by(email=email)
            passwd: bytes = str.encode(user.hashed_password)
            valid: bool = bcrypt.checkpw(password.encode('utf-8'),
                                         passwd)

            return valid
        except NoResultFound:
            return False
