#!/usr/bin/env python3
""" Ofuscated and replace with regex """
from re import sub
from typing import List


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """
        Args:
            fields: a list of strings representing all fields to obfuscate
            redaction: a string representing by what the
                       field will be obfuscated
            message: a string representing the log line
            separator: a string representing by which character is
                    separating all fields in the log line (message)
        Return:
            String with string ofuscated
    """
    for field in fields:
        message = sub(f'{field}=.+?{separator}',
                      f'{field}={redaction}{separator}', message)

    return message
