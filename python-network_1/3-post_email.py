"""
Represents how to fetch a url using a link

"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    request = requests.post(url, params=email)
    print(request)