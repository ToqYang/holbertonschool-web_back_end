#!/usr/bin/env python3
""" Module of Session Auth
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import Dict
from uuid import uuid4, UUID


class SessionAuth(Auth):
    """ Auth Class """
    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """
            Make a new Session and register in the class

            Args:
                user_id: Identificator of the user_id

            Return:
                Session ID
        """
        if user_id is None or type(user_id) is not str:
            return None

        print(type(user_id))
        session_id: str = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
