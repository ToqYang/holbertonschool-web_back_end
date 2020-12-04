#!/usr/bin/env python3
"""
    String Redis
"""
from uuid import uuid4
from typing import Union, Callable
from functools import wraps
import redis


def count_calls(method: Callable = None) -> Callable:
    """ Decorator count calls """
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper method """
        self._redis.incr(name)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator call history """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wraper function """
        input: str = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper



class Cache:
    """ Functionality Redis """

    def __init__(self):
        """ Constructor """
        self._redis=redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Store the cache

            Args:
                data: bring the information to store

            Return:
                Key or number uuid
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable= None)\
            -> Union[str, bytes, int, float]:
        """
            Store the cache

            Args:
                data: bring the information to store

            Return:
                Key or number uuid
        """
        key = self._redit.get(key)

        if fn:
            return fn(key)

        return key

    def get_str(self, key: str) -> str:
        """ Parametrized get str """
        return self._redit.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Parametrized get int """
        value=self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0

        return value
