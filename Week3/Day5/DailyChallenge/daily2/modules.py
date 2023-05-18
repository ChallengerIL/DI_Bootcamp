# MODULES
# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

import requests
import time

URL = 'https://imdb.com'


def loading_speed_test(url: str = URL):
    return requests.get(url).elapsed.total_seconds()


def loading_speed_test2(url: str = URL):
    start = time.time()
    requests.get(url)
    end = time.time()
    return end - start


print(loading_speed_test())
print(loading_speed_test2())
