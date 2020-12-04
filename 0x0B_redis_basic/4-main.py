#!/usr/bin/env python3
""" Test replay calls """
from exercise import *

cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
