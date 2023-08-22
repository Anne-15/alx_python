"""
Represents how to fetch a url using a link

"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://github.com/{Anne-15}"
    "https://api.github.com/authorizations"
    r = requests.get(url).json()
    print(r)