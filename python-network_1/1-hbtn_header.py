"""
Represents how to fetch a url using a link

"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("No X-Request-Id header found in the response.")
    else:
        print(f"Request failed with status code: {response.status_code}")