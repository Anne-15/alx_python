"""
Represents how to fetch a url using a link

"""
import requests

if __name__ == "__main__":
    # url = "https://alu-intranet.hbtn.io/status"
    r = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(r.text))
    if "Custom status" in r.text:
        print("\t- content: Custom status")
    else:
        print("\t- content:", r.text)
    # r.json()