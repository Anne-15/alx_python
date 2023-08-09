"""
Represents how to fetch a url using a link

"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    request = requests.post(url, data=payload)
    print("Your email is: {}".format(request.text))