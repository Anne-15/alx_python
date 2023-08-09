"""
Represents how to fetch a url using a link

"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url, allow_redirects=True)
    print(r.headers)
    x_request_id = r.headers.get('X-Request-Id')
    print(x_request_id)