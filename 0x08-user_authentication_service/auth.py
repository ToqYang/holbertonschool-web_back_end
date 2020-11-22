#!/usr/bin/env python3
"""
    Encrypt a string
"""
import bcrypt


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
