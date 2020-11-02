#!/usr/bin/env python3
"""
    Obfuscated and replace with regex
    Provide Log formatter
    Create logger
"""
import os
import logging
import mysql.connector
from re import sub
from typing import List


PII_FIELDS = ("name", "phone", "email", "ssn", "ip")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get a point of connection toward the database

        Return:
            A connection toward the database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    passw = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    hosting = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')

    medb = mysql.connector.connect(
        host=hosting,
        username=username,
        password=passw
    )

    return medb


def get_logger() -> logging.Logger:
    """Set the format of the record

        Return:
            The function overloaded to make a new log with all items
    """
    log: logging.Logger = logging.getLogger('user_data')
    print(type(log))

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    print(type(stream_handler))
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter((RedactingFormatter(fields=PII_FIELDS)))
    stream_handler.formatter(formatter)

    log.addHandler(stream_handler)
    log.propagate = False

    return log


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """
        Filter and obfuscated the string

        Args:
            fields: a list of strings representing all fields to obfuscate
                    ["password", "date_of_birth"]
            redaction: a string representing by what the
                       field will be obfuscated
                       "XXXXX"
            message: a string representing the log line
                    ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"]
                    ["name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]
            separator: a string representing by which character is
                    separating all fields in the log line (message)
                    ";"
        Return:
            String with string ofuscated
    """
    for field in fields:
        message = sub(f'{field}=.+?{separator}',
                      f'{field}={redaction}{separator}', message)

    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
            Set the format of the record

            Args:
                record: Log record of a event

            Return:
                The function overloaded to make a new log with all items
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)

        return (super(RedactingFormatter, self).format(record))
