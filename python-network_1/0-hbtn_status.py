"""
Represents how to fetch a url using a link

"""
import requests

if __name__ == "__main__":

    # url = "https://alu-intranet.hbtn.io/status"
    r = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)