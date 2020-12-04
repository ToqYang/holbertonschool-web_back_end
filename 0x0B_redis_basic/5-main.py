#!/usr/bin/env python3
""" Testing expiring web cache and tracker """

from web import get_page

URL: str = "http://slowwly.robertomurray.co.uk/delay/5300/url/http://www.google.co.uk"

print(get_page(URL))

print("----------------------------------\n" * 3)

print(get_page(URL))