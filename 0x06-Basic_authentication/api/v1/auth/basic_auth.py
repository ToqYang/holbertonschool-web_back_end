#!/usr/bin/env python3
""" Module of Basicauth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode, binascii


class BasicAuth(Auth):
    """ Basic Auth class """
    def __init__(self):
        """Constructor"""

    def extract_base64_authorization_header(
                                            self,
                                            authorization_header: str
                                            ) -> str:
        """
            Extract header in base64

            Args:
                authorization_header: string in base64

            Return:
                Header in base64
        """
        if authorization_header is None\
           or type(authorization_header) != str\
           or not authorization_header.startswith('Basic ')\
           and not authorization_header.endswith(' '):

            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header: str
                                            ) -> str:
        """
            Decode base64 header

            Args:
                base64_authorization_header: Base64 header

            Return:
                string header
        """
        if base64_authorization_header is None or\
           type(base64_authorization_header) != str:

            return None

        try:
            data_decode = b64decode(base64_authorization_header)
        except binascii.Error as err:
            return None

        return data_decode.decode('utf-8')
