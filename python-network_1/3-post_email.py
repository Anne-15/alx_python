"""
Represents how to fetch a url using a link

"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5050"
    # email = "test@test.com"
    payload = {"email":"test@test.com"}
    request = requests.post(url, data=payload)
    print("Your email is: {}".format(request.text))