"""
Represents how to fetch a url using a link

"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    if request.status_code >= 400:
        print("Error code: ", request.status_code)
    else:
        print(request.text)