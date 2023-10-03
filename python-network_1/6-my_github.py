#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    try:
        # Create a basic authentication string
        auth = (username, access_token)

        # Make a GET request to the GitHub API
        response = requests.get("https://api.github.com/user", auth=auth)

        # Check the status code
        if response.status_code == 200:
            # Display the user ID
            user_id = response.json()["id"]
            print(f"{user_id}")
        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print("None")
