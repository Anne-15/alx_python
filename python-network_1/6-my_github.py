"""
Represents how to fetch a url using a link

"""
import requests
import sys

if __name__ == "__main__":
    url = "https://github.com/Anne-15"
    r = requests.get(url, auth=('user', 'pass'))
    print(r.text)